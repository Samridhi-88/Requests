import requests
import json
from pprint import pprint

x=requests.get("http://saral.navgurukul.org/api/courses")
data=x.json()
def option(select,var1,slug,data1):
    var_1=var1
    while True:
        print("*-*-*-*-*-*-*-*-*-*-*-*")
        option=input("inter the option::- UP,NEXT,EXIT,BACK")
        if option=="up":
            pprint(var_1)
            var_1=var1-1
            req=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+str(slug[var_1-1]))
            request=req.json()
            print("****************",request["content"])
            pprint(var_1)
        elif option=="next":
            var_1=var_1+1
            req2=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+str(slug[var_1-1]))
            request1=req2.json()
            print("****************",request1["content"])
            pprint(var_1)
        elif option=="back":
            c=1
            for dictnuary in data1["data"]:
                print(c,dictnuary["name"])
                c+=1
        else:
            break
def courses():
    index=0
    for i in data["availableCourses"]:
        print(index+1,i["name"],i["id"])
        print("--------------------")
        index+=1
    for cource in data["availableCourses"]:
        course=int(input("enter your index of course= "))
        select=data["availableCourses"][course-1]["id"]
        var1=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercises")
        data1=var1.json()
        c=1
        slug=[]
        for dic_data in data1["data"]:
            print(c,dic_data["slug"])
            print("*-**-**-**-*")
            slug.append(dic_data["slug"])
            c+=1
        var4=int(input("selected content slug ::"))
        var3=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+str(slug[var4-1]))
        data4=var3.json()
        print(data4["content"])
        option(select,var4,slug,data1)
courses()