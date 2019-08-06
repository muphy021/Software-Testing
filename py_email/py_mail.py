# -*- encoding: utf-8 -*-

'''
此用例，用于自动读取草稿中的条目，然后写入邮件。

step 1：
读取草稿文件

step 2：
格式化读取的内容
'''



from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid
from smtplib import SMTP, SMTP_SSL

import datetime


# -----------
# 获取报告原文
# -----------
def read_report():
    send_msg = ''  # 初始化发送的内容
    open_report = open("./weeklyreport", "r", True, "utf-8")
    weekly_report = open_report.readlines()
    # print(weekly_report)

    for content in weekly_report:
        # print(content)
        send_msg=send_msg+content
    open_report.close()
    return send_msg

# ---------
# 格式化报告
# ---------
def format_report(send_msg):
    send_msg='Hi Frank, <br/>' \
                  '    下面是本周QA的主要工作：\n'\
                  + send_msg + 'Thanks and Regards<br/>' \
                  'Murphy<br/>'

    print("准备发送的内容是：" + send_msg)#发送的内容

    html_start = '<font face="Courier New, Courier, monospace"><pre>'
    html_end = '</pre></font>'

    msg = MIMEText(html_start + send_msg + html_end, _subtype='html', _charset='utf-8')
    msg['To'] = '*******,*******'
    msg['Cc'] = '*******'
    msg['From'] = '*******'

    date_internal = datetime.timedelta(5)  # 日期相差的天数
    end_date = datetime.date.today()
    start_date = end_date - date_internal
    print(date_internal)
    print(start_date)
    print(end_date)

    msg['Subject'] = 'QA weekly report from ' + start_date.strftime('%Y-%m-%d') + " to " + end_date.strftime(
        '%Y-%m-%d')  # 将日期传化为str
    msg['Date'] = formatdate(localtime=1)
    msg['Message-ID'] = make_msgid()
    return msg

# ---------------
# connect to smtp
# 发送邮件
# ---------------
def send_report(format_msg):
    smtp_server = 'smtp.*******'
    smtp = SMTP(smtp_server)
    smtp.set_debuglevel(1)

    smtp.login('mofei@*******', '******')
    smtp.sendmail(format_msg['From'], format_msg['To'].split(',')+format_msg['Cc'].split(','), format_msg.as_string())#支持多个联系人时，需要.split('')
    smtp.quit()



# 使用上述函数
format_msg = format_report(read_report())
send_report(format_msg)


