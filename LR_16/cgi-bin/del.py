#!/usr/bin/env python3
import cgi
from LR_15 import execute_sql

form = cgi.FieldStorage()
index_table_to_show = form['tableselect']
index_delete = form['sql_del']

index_table_to_show = int(index_table_to_show.value)
match index_table_to_show:
    case 1:
        table_to_show = 'regions'
    case 2:
        table_to_show = 'clients'
    case 3:
        table_to_show = 'orders'
    case 4:
        table_to_show = 'goods'
    case 5:
        table_to_show = 'warehouse'
    case _:
        table_to_show = 'regions'

sql = f"DELETE FROM {table_to_show} WHERE id = {index_delete.value}"

if sql is not None:

    print("""<h1><>Succes</font></h1>""")
    smth = execute_sql(sql, True)
else:
    print("""<h1><>Error</font></h1>""")
