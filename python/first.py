#1.从键盘接收一个输入，输入成绩，
# 当输入的成绩在60以下时，打印不及格，
# 60-79打印及格，80及以上打印优秀
# grade = int(input("请输入成绩："))
# if grade < 60:
#     print("不及格")
# elif 60 <= grade < 80:
#     print("及格")
# else:
#     print("优秀")


# a = input("请输入一个神奇的数：")
# print(a)



#2.输入一个整数，如果此数为0，则输出”石头”,如果此数为1，则输出”剪刀”,如果此数为2，则输出”布”,如果为其它，则输出”错误”
# num=input("输入整数：")
# if num=='0':
#     print("石头")
# elif num=='1':
#     print("剪刀")
# elif num=='2':
#     print("布")
# else:
#     print("错误")




#3. 输入一个int型的数据，判断这个数是否能被2整除，如果能被2整除，那么输出“这个数是偶数”，否则输出“这个数是奇数”。
# a=input("输入一个int型的数据：")
# if int(a)%2==0:
#     print("这个数是偶数")
# else:
#     print("这个数是奇数")




#4. 输入两个整数，放入到a与b变量中去，如果a>=b就将a与b中的值进行交换，否则就不交换。目的就是要让a中放的值总是小于或等于b中的数，输出。
# a=input("输入整数a：")
# b=input("输入整数b：")
# if int(a)>=int(b):
#     c=b
#     b=a
#     a=c
#     print("a和b进行值交换")
#     print("a=%s" % (a))
#     print("b=%s" % (b))
# else:
#     print("a和b不进行值交换")
#     print("a=%s" % (a))
#     print("b=%s" % (b))




#5. 输入三个int型的数据，放入到a,b,c三个变量中去，使用条件结构与交换逻辑将这三个变量中的值从小到大排列。
# x=input("输入int型的数据x:")
# y=input("输入int型的数据y:")
# z=input("输入int型的数据z:")
# if int(x)>=int(y):
#     if int(z)>=int(x):
#         print(y,x,z)
#     else:
#         if int(z)>=int(y):
#             print(y, z, x)
#         else:
#             print(z, y, x)
# else:
#     if int(z) >= int(y):
#         print(x, y, z)
#     else:
#         if int(z) >= int(x):
#             print(x, z, y)
#         else:
#             print(z, x, y)






#6. 输入一个三位整数，判断其是不是降序数如:531是降序数 百位>十位>个位
# num=input("输入一个三个整数：")
# if num[0]>num[1]>num[2]:
#     print("这是一个降序数")
#     print("%s>%s>%s" % (num[0],num[1],num[2]))
# else:
#     print("这不是一个降序数")





#7. 现在有一个银行保险柜，有两道密码。
# 想拿到里面的钱必须两次输入的密码都要正确。
# 如果第一道密码都不正确，那直接把你拦在外面；
# 如果第一道密码输入正确，才能有权输入第二道密码。
# 只有当第二道密码也输入正确，才能拿到钱！
# password1=input("请输入第一道密码：")
# if password1=='admin123':
#     print("第一道密码正确！")
#     password2 = input("请输入第二道密码：")
#     if password2 == 'admin':
#         print("第二道密码正确！恭喜成功拿到钱！")
#     else:
#         print("第二道密码错误！")
# else:
#     print("第一道密码错误！")





#8.实现100以内的累加
# sum=0
# for i in range(1,101):
#     sum=sum+i
# print("100以内的累加和为:%d" % (sum))





#9.纸张可以无限次对折，纸张厚度为0.07毫米。问多少次对折至少可以超过8848米？
# i=1
# while i>0:
#     i = i + 1
#     if 2**i*0.07>8848000:
#         break
# print("至少%d次对折后可以超过8848米" % (i))





#10.有一个列表['a','b','c','a','e','a']， 使用for循环统计a出现的次数，并删除其中的所有a元素。
# cou=0
# lst=['a','b','c','a','e','a']
# for i in lst:
#     if i=='a':
#         lst.remove(i)
#         cou=cou+1
# print(cou)
# print(lst)

#正确的方法
# cou=0
# lst=['a','b','c','a','e','a']
# for i in lst:
#     if i=='a':
#         cou=cou+1
# for j in range(cou):
#     lst.remove('a')
# print(cou)
# print(lst)





#11. 写代码，有如下列表，请按照功能要求实现每一个功能
# li = ["hello",'seven',["mon",["h","kelly"],'all'],123,446]
# a.请输出"Kelly"
# b.请使用索引找到 'all'元素并将其修改为"ALL"
# li = ["hello",'seven',["mon",["h","kelly"],'all'],123,446]
# print(li[2][1][1])
# li[2][2]="ALL"
# print(li)




#12一些四位数,百位数字都是3,十位数字都是6,
# 并且它们既能被2整除,又能被 3整除,
# 求这样的四位数中最大的和最小的两数各是几?
# lst=[1,2,3,4,5,6,7,8,9]
# for n in lst:
# lst=[1,2,3,4,5,6,7,8,9]
# for i in range(0,9,2):
#     sum1=1+3+6+i
#     if sum1 % 3 == 0:
#         print("136%d" % (i))
#         break
# lst1=[]
# for m in range(0,9,2):
#     sum2=9+3+6+m
#     if sum2 % 3 == 0:
#         lst1.append("936"+str(m))
# print(max(lst1))



#13 n维矩阵
# n = int(input("请输入维度："))
# lst = []
# for i in range(n):
#     lst1 = []
#     for j in range(n):
# #        num = input("请输入第%d个数字：" % (i*n+j+1))
#         num = input("第%d行第%d列数字：" % (i+1,j+1))
#         lst1.append(int(num))
#     lst.append(lst1)
# print(lst)






# lst = ['a','b','c',1,2,3]
# dic = {lst[0]:lst[3],lst[1]:lst[4],lst[2]:lst[5]}
# print(dic)




# from time import sleep
# i = 1
# lst = []
# while i < 300:
#     i = i + 1
#     if (i + 3) % 5 == 0 and (i - 3) % 6 == 0:
#         print(i)
#         sleep(1)
#         lst.append(i)
# print(lst)
