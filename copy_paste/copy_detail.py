import MySQLdb
import pandas as pd
from datetime import datetime

db1 = MySQLdb.connect("202.4.155.100", "root", "buctacm4726", "record", charset='utf8')
db2 = MySQLdb.connect("202.4.155.100", "root", "buctacm4726", "jol", charset='utf8')

cursor1 = db1.cursor()
cursor2 = db2.cursor()

cid = '2315'

if(cid == '2167'):
    start_time = '2021-10-14 18:00:00'
    endtime = '2021-10-14 19:00:00'
elif(cid == '2180'):
    start_time = '2021-10-21 18:00:00'
    endtime = '2021-10-21 19:00:00'
elif(cid == '2196'):
    start_time = '2021-10-28 18:00:00'
    endtime = '2021-10-28 19:00:00'
elif(cid == '2217'):
    start_time = '2021-11-04 18:00:00'
    endtime = '2021-11-04 19:00:00'
elif(cid == '2232'):
    start_time = '2021-11-11 18:00:00'
    endtime = '2021-11-11 19:00:00'
elif(cid == '2262'):
    start_time = '2021-11-30 19:00:00'
    endtime = '2021-12-06 22:00:00'
elif(cid == '2315'):
    start_time = '2021-12-21 19:00:00'
    endtime = '2021-12-27 22:00:00'

resultnum1 = pd.DataFrame(columns=["用户名", "竞赛", "最小化页面次数", "鼠标离开页面的时间", "调试次数", "终端输入次数"])
savefile = '../excel/7-' + cid + '/' + cid + '_detail.xlsx'

sql = "SELECT DISTINCT username FROM userstatus WHERE updatetime > %s AND updatetime < %s"
cursor1.execute(sql, (start_time, endtime))
results = cursor1.fetchall()

for row in results:
    username = row[0]
    sqlhidden = "SELECT count(*) FROM userstatus WHERE updatetime >%s AND updatetime <%s " \
          "AND username=%s AND `status`= 'hidden_web'"
    cursor1.execute(sqlhidden, (start_time, endtime, username ))
    resulthidden = cursor1.fetchall()
    hidden = resulthidden[0][0]

    sqlhidden = "SELECT count(*) FROM userstatus WHERE updatetime >%s AND updatetime <%s " \
                "AND username=%s AND `status`= 'debug'"
    cursor1.execute(sqlhidden, (start_time, endtime, username))
    resultdebug = cursor1.fetchall()
    debug = resultdebug[0][0]

    sqlhidden = "SELECT count(*) FROM userstatus WHERE updatetime >%s AND updatetime <%s " \
                "AND username=%s AND `status`= 'command'"
    cursor1.execute(sqlhidden, (start_time, endtime, username))
    resultcommand = cursor1.fetchall()
    command = resultcommand[0][0]
    print(username, start_time, endtime)
    sql1 = "SELECT * FROM userstatus WHERE (`status` = 'get_web' OR `status` = 'leave_web') " \
           "AND username=%s AND updatetime >%s AND updatetime <%s ORDER BY `updatetime` ASC"
    cursor1.execute(sql1, (username, start_time, endtime))
    resultlg = cursor1.fetchall()
    totaltime = 0
    if(len(resultlg)>=2):
        leavetime = ''
        gettime = ''
        for row1 in resultlg:
            if(row1[2] == 'leave_web'):
                leavetime = row1[4]
                # print(row1[4])
            elif(row1[2] == 'get_web'):
                gettime = row1[4]
                if(leavetime != ''):
                    if(gettime > leavetime):
                        # print(leavetime, gettime)
                        time_1_struct = datetime.strptime(leavetime, "%Y-%m-%d %H:%M:%S")
                        time_2_struct = datetime.strptime(gettime, "%Y-%m-%d %H:%M:%S")
                        seconds = (time_2_struct - time_1_struct).seconds
                        # print(seconds)
                        totaltime = totaltime + seconds
    else:
        totaltime = 0
    # totaltime = 0
    resultnum1 = resultnum1.append(
        {"用户名": username, "竞赛": cid, "最小化页面次数": hidden, "鼠标离开页面的时间": totaltime, "调试次数": debug, "终端输入次数": command}, ignore_index=True)
    resultnum1.to_excel(savefile, index=False)

    print(username, hidden, debug, command, totaltime)
    # break

