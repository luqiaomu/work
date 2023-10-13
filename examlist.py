l=[]
print(type(l))
hobbies=["唱","跳","rap"]
print("hobbies=",hobbies)

cxk=['我是练习时长','一坤','年的个人练习生','蔡徐坤','我喜欢']

print(hobbies[1:3])#访问

hobbies.append("篮球")
hobbies.append("music")#添加

print(hobbies)
cxk.extend(hobbies)
ikun=cxk
print(ikun)#合并


ikun[1]=2.5
print(ikun)#替换

ikun.insert(0,"大家好！")
print(ikun)#增添

#从头到尾，每隔两个元素访问
print(ikun[0:-1:3])
