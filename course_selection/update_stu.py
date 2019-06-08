import pandas
import pymysql

# 读取excel数据
data = pandas.read_excel('data/student.xlsx')
# 打开数据库连接
db = pymysql.connect("62.234.121.2","testuser","mysqlNo.1","EduManage" )

def select(id):
    cursor = db.cursor()
    sql = "select * from course_selection_student where stuid_id=('%s')" % (id)
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
        return results
    except:
        print("查询出错")

def update(stuid, name):
    subject = stuid[2:8]
    cursor = db.cursor()
    row = select(stuid)
    if row == None:
        sql = "insert into course_selection_student(stuid_id, name, subject_id) \
            values ('%s', '%s', '%s')" % (stuid, name, subject)
    else:
        sql = "update course_selection_student set name=('%s') where stuid_id = ('%s')" % (name, stuid)
    try:
        cursor.execute(sql)
        db.commit()
        print('更新student %s 成功' %(stuid))
    except:
        db.rollback()
        sql2 = "insert into course_selection_user(id, password, flag) \
            values ('%s', '%s', '%s')" % (stuid, stuid, 10)
        cursor.execute(sql2)
        db.commit()
        print('创建user %s 成功' %(stuid))
        cursor.execute(sql)
        db.commit()
        print('创建student %s 成功' %(stuid))

cols = data.columns
if 'stuid' in cols:
    if 'name' in cols:
        data_dict = data.to_dict(orient = "records")
        for stu in data_dict:
            update(str(stu['stuid']), stu['name'])
    else:
        print('未找到name列，请检查您的文件')
else:
    print('未找到stuid列，请检查您的文件')

# 关闭数据库连接
db.close()