import MySQLdb
import time

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec
second = sleeptime(0,5,0)

first_id = 651337

while True:
    print("----"*10)
    print("Start : %s" % time.ctime())

    db1 = MySQLdb.connect("202.4.155.100", "root", "buctacm4726", "record", charset='utf8')
    db2 = MySQLdb.connect("202.4.155.100", "root", "buctacm4726", "jol", charset='utf8')
    cursor1 = db1.cursor()
    cursor2 = db2.cursor()

    sql = "SELECT * FROM userstatus WHERE id > %s ORDER BY id DESC LIMIT 1"
    cursor1.execute(sql, (first_id, ))
    resultlastid = cursor1.fetchall()
    if(len(resultlastid)>0):
        last_id = resultlastid[0][0]

        i = 0
        sql = "SELECT * FROM userstatus WHERE detail IS NOT NULL " \
              "AND status LIKE 'paste_vscode' " \
              "AND id >= %s AND id < %s ORDER BY id ASC"
        cursor1.execute(sql, (first_id, last_id))
        resultall = cursor1.fetchall()
        if(len(resultall)>0):
            for row in resultall:
                i = i + 1
                id = row[0]
                username = row[1]
                paste_vscode = row[3]  # 粘贴内容
                updatetime = row[4]

                sql1 = "SELECT * FROM collectinfo WHERE username = %s AND  updatetime >= %s ORDER BY updatetime LIMIT 1"
                cursor1.execute(sql1, (username, updatetime))
                resultcontest = cursor1.fetchall()
                contest_id = resultcontest[0][8]

                sql1 = "SELECT * FROM contest WHERE contest_id = %s "
                cursor2.execute(sql1, (contest_id,))
                resultcontesttime = cursor2.fetchall()
                if(len(resultcontesttime)>0):
                    sqls = ""
                    start_time = resultcontesttime[0][2]
                    end_time = resultcontesttime[0][3]
                    # print(start_time, end_time)

                    # sql1 = "SELECT * FROM contest WHERE title LIKE '%%在线编程平台%%' AND start_time<%s AND end_time > %s ORDER BY contest_id ASC"
                    # cursor2.execute(sql1, (updatetime, updatetime))
                    # resultcontest = cursor2.fetchall()
                    # if(len(resultcontest)>0):
                    #     if(len(resultcontest) == 1):
                    #         contest_id = resultcontest[0][0]
                    #         start_time = resultcontest[0][2]
                    #         end_time = resultcontest[0][3]
                    #     else:
                    #         for rowcid in resultcontest:
                    #             sqlid = "SELECT * FROM privilege WHERE rightstr = %s AND user_id = %s "
                    #             cursor2.execute(sqlid, ('c'+str(rowcid[0]), username))
                    #             resultid = cursor2.fetchall()
                    #             if(len(resultid) > 0):
                    #                 contest_id = rowcid[0]
                    #                 start_time = rowcid[2]
                    #                 end_time = rowcid[3]
                    #             else:
                    #                 contest_id = rowcid[0]
                    #                 start_time = rowcid[2]
                    #                 end_time = rowcid[3]

                    iscopy = 1000
                    iscut = 1000

                    # 复制内容
                    sql2 = "SELECT * FROM userstatus WHERE detail IS NOT NULL " \
                           "AND username = %s " \
                           "AND status LIKE 'copy_vscode' " \
                           "AND updatetime > %s AND updatetime < %s"
                    cursor1.execute(sql2, (username, start_time, updatetime))
                    resultcopy = cursor1.fetchall()
                    for row1 in resultcopy:
                        copy_vscode = row1[3]
                        if paste_vscode == copy_vscode:
                            iscopy = 0  # 没有外部粘贴
                            break
                    if iscopy != 0:
                        iscopy = 1  # 没有复制匹配项

                    # 剪切内容
                    sql3 = "SELECT * FROM userstatus WHERE detail IS NOT NULL " \
                           "AND username = %s " \
                           "AND status LIKE 'cut_vscode' " \
                           "AND updatetime > %s AND updatetime < %s"
                    cursor1.execute(sql3, (username, start_time, updatetime))
                    resultcut = cursor1.fetchall()
                    for row2 in resultcut:
                        cut_vscode = row2[3]
                        if paste_vscode == cut_vscode:
                            iscut = 0  # 没有外部粘贴
                            break
                    if iscut != 0:
                        iscut = 1  # 没有剪切匹配项

                    if iscopy == 1 and iscut == 1:
                        copy = 1  # 存在外部粘贴
                    else:
                        copy = 0  # 不存在外部粘贴

                    if copy == 1:
                        sql = "SELECT * FROM collectinfo WHERE username = %s " \
                              "AND modifytime> %s AND modifytime < %s AND modifycode != '' " \
                              "ORDER BY modifytime desc LIMIT 5"
                        cursor1.execute(sql, (username, start_time, updatetime))
                        resultpaste_pre = cursor1.fetchall()

                        sql = "SELECT * FROM collectinfo WHERE username = %s " \
                              "AND modifytime>= %s AND modifytime < %s AND modifycode != ''" \
                              "ORDER BY modifytime ASC LIMIT 5"
                        cursor1.execute(sql, (username, updatetime, end_time))
                        resultpaste_after = cursor1.fetchall()

                        if(len(resultpaste_pre) + len(resultpaste_after) >=5):
                            if(len(resultpaste_pre) == 0):
                                paste_pre1 = resultpaste_after[0][6]
                                paste_pre2 = resultpaste_after[1][6]
                                paste = resultpaste_after[2][6]
                                paste_after1 = resultpaste_after[3][6]
                                paste_after2 = resultpaste_after[4][6]
                                problem_id2 = resultpaste_after[0][9]
                            elif(len(resultpaste_pre) == 1):
                                paste_pre1 = resultpaste_pre[0][6]
                                paste_pre2 = resultpaste_after[0][6]
                                paste = resultpaste_after[1][6]
                                paste_after1 = resultpaste_after[2][6]
                                paste_after2 = resultpaste_after[3][6]
                                problem_id1 = resultpaste_pre[0][9]
                                problem_id2 = resultpaste_after[0][9]
                            elif(len(resultpaste_pre) >=2):
                                if(len(resultpaste_after) >= 3):
                                    paste_pre1 = resultpaste_pre[1][6]
                                    paste_pre2 = resultpaste_pre[0][6]
                                    paste = resultpaste_after[0][6]
                                    paste_after1 = resultpaste_after[1][6]
                                    paste_after2 = resultpaste_after[2][6]
                                    problem_id1 = resultpaste_pre[0][9]
                                    problem_id2 = resultpaste_after[0][9]
                                elif(len(resultpaste_after) == 2):
                                    paste_pre1 = resultpaste_pre[2][6]
                                    paste_pre2 = resultpaste_pre[1][6]
                                    paste = resultpaste_pre[0][6]
                                    paste_after1 = resultpaste_after[0][6]
                                    paste_after2 = resultpaste_after[1][6]
                                    problem_id1 = resultpaste_pre[0][9]
                                    problem_id2 = resultpaste_after[0][9]
                                elif (len(resultpaste_after) == 1):
                                    paste_pre1 = resultpaste_pre[3][6]
                                    paste_pre2 = resultpaste_pre[2][6]
                                    paste = resultpaste_pre[1][6]
                                    paste_after1 = resultpaste_pre[0][6]
                                    paste_after2 = resultpaste_after[0][6]
                                    problem_id1 = resultpaste_pre[0][9]
                                    problem_id2 = resultpaste_after[0][9]
                                elif (len(resultpaste_after) == 0):
                                    paste_pre1 = resultpaste_pre[4][6]
                                    paste_pre2 = resultpaste_pre[3][6]
                                    paste = resultpaste_pre[2][6]
                                    paste_after1 = resultpaste_pre[1][6]
                                    paste_after2 = resultpaste_pre[0][6]
                                    problem_id1 = resultpaste_pre[0][9]
                        elif(len(resultpaste_pre) + len(resultpaste_after) == 4):
                            if(len(resultpaste_pre) == 0):
                                paste_pre1 = resultpaste_after[0][6]
                                paste_pre2 = resultpaste_after[1][6]
                                paste = resultpaste_after[2][6]
                                paste_after1 = resultpaste_after[3][6]
                                paste_after2 = 'THE END'
                                problem_id2 = resultpaste_after[0][9]
                            elif(len(resultpaste_pre) == 1):
                                paste_pre1 = resultpaste_pre[0][6]
                                paste_pre2 = resultpaste_after[0][6]
                                paste = resultpaste_after[1][6]
                                paste_after1 = resultpaste_after[2][6]
                                paste_after2 = 'THE END'
                                problem_id2 = resultpaste_after[0][9]
                            elif (len(resultpaste_pre) == 2):
                                paste_pre1 = resultpaste_pre[1][6]
                                paste_pre2 = resultpaste_pre[0][6]
                                paste = resultpaste_after[0][6]
                                paste_after1 = resultpaste_after[1][6]
                                paste_after2 = 'THE END'
                                problem_id2 = resultpaste_after[0][9]
                            elif (len(resultpaste_pre) == 3):
                                paste_pre1 = resultpaste_pre[2][6]
                                paste_pre2 = resultpaste_pre[1][6]
                                paste = resultpaste_pre[0][6]
                                paste_after1 = resultpaste_after[0][6]
                                paste_after2 = 'THE END'
                                problem_id2 = resultpaste_after[0][9]
                            elif (len(resultpaste_pre) == 4):
                                paste_pre1 = resultpaste_pre[3][6]
                                paste_pre2 = resultpaste_pre[2][6]
                                paste = resultpaste_pre[1][6]
                                paste_after1 = resultpaste_pre[0][6]
                                paste_after2 = 'THE END'
                                problem_id2 = resultpaste_pre[0][9]
                        elif (len(resultpaste_pre) + len(resultpaste_after) == 3):
                            if (len(resultpaste_pre) == 0):
                                paste_pre1 = resultpaste_after[0][6]
                                paste_pre2 = resultpaste_after[1][6]
                                paste = resultpaste_after[2][6]
                                paste_after1 = 'THE END'
                                paste_after2 = 'THE END'
                                problem_id2 = resultpaste_after[0][9]
                            elif (len(resultpaste_pre) == 1):
                                paste_pre1 = resultpaste_pre[0][6]
                                paste_pre2 = resultpaste_after[0][6]
                                paste = resultpaste_after[1][6]
                                paste_after1 = 'THE END'
                                paste_after2 = 'THE END'
                                problem_id2 = resultpaste_after[0][9]
                            elif (len(resultpaste_pre) == 2):
                                paste_pre1 = resultpaste_pre[1][6]
                                paste_pre2 = resultpaste_pre[0][6]
                                paste = resultpaste_after[0][6]
                                paste_after1 = 'THE END'
                                paste_after2 = 'THE END'
                                problem_id2 = resultpaste_after[0][9]
                            elif (len(resultpaste_pre) == 3):
                                paste_pre1 = resultpaste_pre[2][6]
                                paste_pre2 = resultpaste_pre[1][6]
                                paste = resultpaste_pre[0][6]
                                paste_after1 = 'THE END'
                                paste_after2 = 'THE END'
                                problem_id2 = resultpaste_pre[0][9]
                        elif (len(resultpaste_pre) + len(resultpaste_after) == 2):
                            if (len(resultpaste_pre) == 0):
                                paste_pre1 = resultpaste_after[0][6]
                                paste_pre2 = resultpaste_after[1][6]
                                paste = 'THE END'
                                paste_after1 = 'THE END'
                                paste_after2 = 'THE END'
                                problem_id2 = resultpaste_after[0][9]
                            elif (len(resultpaste_pre) == 1):
                                paste_pre1 = resultpaste_pre[0][6]
                                paste_pre2 = resultpaste_after[0][6]
                                paste = 'THE END'
                                paste_after1 = 'THE END'
                                paste_after2 = 'THE END'
                                problem_id2 = resultpaste_after[0][9]
                            elif (len(resultpaste_pre) == 2):
                                paste_pre1 = resultpaste_pre[1][6]
                                paste_pre2 = resultpaste_pre[0][6]
                                paste = 'THE END'
                                paste_after1 = 'THE END'
                                paste_after2 = 'THE END'
                                problem_id2 = resultpaste_pre[0][9]
                        elif (len(resultpaste_pre) + len(resultpaste_after) == 1):
                            if (len(resultpaste_pre) == 0):
                                paste_pre1 = resultpaste_after[0][6]
                                paste_pre2 = 'THE END'
                                paste = 'THE END'
                                paste_after1 = 'THE END'
                                paste_after2 = 'THE END'
                                problem_id2 = resultpaste_after[0][9]
                            elif (len(resultpaste_pre) == 1):
                                paste_pre1 = resultpaste_pre[0][6]
                                paste_pre2 = 'THE END'
                                paste = 'THE END'
                                paste_after1 = 'THE END'
                                paste_after2 = 'THE END'
                                problem_id2 = resultpaste_pre[0][9]
                        elif (len(resultpaste_pre) + len(resultpaste_after) == 0):
                            paste_pre1 = 'THE END'
                            paste_pre2 = 'THE END'
                            paste = 'THE END'
                            paste_after1 = 'THE END'
                            paste_after2 = 'THE END'
                            problem_id2 = 'no'

                        print("resultpaste_pre:", len(resultpaste_pre), "  resultpaste_after:", len(resultpaste_after))

                        if(problem_id1 == 'no'):
                            problem_id = problem_id2
                        elif (problem_id2 == 'no'):
                            problem_id = problem_id1
                        else:
                            if(problem_id1 == problem_id2):
                                problem_id = problem_id1
                            else:
                                problem_id = problem_id2
                    elif(copy == 0):
                        problem_id = 'no'
                        paste_pre1 = 'empty'
                        paste_pre2 = 'empty'
                        paste = 'empty'
                        paste_after1 = 'empty'
                        paste_after2 = 'empty'

                    # sql = "INSERT INTO userstatus_detail (username,contest_id,problem_id," \
                    #       "status,detail,updatetime,copy_label," \
                    #       "paste_pre1,paste_pre2,paste,paste_after1,paste_after2) " \
                    #       "VALUES (%s,%s,%s,'paste_vscode',%s,%s,%s,%s,%s,%s,%s,%s)"
                    # cursor1.execute(sql, (username, contest_id, problem_id, paste_vscode, updatetime, copy,
                    #                       paste_pre1, paste_pre2, paste, paste_after1, paste_after2))
                    # db1.commit()

                    print(id, username, contest_id, problem_id, updatetime, "       ", "copylabel:", copy, "       ", i, "/", len(resultall))


        first_id = last_id
        print("End : %s" % time.ctime())
        print("----" * 10)
        time.sleep(second)
    else:
        time.sleep(second)

    db1.close()
    db2.close()

