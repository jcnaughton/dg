#!/usr/bin/python3

import sqlite3

connection = sqlite3.connect("cabinets.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()
# cursor.execute("CREATE TABLE worklist ( prime INTEGER, room TEXT, rack TEXT, category INTEGER, dt TEXT)")
# cursor.execute("INSERT INTO worklist (prime,category,dt)VALUES (100010, 0, CURRENT_TIMESTAMP)")
# cursor.execute("INSERT INTO worklist (prime,category,dt)VALUES (100011, 0, CURRENT_TIMESTAMP)")
# cursor.execute("INSERT INTO worklist (prime,category,dt)VALUES (100012, 0, CURRENT_TIMESTAMP)")
cursor.execute("UPDATE worklist SET category = 2 WHERE prime = 100010")
connection.commit()

columnList = ['reserved','received','in-room','in-place','powered']

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>egg</title>")
print ("</head>")
print ("<body>")


print("<table border='1'>")
print("<tr>")
for col in columnList:
    print("<th>" + str(col) + "</th>")
print("</tr>")

cursor.execute("SELECT * FROM worklist")
for rack in cursor.fetchall():
    rackDict= dict(rack)
    print("<tr>")
    for col in range(len(columnList)):
        if rackDict['category'] == col:
            print("<td>" + str(rackDict['prime']) + "<br / >" + rackDict['dt'] + "</td>")
        else:
            print("<td>&nbsp;</td>")
    print("</tr>")
