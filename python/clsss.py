# class Person():
#     x="class attribute"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def walk(self):
#         print("%s都已经%d岁了，因此要多运动" % (self.name,self.age))
#     def walk1(self,name='doudou',age=18):
#         print("%s都已经%d岁了，因此要多运动" % (name, age))
# print(Person.x)
# p=Person("zhangsan",30)
# print(p.name)
# print(p.x)
# print(p.walk())
# print(p.walk1())
# print(p.walk1('yuanyuan',17))


# class Student():
#     x="class attribute"
#     num="学号"
#     cla="班级"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def walk(self):
#         print("%s都已经%d岁了，因此要多运动" % (self.name,self.age))
#     def walk1(self,name='doudou',age=18):
#         print("%s都已经%d岁了，因此要多运动" % (name, age))
#     def exam(self):
#         print("%s参加考试" % self.name)
# stu=Student('doudou',18)
# print(stu.name)
# stu.walk()
# print(stu.age)
# stu.exam()




# class Father(): #声明Father类
#     def __init__(self,a,b): #初始化，绑定实例属性
#         self.a = a   #把a赋给self.a
#         self.b = b   #把b赋给self.b
#     def add(self):   #add方法
#         return self.a + self.b  #对a,b实现相加的操作
#     def sub(self):    #sub方法
#         return self.a - self.b     #对a,b实现相减的操作
# class Son(Father):   #声明Son类并继承Father类
#     def print_add(self): #print_add方法
#         print(Father.add())   #打印调用Father类的add方法返回的值
#     def sub(self):   #重写sub方法
#         return self.a * 2 - self.b  #实现a*2-b的操作
# son = Son(6,3) #实例化对象，传参为（6,3）
# print(son.sub())  #打印调用Son自身的sub方法返回的值
# print(son.add())   #打印调用Son继承Father类的add方法返回的值





# class dictclass():
#     def __init__(self,dct):  #初始化，绑定实例属性
#         self.dct = dct
#     def del_dict(self,key):  #删除某个key，并返回删除后的字典
#         self.dct.pop(key)
#         return self.dct
#     def get_dict(self,key):  #判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
#         return self.dct.get(key,"not found")
#     def get_key(self):       #返回键组成的列表：返回类型;(list)
#         return self.dct.keys()
#     def update_dict(self,dct1):  #合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
#         self.dct.update(dct1)
#         return self.dct.values()
# dct = {'1':2,'3':4,'7':8}
# dct1 = {'5':6}
# dct2 = dictclass(dct) #实例化对象
# print(dct2.dct)  #验证dct属性
# print(dct2.del_dict('1'))   #验证del_dict方法
# print(dct2.get_dict('7'))   #验证get_dict方法
# print(dct2.get_key())      #验证get_key方法
# print(dct2.update_dict(dct1))   #验证update_dict方法






# class Listinfo():
#     def __init__(self,lst):     #初始化，绑定实例属性
#         self.lst = lst
#     def add_key(self,keyname):  #列表元素添加
#         if isinstance(keyname,(str,int)):
#             self.lst.append(keyname)
#             return self.lst
#     def get_key(self,num):      #列表元素取值
#         if isinstance(num,int) and num >= -int(len(self.lst)) and num < int(len(self.lst)):
#             return self.lst[num]
#     def update_list(self,lst1):  #列表合并
#         if isinstance(lst1,list):
#             self.lst.extend(lst1)
#             return self.lst
#     def del_key(self):     #删除并且返回最后一个元素
#         return self.lst.pop()
# lst1 = [1,2,3,4,5,6,7]
# lst2 = [1,2,3]
# lst = Listinfo(lst1)  #实例化对象
# print(lst.lst)        #验证lst属性
# print(lst.add_key(8))  #验证add_key功能
# print(lst.add_key([1]))
# print(lst.get_key(1))  #验证get_key功能
# print(lst.get_key(10))
# print(lst.update_list(lst2))    #验证update_list功能
# print(lst.update_list(1))
# print(lst.del_key())     #验证del_key功能




# #重写init方法
# class Father():
#     def __index__(self,name):
#         self.name = name
# class Son(Father):
#     super(Son, self).__init__()



class Person():
    z = 1
    def __index__(self,name=0):
        self.name = name
    def walk(self):
        print("走路")
class Studet(Person):
    y = 2
    def __init__(self,age):
        super(Studet, self).__init__()
        self.age = age
    def eat(self):
        print("吃")
stu = Studet(18)
print(stu.z)
print(stu.y)
print(stu.age)
#stu.name  #能调name属性吗？
stu.walk()
stu.eat()