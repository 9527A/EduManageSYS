import pandas
import pymysql

# 读取excel数据
data = pandas.read_excel('data/course.xlsx')
# 打开数据库连接
db = pymysql.connect("62.234.121.2","testuser","mysqlNo.1","EduManage" )

def select(id):
    # 查询课程是否存在
    cursor = db.cursor()
    sql = "select * from course_selection_course where couid=('%d')" % (id)
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
        return results
    except:
        print("查询课程出错")

def cou_to_sub(couid, subids):
    cursor = db.cursor()
    # 查询数据库中和当前课程有关系的学科id
    sql = "select subject_id from course_selection_course_subject where course_id=('%d')" % (couid)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except:
        print("查询课程与学科的关系出错")
    # 开始清洗数据
    subids_online = []
    for row in results:
        subids_online.append(int(row[0]))
    subids_local = []
    for i in subids:
        subids_local.append(int(i))
    # 求差集，数据库里有而本地没有的，需要删除；本地有而数据库里没有的，需要添加
    subids_create = list(set(subids_local).difference(set(subids_online)))
    subids_delete = list(set(subids_online).difference(set(subids_local)))
    if subids_create == []:
        print('课程%d和学科没有需要添加的多对多关系'%(couid))
    else:
        for subid in subids_create:
            sql2 = "insert into course_selection_course_subject(course_id, subject_id) \
                values ('%d', '%d')" % (couid, int(subid))
            cursor.execute(sql2)
            db.commit()
            print('创建 %d to %d 关系成功' %(couid, subid))

    if subids_delete == []:
        print('课程%d和学科没有需要删除的多对多关系'%(couid))
    else:
        for subid in subids_delete:
            sql3 = "delete from course_selection_course_subject where course_id=('%d') and subject_id=('%d')" % (couid, int(subid))
            cursor.execute(sql3)
            db.commit()
            print('删除 %d to %d 关系成功' %(couid, subid))

def update(couid, name, flag, maxnum, subids):
    cursor = db.cursor()
    row = select(couid)
    if row == None:
        sql = "insert into course_selection_course(couid, name, flag, maxnum) \
            values ('%d', '%s', '%d', '%d')" % (couid, name, flag, maxnum)
        try:
            cursor.execute(sql)
            db.commit()
            print('创建course %d 成功' %(couid))
        except:
            db.rollback()
            print('创建课程出错')
    else:
        sql1 = "update course_selection_course set name=('%s') where couid = ('%d')" % (name, couid)
        sql2 = "update course_selection_course set flag=('%d') where couid = ('%d')" % (flag, couid)
        sql3 = "update course_selection_course set maxnum=('%d') where couid = ('%d')" % (maxnum, couid)
        try:
            cursor.execute(sql1)
            cursor.execute(sql2)
            cursor.execute(sql3)
            db.commit()
            print('更新course %d 成功' %(couid))
        except:
            db.rollback()
            print('更新课程出错')

    if flag == 0:
        sql = "select subid from course_selection_subject"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
        except:
            print("查询学科出错")
        subids = []
        for row in results:
            subids.append(row[0])
    cou_to_sub(couid, subids)

# 取得列名
cols = data.columns
if 'couid' in cols:
    if 'name' in cols:
        if 'flag' in cols:
            if 'subject' in cols:
                if 'maxnum' in cols:
                    data['maxnum'] = data['maxnum'].fillna(99999)
                    data_dict = data.to_dict(orient = "records")
                    for cou in data_dict:
                        sub = str(cou['subject']).split(" ")
                        update(int(cou['couid']), cou['name'], int(cou['flag']), int(cou['maxnum']), sub)
                else:
                    print('未找到maxnum列，请检查您的文件')
            else:
                print('未找到subject列，请检查您的文件')
        else:
            print('未找到flag列，请检查您的文件')
    else:
        print('未找到name列，请检查您的文件')
else:
    print('未找到couid列，请检查您的文件')
# 关闭数据库连接
db.close()