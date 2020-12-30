from Python_package.lesion07 import read_case,login,write_result
def test_fun(filename,sheetname):
    cases = read_case(filename,sheetname)#先读取数据（从Excel表格中）；调用函数，设置变量接收返回值
    for case in cases:
        case_id =case['cell_id']#获取用例编号
        test_url = case['url']#获取URL
        test_data = eval(case['data'])#字符串==字典
        test_expect =eval(case['expect'])#字符串转成字典
        expect_msg = test_expect['msg']
        real_result = login(url=test_url,data=test_data)#实际执行结果
        real_msg=real_result['msg']
        print('期望结果为:{}'.format(expect_msg))
        print('实际结果为:{}'.format(real_msg))
        if expect_msg==real_msg:
            print("第{}条用例执行通过".format(case_id))
            finnal_real = 'passed'
        else:
            print('这{}条用例执行不通过'.format(case_id))
            finnal_real = 'failed'
        write_result(filename,sheetname,case_id+1,8,finnal_real)
        print('='*22)
# test_fun('D:\\PycharmProjects\\scb18\\test_data\\test_case_api.xlsx', 'register')
# test_fun('D:\\PycharmProjects\\scb18\\test_data\\test_case_api.xlsx', 'login')