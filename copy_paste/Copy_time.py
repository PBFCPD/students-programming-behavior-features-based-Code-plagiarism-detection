import MySQLdb
import pandas as pd
from datetime import datetime

db1 = MySQLdb.connect("202.4.155.100", "root", "buctacm4726", "record", charset='utf8')
db2 = MySQLdb.connect("202.4.155.100", "root", "buctacm4726", "jol", charset='utf8')

cursor1 = db1.cursor()
cursor2 = db2.cursor()

cid = '2315'
resultnum1 = pd.DataFrame(columns=["用户名", "竞赛", "题目", "是否AC", "花费时间", "平均花费时间"])
savefile = '../excel/7-' + cid + '/' + cid + '_time.xlsx'

sqlnum = "SELECT MAX(num) FROM contest_problem WHERE contest_id = %s"
cursor2.execute(sqlnum, (cid, ))
resultnum = cursor2.fetchall()
maxnum = resultnum[0][0]

sql = "SELECT DISTINCT username FROM collectinfo WHERE contestid = %s"
cursor1.execute(sql, (cid, ))
results = cursor1.fetchall()
for row in results:
    username = row[0]
    for problemid in range(0,maxnum+1):
        sqlmin = "SELECT * FROM collectinfo WHERE contestid=%s and username=%s AND problemid = %s ORDER BY updatetime ASC LIMIT 1"
        cursor1.execute(sqlmin, (cid, username,problemid))
        resulttimemin = cursor1.fetchall()
        if(len(resulttimemin)>0):
            mintime = resulttimemin[0][4]
        else:
            mintime = '2020-03-02 15:00:00'

        sqlmax = "SELECT * FROM collectinfo WHERE contestid=%s and username=%s AND problemid = %s ORDER BY updatetime DESC LIMIT 1"
        cursor1.execute(sqlmax, (cid, username, problemid))
        resulttimemax = cursor1.fetchall()
        if (len(resulttimemin) > 0):
            maxtime = resulttimemax[0][4]
        else:
            maxtime = '2020-03-02 15:00:00'

        time_1_struct = datetime.strptime(mintime, "%Y-%m-%d %H:%M:%S")
        time_2_struct = datetime.strptime(maxtime, "%Y-%m-%d %H:%M:%S")
        seconds = (time_2_struct - time_1_struct).seconds

        sqlcor = "SELECT * FROM solution WHERE contest_id = %s AND num=%s AND user_id=%s AND result='4'"
        cursor2.execute(sqlcor, (cid, problemid, username))
        resultcor = cursor2.fetchall()
        if(len(resultcor) > 0):
            correct = 1
        else:
            correct = 0

        resultnum1 = resultnum1.append(
            {"用户名": username, "竞赛": cid, "题目": problemid, "是否AC": correct, "花费时间": seconds, "平均花费时间": ''}, ignore_index=True)
        resultnum1.to_excel(savefile, index=False)
        print(username, problemid, seconds, correct)




