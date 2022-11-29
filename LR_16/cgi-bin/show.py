#!/usr/bin/env python3
import cgi
import jinja2
from LR_15 import execute_sql
import sys

form = cgi.FieldStorage()
index_table_to_show = int(form['tableselect'].value)
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

sql = f"SELECT * FROM {table_to_show}"

enviroment = jinja2.Environment(loader=jinja2.FileSystemLoader('templates/'))

template = enviroment.get_template('table.html')

contex = {'table': ''}
all = execute_sql(sql, False)
contex['table'] = all
content = template.render(contex)
print(content.replace('}', ''))
