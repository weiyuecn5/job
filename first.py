import sqlite3
import os,shutil,time
# 这是处理数据库的脚本

# 1.批量修改 是否已卖状态 默认值为0,已卖为1
def isbuy():
    conn = sqlite3.connect('db.sqlite3') #链接数据库
    c = conn.cursor()
    c.execute("UPDATE pad_shujuku set 已卖 = '0' where 已卖='1'")
    print('完成')
    conn.commit()
    conn.close()

# 2.批量升级数据 未上传为0,上传了为1
def upshuju():
    if os.path.isfile('db1.sqlite3'):
         os.remove('db1.sqlite3')
         shutil.copyfile('db.sqlite3','db1.sqlite3')
    else:
        shutil.copyfile('db.sqlite3', 'db1.sqlite3')

    conn = sqlite3.connect('db.sqlite3') #链接数据库
    c = conn.cursor()

    conn1 = sqlite3.connect('db1.sqlite3') #链接数据库
    d = conn1.cursor()

    datas=d.execute("SELECT * from pad_huancun")
    for data in datas:
        if data[5]=='1':
            print(data[0],data[1],data[2],data[3],data[4],data[6])
            c.execute("SELECT 宠物 FROM pad_shujuku WHERE 账号编号='%s'"%(data[1]))
            ycw=c.fetchone()
            # print(ycw[0])
            xcw=ycw[0]+data[4]+','
            sql = "UPDATE pad_shujuku set 石头数量 = '%s',等级='%s',宠物='%s',更新时间='%s' where 账号编号='%s'"%(data[2],data[3],xcw,data[6],data[1])
            c.execute(sql)
            c.execute("UPDATE pad_huancun set 是否上传 = '0' where 唯一键='%s'"%(data[0]))
        # break
        time.sleep(0.1)
    conn.commit()
    conn.close()

isbuy()