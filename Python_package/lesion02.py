str1 = 'python hello aaa 123123aabb'
str2 = str1.replace('python','lemon')
print(str2)
print(str1.index('aaa'))
name = input('请输入姓名')
sex = input('请输入性别')
name = 'muse'
sex = '女'
age = 18
print('''
       姓名：%s
       sex:%s
       年龄: %d
'''
% (name,sex,age)
)
