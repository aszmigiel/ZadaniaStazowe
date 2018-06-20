import sys
import csv
import requests
import re

websites_filename=sys.argv[1]
filename_save=sys.argv[2]

pattern='(?i)(<a href=\"#\".+class=\".+(btn|button).+</a>)|(<button.*>.+<\/button>)|(<input type=\"(submit|reset|button)\".+>)'
sources = open(websites_filename)
save_file=open(filename_save,"w+")
writer = csv.writer(save_file)
writer.writerow(['address','number_of_buttons'])
for row in sources:
 response=requests.get("http://"+row)
 btncount= len( re.findall(pattern,response.text))
 writer.writerow([row,str(btncount)])
sources.close()
save_file.close()
 

 
