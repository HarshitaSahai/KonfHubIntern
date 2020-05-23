import json 
  
import pprint
# the file to be converted to  
# json format 
filename = 'jsontext.txt'
  
# dictionary where the lines from 
# text will be stored 
dict1 = {} 
  
# creating dictionary 
with open(filename) as fh: 
  
    for line in fh: 
  
        # reads each line and trims of extra the spaces  
        # and gives only the valid words 
        command, description = line.strip().split(None, 1) 
  
        dict1[command] = description.strip() 
  
# creating json file 
# the JSON file is named as test1 
out_file = open("pretty11.json", "w") 
json.dump(dict1, out_file )
out_file.close() 

# Opening json file and divding the data into free and paid 
f = open('pretty.json') 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 

pfile  = open("paid.json", "w") # Creating file
# Finding paid 
for i in data['paid']: 
   json.dump(i, pfile) 

ffile = open("free.json","w") # Creating file
# Finding free 
for i in data['free']: 
    json.dump(i, ffile) 
  
# Closing file 
f.close() 