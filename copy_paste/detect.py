import MySQLdb

db1 = MySQLdb.connect("202.4.155.100", "root", "*", "*", charset='utf8')
db2 = MySQLdb.connect("202.4.155.100", "root", "*", "*", charset='utf8')

cursor1 = db1.cursor()
cursor2 = db2.cursor()

# sql = "SELECT * FROM contest WHERE title LIKE '%在线编程平台%' AND start_time > '2021-10-14 18:00:00' AND start_time < '2021-11-09 00:00:00'"
# sql = "SELECT * FROM contest WHERE title LIKE '%在线编程平台%' AND start_time > '2021-11-09 00:00:00' AND start_time < '2021-12-01 00:00:00'"
sql = "SELECT * FROM contest WHERE title LIKE '%在线编程平台%' AND start_time > '2021-12-01 00:00:00'"
cursor2.execute(sql)
results = cursor2.fetchall()
i = 0
for row in results:
    i = i+1
    print(i)
    break
    # contest_id = row[0]
    # starttime = row[2]
    # endtime = row[3]
    # # print(contest_id, starttime, endtime)
    # sql = "SELECT DISTINCT(username) FROM userstatus WHERE detail IS NOT NULL " \
    #       "AND status LIKE 'paste_vscode' " \
    #       "AND updatetime >%s AND updatetime < %s"
    # cursor1.execute(sql, (starttime, endtime))
    # resultuser = cursor1.fetchall()
    # j=0
    # for row1 in resultuser:
    #     j = j+1
    #     username = row1[0]
    #
    #     # 粘贴内容
    #     sql1 = "SELECT * FROM userstatus WHERE detail IS NOT NULL " \
    #           "AND username = %s " \
    #           "AND status LIKE 'paste_vscode' " \
    #           "AND updatetime > %s AND updatetime < %s"
    #     cursor1.execute(sql1, (username, starttime, endtime))
    #     resultpaste = cursor1.fetchall()
    #     k=0
    #     for row2 in resultpaste:
    #         k = k+1
    #         paste_vscode = row2[3]
    #         updatetime = row2[4]
    #         iscopy = 1000
    #         iscut = 1000
    #         # 复制内容
    #         sql2 = "SELECT * FROM userstatus WHERE detail IS NOT NULL " \
    #                "AND username = %s " \
    #                "AND status LIKE 'copy_vscode' " \
    #                "AND updatetime > %s AND updatetime < %s"
    #         cursor1.execute(sql2, (username, starttime, endtime))
    #         resultcopy = cursor1.fetchall()
    #         for row3 in resultcopy:
    #             copy_vscode = row3[3]
    #             if paste_vscode == copy_vscode:
    #                 iscopy = 0  # 没有外部粘贴
    #                 break
    #         if iscopy != 0:
    #             iscopy = 1  # 没有复制匹配项
    #
    #         # 剪切内容
    #         sql3 = "SELECT * FROM userstatus WHERE detail IS NOT NULL " \
    #                "AND username = %s " \
    #                "AND status LIKE 'cut_vscode' " \
    #                "AND updatetime > %s AND updatetime < %s"
    #         cursor1.execute(sql3, (username, starttime, endtime))
    #         resultcut = cursor1.fetchall()
    #         for row4 in resultcut:
    #             cut_vscode = row4[3]
    #             if paste_vscode == cut_vscode:
    #                 iscut = 0  # 没有外部粘贴
    #                 break
    #         if iscut != 0:
    #             iscut = 1  # 没有剪切匹配项
    #
    #         if iscopy == 1 and iscut == 1:
    #             copy = 1  # 存在外部粘贴
    #         else:
    #             copy = 0  # 不存在外部粘贴
    #
    #         if copy == 1:
    #             sql = "SELECT * FROM collectinfo WHERE username = %s " \
    #                   "AND modifytime> %s AND modifytime < %s AND modifycode != '' " \
    #                   "ORDER BY modifytime desc LIMIT 5"
    #             cursor1.execute(sql, (username, starttime, updatetime))
    #             resultpaste_pre = cursor1.fetchall()
    #
    #             sql = "SELECT * FROM collectinfo WHERE username = %s " \
    #                   "AND modifytime>= %s AND modifytime < %s AND modifycode != ''" \
    #                   "ORDER BY modifytime ASC LIMIT 5"
    #             cursor1.execute(sql, (username, updatetime, endtime))
    #             resultpaste_after = cursor1.fetchall()
    #
    #             if(len(resultpaste_pre) + len(resultpaste_after) >=5):
    #                 if(len(resultpaste_pre) == 0):
    #                     paste_pre1 = resultpaste_after[0][6]
    #                     paste_pre2 = resultpaste_after[1][6]
    #                     paste = resultpaste_after[2][6]
    #                     paste_after1 = resultpaste_after[3][6]
    #                     paste_after2 = resultpaste_after[4][6]
    #                     problem_id2 = resultpaste_after[0][9]
    #                 elif(len(resultpaste_pre) == 1):
    #                     paste_pre1 = resultpaste_pre[0][6]
    #                     paste_pre2 = resultpaste_after[0][6]
    #                     paste = resultpaste_after[1][6]
    #                     paste_after1 = resultpaste_after[2][6]
    #                     paste_after2 = resultpaste_after[3][6]
    #                     problem_id1 = resultpaste_pre[0][9]
    #                     problem_id2 = resultpaste_after[0][9]
    #                 elif(len(resultpaste_pre) >=2):
    #                     if(len(resultpaste_after) >= 3):
    #                         paste_pre1 = resultpaste_pre[1][6]
    #                         paste_pre2 = resultpaste_pre[0][6]
    #                         paste = resultpaste_after[0][6]
    #                         paste_after1 = resultpaste_after[1][6]
    #                         paste_after2 = resultpaste_after[2][6]
    #                         problem_id1 = resultpaste_pre[0][9]
    #                         problem_id2 = resultpaste_after[0][9]
    #                     elif(len(resultpaste_after) == 2):
    #                         paste_pre1 = resultpaste_pre[2][6]
    #                         paste_pre2 = resultpaste_pre[1][6]
    #                         paste = resultpaste_pre[0][6]
    #                         paste_after1 = resultpaste_after[0][6]
    #                         paste_after2 = resultpaste_after[1][6]
    #                         problem_id1 = resultpaste_pre[0][9]
    #                         problem_id2 = resultpaste_after[0][9]
    #                     elif (len(resultpaste_after) == 1):
    #                         paste_pre1 = resultpaste_pre[3][6]
    #                         paste_pre2 = resultpaste_pre[2][6]
    #                         paste = resultpaste_pre[1][6]
    #                         paste_after1 = resultpaste_pre[0][6]
    #                         paste_after2 = resultpaste_after[0][6]
    #                         problem_id1 = resultpaste_pre[0][9]
    #                         problem_id2 = resultpaste_after[0][9]
    #                     elif (len(resultpaste_after) == 0):
    #                         paste_pre1 = resultpaste_pre[4][6]
    #                         paste_pre2 = resultpaste_pre[3][6]
    #                         paste = resultpaste_pre[2][6]
    #                         paste_after1 = resultpaste_pre[1][6]
    #                         paste_after2 = resultpaste_pre[0][6]
    #                         problem_id1 = resultpaste_pre[0][9]
    #             elif(len(resultpaste_pre) + len(resultpaste_after) == 4):
    #                 if(len(resultpaste_pre) == 0):
    #                     paste_pre1 = resultpaste_after[0][6]
    #                     paste_pre2 = resultpaste_after[1][6]
    #                     paste = resultpaste_after[2][6]
    #                     paste_after1 = resultpaste_after[3][6]
    #                     paste_after2 = 'THE END'
    #                     problem_id2 = resultpaste_after[0][9]
    #                 elif(len(resultpaste_pre) == 1):
    #                     paste_pre1 = resultpaste_pre[0][6]
    #                     paste_pre2 = resultpaste_after[0][6]
    #                     paste = resultpaste_after[1][6]
    #                     paste_after1 = resultpaste_after[2][6]
    #                     paste_after2 = 'THE END'
    #                     problem_id2 = resultpaste_after[0][9]
    #                 elif (len(resultpaste_pre) == 2):
    #                     paste_pre1 = resultpaste_pre[1][6]
    #                     paste_pre2 = resultpaste_pre[0][6]
    #                     paste = resultpaste_after[0][6]
    #                     paste_after1 = resultpaste_after[1][6]
    #                     paste_after2 = 'THE END'
    #                     problem_id2 = resultpaste_after[0][9]
    #                 elif (len(resultpaste_pre) == 3):
    #                     paste_pre1 = resultpaste_pre[2][6]
    #                     paste_pre2 = resultpaste_pre[1][6]
    #                     paste = resultpaste_pre[0][6]
    #                     paste_after1 = resultpaste_after[0][6]
    #                     paste_after2 = 'THE END'
    #                     problem_id2 = resultpaste_after[0][9]
    #                 elif (len(resultpaste_pre) == 4):
    #                     paste_pre1 = resultpaste_pre[3][6]
    #                     paste_pre2 = resultpaste_pre[2][6]
    #                     paste = resultpaste_pre[1][6]
    #                     paste_after1 = resultpaste_pre[0][6]
    #                     paste_after2 = 'THE END'
    #                     problem_id2 = resultpaste_pre[0][9]
    #             elif (len(resultpaste_pre) + len(resultpaste_after) == 3):
    #                 if (len(resultpaste_pre) == 0):
    #                     paste_pre1 = resultpaste_after[0][6]
    #                     paste_pre2 = resultpaste_after[1][6]
    #                     paste = resultpaste_after[2][6]
    #                     paste_after1 = 'THE END'
    #                     paste_after2 = 'THE END'
    #                     problem_id2 = resultpaste_after[0][9]
    #                 elif (len(resultpaste_pre) == 1):
    #                     paste_pre1 = resultpaste_pre[0][6]
    #                     paste_pre2 = resultpaste_after[0][6]
    #                     paste = resultpaste_after[1][6]
    #                     paste_after1 = 'THE END'
    #                     paste_after2 = 'THE END'
    #                     problem_id2 = resultpaste_after[0][9]
    #                 elif (len(resultpaste_pre) == 2):
    #                     paste_pre1 = resultpaste_pre[1][6]
    #                     paste_pre2 = resultpaste_pre[0][6]
    #                     paste = resultpaste_after[0][6]
    #                     paste_after1 = 'THE END'
    #                     paste_after2 = 'THE END'
    #                     problem_id2 = resultpaste_after[0][9]
    #                 elif (len(resultpaste_pre) == 3):
    #                     paste_pre1 = resultpaste_pre[2][6]
    #                     paste_pre2 = resultpaste_pre[1][6]
    #                     paste = resultpaste_pre[0][6]
    #                     paste_after1 = 'THE END'
    #                     paste_after2 = 'THE END'
    #                     problem_id2 = resultpaste_pre[0][9]
    #             elif (len(resultpaste_pre) + len(resultpaste_after) == 2):
    #                 if (len(resultpaste_pre) == 0):
    #                     paste_pre1 = resultpaste_after[0][6]
    #                     paste_pre2 = resultpaste_after[1][6]
    #                     paste = 'THE END'
    #                     paste_after1 = 'THE END'
    #                     paste_after2 = 'THE END'
    #                     problem_id2 = resultpaste_after[0][9]
    #                 elif (len(resultpaste_pre) == 1):
    #                     paste_pre1 = resultpaste_pre[0][6]
    #                     paste_pre2 = resultpaste_after[0][6]
    #                     paste = 'THE END'
    #                     paste_after1 = 'THE END'
    #                     paste_after2 = 'THE END'
    #                     problem_id2 = resultpaste_after[0][9]
    #                 elif (len(resultpaste_pre) == 2):
    #                     paste_pre1 = resultpaste_pre[1][6]
    #                     paste_pre2 = resultpaste_pre[0][6]
    #                     paste = 'THE END'
    #                     paste_after1 = 'THE END'
    #                     paste_after2 = 'THE END'
    #                     problem_id2 = resultpaste_pre[0][9]
    #             elif (len(resultpaste_pre) + len(resultpaste_after) == 1):
    #                 if (len(resultpaste_pre) == 0):
    #                     paste_pre1 = resultpaste_after[0][6]
    #                     paste_pre2 = 'THE END'
    #                     paste = 'THE END'
    #                     paste_after1 = 'THE END'
    #                     paste_after2 = 'THE END'
    #                     problem_id2 = resultpaste_after[0][9]
    #                 elif (len(resultpaste_pre) == 1):
    #                     paste_pre1 = resultpaste_pre[0][6]
    #                     paste_pre2 = 'THE END'
    #                     paste = 'THE END'
    #                     paste_after1 = 'THE END'
    #                     paste_after2 = 'THE END'
    #                     problem_id2 = resultpaste_pre[0][9]
    #             elif (len(resultpaste_pre) + len(resultpaste_after) == 0):
    #                 paste_pre1 = 'THE END'
    #                 paste_pre2 = 'THE END'
    #                 paste = 'THE END'
    #                 paste_after1 = 'THE END'
    #                 paste_after2 = 'THE END'
    #                 problem_id2 = 'no'
    #
    #             print("resultpaste_pre:", len(resultpaste_pre), "  resultpaste_after:", len(resultpaste_after))
    #
    #             if(problem_id1 == 'no'):
    #                 problem_id = problem_id2
    #             elif (problem_id2 == 'no'):
    #                 problem_id = problem_id1
    #             else:
    #                 if(problem_id1 == problem_id2):
    #                     problem_id = problem_id1
    #                 else:
    #                     problem_id = problem_id2
    #         elif(copy == 0):
    #             problem_id = 'no'
    #             paste_pre1 = 'empty'
    #             paste_pre2 = 'empty'
    #             paste = 'empty'
    #             paste_after1 = 'empty'
    #             paste_after2 = 'empty'
    #
    #         sql = "INSERT INTO userstatus_detail (username,contest_id,problem_id," \
    #               "status,detail,updatetime,copy_label," \
    #               "paste_pre1,paste_pre2,paste,paste_after1,paste_after2) " \
    #               "VALUES (%s,%s,%s,'paste_vscode',%s,%s,%s,%s,%s,%s,%s,%s)"
    #         cursor1.execute(sql, (username, contest_id, problem_id, paste_vscode, updatetime, copy,
    #                               paste_pre1, paste_pre2, paste, paste_after1, paste_after2))
    #         db1.commit()
    #         print(k, "/", len(resultpaste), "  ", j, "/", len(resultuser), "  ", i, "/", len(results))

db1.close()
db2.close()

