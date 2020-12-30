# def good_job(salary,bouns,subsidy=300,*args,**kwargs):  #定义函数的同时，去定义参数即变量-----这个形式是形参，真正调用的时候再去传
#     sum1 = (salary+bouns+subsidy)
#     print('参数salary：{}'.format(salary))
#     print('参数bouns:{}'.format(bouns))
#     print('参数subsidy:{}'.format(subsidy))
#     print('参数*args:{}'.format(args))
#     print('参数*kwargs:{}'.format(kwargs))
#     for i in args:
#         sum1 += i
#     for j in kwargs.values():
#         sum1 += j
#     print(sum1)
#     # print('今天天气很好')
#     return sum1
#
# #函数调用
# #定义一个变量来接收函数调用后的返回值，这里用result变量
# result = good_job(9000,2000,300,100,a=1000,b=200)##这里就是关键字传参
# print(result)
# if result > 10000:
#     print('这个工作不错，继续干下去')
# else:
#     print('赶紧辞职，重新找工作')
# str1 = '你真的很不错'
# list1 = [str1]
# print(list1)
# print(type(list1))
# amount = 300
# salary = 3000
# print(amount+salary)
#定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。--if 判断嵌套 
# str1 = '好好学习,天天向上'
# print(len(str1))
# def dx(str1):
#     if str1(len(str1)) > 5:
#         print('true')
#     else:
#         print('false')
#         return  dx(str1)
# result = dx(str1)
# print(result)
