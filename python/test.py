# print(list(range(1,10,5)))
#print([3] in [1,2,3,4])
# d = {'a': 1, 'b': 2}
# print(d.setdefault('x','yes'))  # yes

# def fun(number):
#     number = number//100
#     if number == 0:
#         return
#     print(number)
# fun(54321)

# prime_number=[]
# for i in range(2,11):
#     counter = 0
#     for j in range(1,i):
#         if i % j == 0:
#             counter += 1
#     if counter == 1:
#         prime_number.append(i)
# print(prime_number)   取出质数

# strinfo=" hello,where are you from? Are you American? do you from china? no,I am from Australian "
# print(strinfo.count('re'))
# print(strinfo.count(' '))
# print(strinfo.replace('om','en'))
# print(strinfo.split('?'))
# print(strinfo)
# print(strinfo.strip())
# print(strinfo.replace(strinfo,'Y(^_^)Y'))


# li=['h', 'e', 'l', 'l', 'o']
# print(li[1:])
# print(li[:-4])
# li.insert(3,'x')
# print(li)
# li.reverse()
# print(li)
# print(li.index('e'))


# class Father():
#     x = 1
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print('吃饭')
# class Son(Father):
#     pass
# son = Son('doudou')
# print(son.x)
# print(son.name)
# son.eat()



# 冒泡排序
# li=[18,56,24,21,33]
# print(li)
# for i in range(len(li)-1):
#     for j in range(len(li)-1-i):
#         if li[j] > li[j+1]:
#             li[j],li[j+1]=li[j+1],li[j]
# print(li)




# 1. 读取一个txt文件，文件内容为
# 姓名， 邮箱
# abc，123@163.com
# xyz，456@163.com
#
# 得到结果并写入新文件中：
# abc的邮箱为123@163.com
# xyz的邮箱为456@163.com

# with open('b.txt','r',encoding='utf-8') as f:   #打开文件a.txt
#     data = f.readlines()   #以列表形式返回文件的内容
# f2 = open('a.txt','w',encoding='utf-8')  #新建b.txt文件
# data = data[1:]   #截取第二个元素到最后一个元素
# for i in data:  #循环新的列表
#     #把新列表的元素以','分隔，以元组的形式写入到新的文件b.txt里
#     f2.write("%s,%s" % tuple(i.split('的邮箱为')))
#     f2.flush()
# f2.close()





# import pymysql
# config = {
#     'host':'192.168.1.156',
#     'port':3306,
#     'user':'root',
#     'password':'123456',
#     'db':'ecshop',
#     'charset':'utf8',
#     'cursorclass':pymysql.cursors.DictCursor
# }
# db = pymysql.connect(**config)
# cur = db.cursor()
# sql = "SELECT * FROM ecs_admin_user"
# cur.execute(sql)
# data = cur.fetchall()
# print(data)
# join的使用，新的字符串
# lst = '123asdfghj123456'
# print(lst.join('222'))
# print(lst.split('2'))


# from time import sleep
# class Father():
#     def run(self):
#         lst = [1, 2, 3, 4]
#         for i in range(len(lst)):
#             print(lst[i])
#             sleep(1)
#     def eat(self,name):
#         print(name)
# print(__name__)
# if __name__ == '__main__':
#     father = Father()
#     father.eat('doudou')





