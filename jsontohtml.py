from json2table import *
import json




data = open('free.json','r')
jsonFile = data.read()
foo = json.loads(jsonFile)
build_dir = "LEFT_TO_RIGHT"
table_attr = {"style" : "width:100%", "class" : "table table-striped","border": "1px solid black"}
html = convert(foo, build_direction=build_dir,table_attributes=table_attr)

with open("free.html", "w") as ht:
    ht.write(html)

data = open('paid.json','r')
jsonFile = data.read()
foo = json.loads(jsonFile)
build_dir = "LEFT_TO_RIGHT"
table_attr = {"style" : "width:100%", "class" : "table table-striped","border": "1px solid black"}
html = convert(foo, build_direction=build_dir,table_attributes=table_attr)

with open("paid.html", "w") as ht:
    ht.write(html)