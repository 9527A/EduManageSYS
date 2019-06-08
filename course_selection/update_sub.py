import pandas
import pymysql

# 读取excel数据
data = pandas.read_excel('data/subject.xlsx')
# 打开数据库连接
db = pymysql.connect("62.234.121.2","testuser","mysqlNo.1","EduManage" )

def select(id):
    cursor = db.cursor()
    sql = "select * from course_selection_subject where subid=('%d')" % (id)
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
        return results
    except:
        print("查询出错")

def update(subid, name):
    cursor = db.cursor()
    row = select(subid)
    if row == None:
        sql = "insert into course_selection_subject(subid, name) \
            values ('%d', '%s')" % (subid, name)
    else:
        sql = "update course_selection_subject set name=('%s') where subid = ('%d')" % (name, subid)
    try:
        cursor.execute(sql)
        db.commit()
        print('更新subject %d 成功' %(subid))
    except:
        db.rollback()
        print('出现错误')

cols = data.columns
if 'subid' in cols:
    if 'name' in cols:
        data_dict = data.to_dict(orient = "records")
        for sub in data_dict:
            update(sub['subid'], sub['name'])
    else:
        print('未找到name列，请检查您的文件')
else:
    print('未找到subid列，请检查您的文件')

# 关闭数据库连接
db.close()