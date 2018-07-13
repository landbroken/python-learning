from email.mime.text import MIMEText
import smtplib

"""
构造MIMEText对象时，
第一个参数就是邮件正文，
第二个参数是MIME的subtype，传入'plain'表示纯文本，
最终的MIME就是'text/plain'，
最后一定要用utf-8编码保证多语言兼容性。
"""
msg = MIMEText('hello, send by Python email test. Lin in 2018.1.31.', 'plain', 'utf-8')
msg['Subject'] = "python 邮件test"  # 邮件主题
# 输入Email地址和口令:
from_addr = '445299258@qq.com'
password = 'nzwsdynhijbgbhch'  # QQ邮箱提示：在第三方登录时密码框输入授权码nzwsdynhijbgbhch
# 输入收件人地址:
to_addr = '2046675974@qq.com'
"""
使用SSL的通用配置如下：
接收邮件服务器：pop.qq.com ,使用SSL,端口 995
发送邮件服务器： smtp.qq.com,使用SSL,端口 465或 587
"""
# 输入SMTP服务器地址:
smtp_server = 'smtp.qq.com'

print("set SMTP server.")
server = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP协议默认端口是25
try:
    # server.set_debuglevel(1)  # 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
    print("trying login.")
    server.login(from_addr, password)
    print("login over.")
    server.sendmail(from_addr, [to_addr], msg.as_string())
    print("Send over")
except smtplib.SMTPException as e:
    print("Failed to send email")
finally:
    server.quit()
