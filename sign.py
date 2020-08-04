# -*- coding: utf-8 -*-

import requests
import re

def check(str):
    signing = '<button id="checkin" class="btn btn-brand btn-flat">'
    signed = '<a class="btn btn-brand disabled btn-flat" href="#">'
                
    yes = re.search(signing, str.decode('utf-8'))
    if yes == None:
        no = re.search(signed, str.decode('utf-8'))
        if no == None:
            return -1; # 什么都没找到
        else:
            return 0 # 找到了"今日已签到"
    else:
        return 1 # 找到了"签到"
    
# 根据你的邮箱和密码修改email和password的值
email = 'your email'
password = 'your password'
loginurl = 'https://liangchenyun.xyz/auth/login'
# 这行代码是用来维持cookie的，你后续的操作都不用担心cookie，他会自动带上相应的cookie
s = requests.Session()
# 带表单的参数
loginparams = {'email':email, 'passwd':password}
# post数据实现登陆
s.post(loginurl, data=loginparams)
# 验证是否登陆成功，抓取首页看看内容
r = s.get(loginurl)
# print(r.text)
res = check(r.content)
if (res == 1):
    checkinUrl='https://liangchenyun.xyz/user/checkin'
    s.post(checkinUrl)
    print('签到成功')
elif (res == 0):
    print('今日已签到')
else:
    print('签到失败')


