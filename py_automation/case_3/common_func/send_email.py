# -*- encoding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def send_email(report_file):
    f = open(report_file, 'rb')
    mail_body = f.read()
    f.close()

    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户名/密码
    user = 'fmo021@163.com'
    password = '********'
    sender = "fmo021@163.com"
    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver = ['fmo021@126.com', 'murphy_021@qq.com']

    # 发送邮件主题
    subject = '自动定时发送测试报告'

    # 编写 HTML类型的邮件正文
    msg = MIMEMultipart('mixed')
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg_html1["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html1)



    msg['From'] = "fmo021@163.com"
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject, 'utf8')

    # 编写发送邮件
    open_smtp = smtplib.SMTP()
    open_smtp.connect(smtpserver, 25)
    open_smtp.login(user, password)
    open_smtp.sendmail(sender, receiver, msg.as_string())
    open_smtp.quit()

