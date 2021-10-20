import requests
import json
x=requests.get("http://saral.navgurukul.org/api/courses")
a=x.json()
c=1
list=[]
for i in a["availableCourses"]:
    print("--------------------")
    print(c,i["name"],i['id'])
    list.append(i["id"])
    c+=1
num=int(input("enter the courese:::____"))
a=list[num-1]
m=requests.get("http://saral.navgurukul.org/api/courses/"+str(a)+"/exercises")
data2=m.json()
print("          ")
print("****************")
print("          ")
print(data2)
print("           ")
print("******😊Thank You😊******")
print("           ")


