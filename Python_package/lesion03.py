# list1 = []  #空列表
# print(type(list1))   #判断类型
list2 = [1,3.14,True,'python',[1,2,3]]
# print(list2)
# print(list2[1]) #第一位的内容，从索引0开始数
# print(list2[:len(list2):2])  #列表中从0开始，步长为2的内容
# print(len(list2))   #列表的长度，共5位
# print(list2[3][4])    #列表中的嵌套取值  输出Python中的'o'

#列表--增
# list2.append('小林')
# # print(list2)  #追加元素到列表末尾
# list2.insert(4,'betty')   #指定元素位置进行插入
# print(list2)
# #列表---改
# list2[0] = '小程'   #找到元素，重新赋值
# list2[2] = '华东'   #找到哦元素重新赋值
# print(list2)
#列表--删
# list2.pop()  #默认删除最后一个元素
# print(list2)
# list2.pop(0)   #指定索引位置来进行删除
# print(list2)
# list2.remove('python')   #指定元素位置进行删除
# print(list2)
# list2.remove('小程')      #指定元素进行删除存在多个重复元素，删除找到的第一个元素
# print(list2)
# tuple1 = ()
#tuple转换list
# tuple2 = (666,'java',3,14,[6,7,8])
# list3 = list(tuple2)
# list3.insert(5,'橘子')
# print(list3)
# print(type(list3))
#增加
# list3.append('西瓜')
# print(list3)
#改
# list3[0] = '苹果'
# print(list3)
#删
# list3.pop(0)
# print(list3)
# print(tuple2[1])   #指定元祖中元素的位置，从0开始
# tuple2 = (666, 'java', 3, 14, [6, 7, 8])
# tuple2 = (666, 'java', 3, 14, [6, 7, 8])
# temp_tuple2 = (666, 'java', 3, 14, [6, 7, 8])
# print (temp_tuple2)
# print(type(temp_tuple2))
# b = list(temp_tuple2)   #将temp——tuple2进行强制转换
# print(b)
# print(type(b))    #查看是否转换成功
dict1 = {'name':'橙子','age': 18,'hobby': '喜欢写代码'}
# print(dict1)
# print(dict1['name'])   #通过key来去value值  一定是[]
# print(dict1.get('name'))
# print(dict1.keys())
# print(dict1.values())
# dict1['city'] = '长沙'
# print(dict1)
#改
# dict1['name'] = '西瓜'
# print(dict1)
# dict1.pop('age',18)
# print(dict1)
# money = int(input('请输入自己的账户余额：'))
# if money > 80000:
#         print('买个车子')
# elif money > 50000:
#         print('去国外旅游')
# elif money > 30000:
#         print('国内旅游')
# else:
#         print('继续搬砖')
# str1 = '速成18期'
# count = 0
# for i in str1:
#     if i == '1':
#         continue
#     count += 1
#     print(count)
#     print(i)
#     print('*'*5)
# range(5)
# count = 0
# for i in range(5):
#     count += 1
#     print(count)
#     print('*'*3)
# a = (1, 2, '6', 'summer')
# print('i' in a)
# dict_1 = {'class_id': 45, 'num': 20}
# a = dict_1['num']
# if a > 5:
#     print(a)
# else :
#     print('人数太少，不上课')
list1 = ['丁丁','橙子', '小琳', '华栋', '古月', '生命的旅程']
dict1 = {'name':'丁丁','sex':'女','age':18,'city':'重庆'}
dict2 = {'name':'橙子','sex':'女','age':19,'city':'浙江'}
dict3 = {'name':'小琳','sex':'女','age':20,'city':'北京'}
dict4 = {'name':'华栋','sex':'男','age':21,'city':'北京'}
dict5 = {'name':'古月','sex':'女','age':22,'city':'黑龙江'}
dict6 = {'name':'生命的旅程','sex':'男','age':23,'city':'上海'}
list2 = [dict1,dict2,dict3,dict4,dict5,dict6]

print(list2)