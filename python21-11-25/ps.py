#subset,superset
a={1,2,3}
b={1,2,3,4,5}
res=a.issubset(b)
res2=b.issubset(a)
res3=b.issuperset(a)
print(res)
print(res2)
print(res3)
#disjoint
a={1,2,3}
b={4,5,6}
res=a.isdisjoint(b)
print(res)
#dict
d={}
j=dict()
print(type(d))
print(type(j))
k={"name":"abhi","age":25}
k.update({"sub":"python"})   #by adding using update
k.pop("age")                 #by removing using pop
print(k)
print(len(k))
print(k["name"])
# print(k["age"])
# #
d={"abhi":{"office":7286879395,"home":7095622708}}
print(d["abhi"])
print(d["abhi"]["office"])
print(d["abhi"]["home"])
#aloows key values only imutable data types
# d={[10,20,30,]:"python"}
print(d)
d={(10,20,30):"python"}
print(d)
#without using update we can add
k={"name":"abhi"}
k["mobile"]=7286879395
k["salary"]=25000
print(k)

#using append and without apped
j=[10,20,30,40]
j.append(100)    #using append
j+=[100]         #without apped
print(j)
print(j)
#school records store
school=[
    {"name":"abhi",'age':15,"pin":101,"class":9},
    {"name":"niki",'age':15,"pin":102,"class":9},
    {"name":"ajay",'age':14,"pin":103,"class":8},
    {"name":"sweety",'age':13,"pin":104,"class":7},
    {"name":"joshu",'age':12,"pin":105,"class":6}
]
# print(school[0])
# print(school[4])
n=eval(input("Enter pin/name :"))   #using eval any data type will be print
for x in school:
    if x["pin"]==n or x["name"]==n:
        for a,b in x.items():
             print(a,"==",b)
             print(a)
#keys values both :items
d= {"name":"abhi",'age':15,"pin":101,"class":9}
for x in d.items():

    print(x)
#both keys and values in dict
j={"name":"niki",'age':15,"pin":102,"class":9}
for k,v in d.items():
      print(k ,"==" ,v)

#
n=int(input("no/of students :"))
l=[]
for x in range(n):
      d={} #{"name":"abhi"}
      d["name"]=input("Enter student name :")  #"abhi"
      d["pin"]=int(input("Enter pin number :")) #2002
      d["age"]=int(input("Enter std age :"))   # 16
      l.append(d)
print(l)

# by using popitem remove last item in a dict
j={"a":10,"b":20,"c":30}
j.pop("b")
j.popitem()
print(j)

#to cahnge positions of key and values
j={"a":10,"b":20,"c":30}   #(10:"a",20:"b",30:"c")
tem={}
for a,b in j.items():
      tem[b]=a
      print(tem)
      
      


