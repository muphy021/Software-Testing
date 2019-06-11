# -*- encoding: utf-8 -*-

import smtplib

# connect to smtp
smtpobj=smtplib.SMTP('smtp.skyguard.com.cn', 587)
smtpobj.starttls()
smtpobj.login("mofei@skyguard.com.cn", "Sky$1588")
smtpobj.sendmail("mofei@skyguard.com.cn", "murphy_021@qq.com", "Subject: Link\n Dear sir, \nThis is for your mail.")
smtpobj.quit()