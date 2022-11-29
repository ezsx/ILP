#!/usr/bin/env python3
import cgi
from LR_15 import execute_sql

form = cgi.FieldStorage()
index_table_to_show = int(form['tableselect'].value)
sql_red = form['sql_red'].value
sql_red = sql_red.split(',')

match index_table_to_show:
    case 1:
        sql = f"update REGIONS set REGIONS.NAME = {sql_red[1]}, REGIONS.TIME = {sql_red[2]} where REGIONS.ID = {sql_red[0]}"
    case 2:
        sql = f"update CLIENTS set CLIENTS.FIO = {sql_red[1]}, CLIENTS.ADRESS = {sql_red[2]}, CLIENTS.REGIONS_ID={sql_red[3]} where CLIENTS.ID = {sql_red[0]}"
    case 3:
        sql = f"update ORDERS set ORDERS.AMOUNT = {sql_red[1]}, ORDERS.CLIENTS_ID = {sql_red[2]} where ORDERS.ID = {sql_red[0]}"
    case 4:
        sql = f"update GOODS set GOODS.PRICE = {sql_red[1]}, GOODS.WEIGHT = {sql_red[2]} where GOODS.ID = {sql_red[0]}"
    case 5:
        sql = f"update WAREHOUSE set WAREHOUSE.ADDRESS = {sql_red[1]}, WAREHOUSE.TIME = {sql_red[2]} where WAREHOUSE.ID = {sql_red[0]}"
    case _:
        sql = None
if sql is not None:

    print("""<h1><>Succes</font></h1>""")
    smth = execute_sql(sql, True)
else:
    print("""<h1><>Error</font></h1>""")
