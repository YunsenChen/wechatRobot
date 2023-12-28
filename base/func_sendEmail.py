import re
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from time import sleep

from_add = '15217449529@163.com'   # 发件人邮箱
key = 'YDSWXXLVVHGQKPWM'     # 发件人邮箱密码  即配置生成的授权码
#to_add = '1316568848@qq.com'  # 收件人
#to_add = '1623582336@qq.com'  # 收件人
def sendEmail(email,content):
    ret = True
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr([content, from_add])    # 发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([content, email])   # 收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = content   # 邮件的主题

        server = smtplib.SMTP_SSL('smtp.163.com')
        server.login(from_add, key)
        server.sendmail(from_add, [email, ], msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret

def sendNEmail(email,content,n):
    ret=True
    try:
        for i in range(n):
            sendEmail(email,content)
            print(i)
            sleep(0.5)
    except Exception:
        ret=False
    return ret


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ret = sendNEmail(to_add, "hi", 10)
    # if ret:
    #     print('邮件发送成功！')
    # else:
    #     print('邮件发送失败！')
    text="跟1316568848@qq.com发送2封邮件，内容是:你好！"
    if(("邮件" in text)):
        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
        print(emails[0])
        numbers = re.findall(r'\d+', text)
        n=int(numbers[1])
        print(n)
        #print(int(numbers[0]))
        semi_index=text.find(":")
        if semi_index!=-1:
            content_tosend=text[semi_index+1:]
        sendNEmail(to_add,content_tosend,n)
            #print(content_tosend)
