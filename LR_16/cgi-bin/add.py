#!/usr/bin/env python3
import cgi
from LR_15 import execute_sql

form = cgi.FieldStorage()
index_table_to_show = int(form['tableselect'].value)
sql_add = form['sql_add'].value
sql_add = sql_add.split(',')

match index_table_to_show:
    case 1:
        sql = f"insert into regions (id, name, TIME) values ({sql_add[0]},{sql_add[1]}, {sql_add[2]})"
    case 2:
        sql = f"insert into clients (id,FIO, ADRESS,REGIONS_ID) values ({sql_add[0]},{sql_add[1]},{sql_add[2]}, {sql_add[3]})"
    case 3:
        sql = f"insert into orders (id,AMOUNT,CLIENTS_ID) values ({sql_add[0]},{sql_add[1]},{sql_add[2]})"
    case 4:
        sql = f"insert into goods (id,PRICE, WEIGHT) values ({sql_add[0]},{sql_add[1]},{sql_add[2]})"
    case 5:
        sql = f"insert into warehouse (id,ADDRESS, TIME) values ({sql_add[0]},{sql_add[1]},{sql_add[2]})"
    case _:
        sql = None
if sql is not None:

    print("""<h1><font color="lime">Succes</font></h1>""")
    smth = execute_sql(sql, True)
else:
    print("""<h1><font color="red">Error</font></h1>""")
