#1. 有这样一种数如：12321（第一个等于最后一个，第二个等于倒数第二个，
# 以此类推，直到中间仅剩一个数），写一个函数，传入一个整数，
# 判断这个数是不是这种前后一样的数。
# def fun1(num):
#     bool_=True
#     if len(num) % 2 ==0:
#         print("这个数不是神奇的数")
#     else:
#         for i in range((len(num)-1) // 2):
#             if num[i] != num[len(num)-1-i]:
#                 bool_=False
#     if bool_:
#         print("这个数是神奇的数")
#     else:
#         print("这个数不是神奇的数")
# a = input("请输入一个神奇的数：")
# fun1(a)



#2.有这样一个矩阵，设计一个函数，根据我输入的参数，
# 返回其所在的位置是几行几列[[3,8 ,9],[6,11,2],[7,18,5]]

# def fun2(num):
#     lst = [[3,8 ,9],[6,11,2],[7,18,5]]
#     for i in range(3):
#         for j in range(3):
#             if num == lst[i][j]:
#                 a = i
#                 b = j
#                 break
#     print("%d在%d行%d列" % (num,a,b))
# fun2(3)
# fun2(8)
# fun2(9)
# fun2(6)
# fun2(11)
# fun2(2)
# fun2(7)
# fun2(18)
# fun2(5)





#3.实现登录，账号名为admin，密码123，则提示“登录成功”，
# 如果账号或者密码错误，则提示“账号名或密码错误”并允许重新输入用户名和密码，
# 如果3次登录失败，则提示“登录失败”并退出程序。
# def fun3():
#     user = input("请输入账号名：")
#     pwd = input("请输入密码：")
#     if user == 'admin' and pwd == '123':
#         print("登录成功")
#     else:
#         print("请重新输入用户名和密码")
#         fun3()
# fun3()
# count = 0
# while 1:
#     user = input("请输入账号名：")
#     pwd = input("请输入密码：")
#     count = count + 1
#     if user == 'admin' and pwd == '123':
#         print("登录成功")
#         break
#     if count == 3:
#         print("登录失败")
#         break




#编写输入任意一张银行卡号，输出银行卡号的前6位和后4位，
# 剩下的所有数字用星号（*）表示
#如：card("5189301239921331") -> 518930 ** ** ** 1331

# card =input("请输入一个至少11位的正整数：")
# card1=card[:6]
# card2=card[-4:]
# str='*'*(len(card)-10)
# print("加密后的卡号：")
# print(card1+str+card2)






#有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# lst=[1,2,3,4]
# lst1=[]
# for i in lst:
#     for j in lst:
#         if i != j:
#             for k in lst:
#                 if i != k and j != k:
#                     print(str(i)+str(j)+str(k))





#打印九九乘法表。

# for i in range(1, 10): #循环行
#     for j in range(1, i + 1): #循环列
#         print("%d*%d=%d " % (i, j, i * j),end='') #做乘法，不换行
#     print()#换行





#草莓15元一斤，火龙果3元一个，香蕉2元一斤，刚好花完200元，
# 每种至少有一个/斤，有多少种可能，并列举出来
# cm = 15
# hlg = 3
# xj = 2
# sum = 200
# #count = 0
# lst = []
# for i in range(1,sum//cm+1):
#     for j in range(1,sum//hlg+1):
#         for k in range(1,sum//xj+1):
#             if i*cm + j*hlg + k*xj == sum:
#                 lst.append([i,j,k])
# #                count = count + 1
# #                print("草莓%d 火龙果%d 香蕉%d" % (i, j, k))
# #print("共%d种可能" % count)
# print(lst)
# print(len(lst))






# 1.求1-2+3-4+5 ... 99的所有数的和
# total = 0   #定义一个变量total，初始值为0
# for i in range(1,100):  #1到99的循环
#     if i%2 != 0:        #奇数时做加法
#         total = total + i
#     else:                #偶数时做减法
#         total = total - i
# print("1-2+3-4+5…99=%d" % total)   #打印结果
# 2.元素分类
# 有如下值集合 [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个 key 中，将小于 66 的值保存至第二个 key 的值中。
# 即： {'k1': 大于 66 的所有值,'k2': 小于 66 的所有值}
# lst = [11,22,33,44,55,66,77,88,99,90]  #定义一个列表lst
# dct = {'k1':[],'k2':[]}   #定义一个键为k1/k2、值为空列表的字典
# for i in lst:     #循环列表lst
#     if i > 66:    #条件判断，值大于66
#         dct['k1'].append(i)   #值添加到k1的空列表里
#     elif i < 66:   #条件判断，值小于66
#         dct['k2'].append(i)    ##值添加到k2的空列表里
# print(dct)  #打印字典dct
# 3.自定义一个list，每暂停一秒输入一个元素(使用 time 模块的 sleep() 函数)
# from time import sleep  #引入time模块的sleep(函数)
# lst = []  #定义一个空列表
# while 1:  #死循环
#     a = input("请输入列表元素：")    #手动输入列表元素
#     lst.append(a)    #输入的值添加到列表lst中
#     sleep(1)   #每隔一秒执行一次
#自定义一个list，每暂停一秒输出一个元素(使用 time 模块的 sleep() 函数)
# from time import sleep      #引入time模块的sleep(函数)
# lst = [1,2,3,4,5,6,7,8,9,0]  #定义一个列表
# for i in range(len(lst)):     #循环这个列表
#     print(lst[i])           #打印这个元素的值
#     sleep(1)                ##每隔一秒执行一次
# 4.自定义一个list,按相反的顺序输出列表的值 （不能使用reverse()方法）
# lst = [1,'a',2,(12,34),[1,'d'],{'key1':1,'key2':2}]   #定义一个元素个数为偶数的列表lst
# #lst = [1,2,3,4,5]     #定义一个元素个数为奇数的列表lst
# print(lst)     #打印这个列表
# lst1 = lst[-len(lst)//2:]     #用新列表lst1截取lst右半边（长度取整，可能会比左边的少一个元素）
# for i in range(len(lst)):    #循环整个列表lst
#     if i < len(lst)//2:     #如果元素在左半边，就把这个元素的值赋给右边与之对应的位置上
#         lst[len(lst)-1-i] = lst[i]
#     else:         #如果元素在右半边，就把lst1中对应的值赋给左边与之对应的位置上
#         lst[len(lst) - 1 - i] = lst1[i-len(lst)//2]
# print(lst)   #打印新的列表
# lst = [2,'a',2,(12,34),[1,'d'],{'key1':1,'key2':2}]   #定义一个元素个数为偶数的列表lst
# #lst = [1,2,3,4,5]     #定义一个元素个数为奇数的列表lst
# print(lst)     #打印这个列表
# for i in range(len(lst)//2):    #循环整个列表lst
#     lst[i],lst[len(lst)-1-i]=lst[len(lst)-1-i],lst[i] #交换值
# print(lst)   #打印新的列表

#from time import sleep
# from test import Father
# class Son(Father):
#     def eat(self,name,age):
#         print(name,age)
#
#
# print(__name__)
# son = Son()
# son.eat('doudou',18)

dic={'k1':1,'k2':2}
print(dic['k1'])
dic['k1']=2
dic['k3']=3
print(len(dic))
print(dic)
print(dic.items())
