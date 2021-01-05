import requests
import jsonpath
#注册
# url_reg = 'http://120.78.128.25:8766/futureloan/member/register'#请求地址
# headers_reg = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json'}#请求头
# data_reg = {"mobile_phone": "15678328798","pwd": "lemon666","type":"1","reg_name":"围巾"}#请求体
# response_reg = requests.post(url=url_reg,headers=headers_reg,json=data_reg)#调用post，用变量接收返回值
# # print(response_reg.status_code)#获取HTTP状态码
# print(response_reg.headers)#获取请求头
# print(response_reg.text)#text获取响应结果
# print(response_reg.json())#json获取响应结果
#登录
def login(url,data):
    headers_log ={'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json'}
    response_log =requests.post(url=url,headers=headers_log,json=data).json()
    #返回值
    return response_log
    #调用login（）
url_log = 'http://120.78.128.25:8766/futureloan/member/login'
data_log = {"mobile_phone": "15678328798", "pwd": "lemon666"}
result=login(url=url_log,data=data_log)
# print(result)
    #充值
#如何获取token
# member_id = response_log['data']['id']#获取id，赋值给变量名member_id
# token = response_log['data']['token_info']['token']#字典嵌套获取token，赋值给变量名token
# print(token,member_id)
# url_recharge = 'http://120.78.128.25:8766/futureloan/member/recharge'
# headers_recharge = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json','Authorization':'Bearer'+' '+token}#这里b值的输入一定要注意，要打空格
# data_recharge = {"member_id":member_id, "amount":"35000"}
# response_recharge = requests.post(url=url_recharge,headers=headers_recharge,json=data_recharge).json()
# print(response_recharge)
#第2种获取token值
#1）安装jsonpath,cmd输入pip install jsonpath
#2)import jsonpath
#import jsonpath
#充值
# member_id = jsonpath.jsonpath(response_log,'$..id')[0]#获取id，赋值给变量名member_id
# token = jsonpath.jsonpath(response_log,'$..token')[0]#字典嵌套获取token，赋值给变量名token
# # print(token,member_id)
# url_recharge = 'http://120.78.128.25:8766/futureloan/member/recharge'
# headers_recharge = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json','Authorization':'Bearer'+' '+token}#这里b值的输入一定要注意，要打空格
# data_recharge = {"member_id":member_id, "amount":"37000"}
# response_recharge = requests.post(url=url_recharge,headers=headers_recharge,json=data_recharge).json()
# print(response_recharge)

