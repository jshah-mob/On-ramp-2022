l1=["1","2"]
l2=[3,4]
print(l1.extend(l2))
print(l1)
print(l2.sort())
print(sorted(l2))
a=[1,2,3,4,5,6,]
#same list
b=a
a.append(7)
print(b)
#create nnew list
c=[i for  i in a]
a.append(8)
print(a)
print(c)	

#enumrate -return a list with index of its elements	
parts=["computer", "monitor", "mouse", "keyboard", "hdmi"]
for num,part in enumerate(parts):
	print(num+1,part)



#sorting
names=["gibb","gia", "Eric","graham","Tinm"]
names.sort(key=str.casefold)
print(names)

#between a range
l=[45,3,4,101,102,350,360]
for i,value in enumerate(l):
    if  value >200 or value<100:
        l[i]=""
        print(l)
print(l.remove("",))
print(l)
