# -*- coding:utf-8 -*-

import sys
sys.path.append(r'/Users/chenhang/Desktop/pythonFile/python/untitled/practice/pyhton-unittest-jenkins/lib')
from fileOperation import newFile
from fileOperation import openFile
from sendEmail import mail
import all_tests
import HTMLTestRunner
import time




now_time = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
reportPath = r"/Users/chenhang/Desktop/pythonFile/python/untitled/practice/pyhton-unittest-jenkins/report/"
filename = reportPath + now_time + 'requort.html'
fp = open(filename, 'wb')



runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试整合报告', description=u'用例执行情况')
runner.run(all_tests.suite())



'''发送邮件'''

# 创建email_content容器
email_content = {}


# 读取最新报告路径
reportPath2 = newFile(reportPath)
email_content['reportPath'] = reportPath2
print("测试报告路径："+"\n" + reportPath2)

# 读取最新报告内容
reportHtml = openFile(reportPath2)
email_content['reportHtml'] = reportHtml
# print("测试报告内容："+"\n" + reportHtml)


'''将获取的报告内容发送邮件'''

# 发送邮箱用户名、账号/密码
user_email = '小h'                        # 发件人邮箱昵称
sender_email = '443990096@qq.com'         # 收件人邮箱账号
password_email = 'btsfupcotihybhhj'       # 发件人邮箱密码

# 收件人邮箱
# 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
receiver_email = ['shaomingbo@smartcinema', 'chenhang@smartcinema.com.cn']
# receiver_email = 'chenhang@smartcinema.com.cn'
# receiver_email = 'shaomingbo@smartcinema.com.cn'
# receiver_email = '1779505264@qq.com'





retMail = mail(user_email,sender_email,password_email,receiver_email,reportHtml)
if retMail:
    print("邮件发送成功")
else:
    print("邮件发送失败")



print("========邮件发送内容=======")
print(email_content)
print("========邮件发送内容=======")