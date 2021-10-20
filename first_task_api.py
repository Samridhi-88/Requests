import requests
import json
x=requests.get("http://saral.navgurukul.org/api/courses")
a=x.json()
c=1
for i in a["availableCourses"]:
    print("---------------------")
    print(c,i["name"],i['id'])
    c+=1

