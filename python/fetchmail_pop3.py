
# coding: utf-8

'''
    邮件关机脚本，
    原理：启动脚本，读取邮箱信息，当有符合要求的邮件时执行响应命令
    目前只有关机命令
    之后将支持扩展和自定义命令（邮件接收命令）
'''

import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import time,os,signal

loop = True

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def loop_get_mail():
    while loop:
        # 连接到POP3服务器:
        server = poplib.POP3(pop3_server or 'pop.exmail.qq.com')
        # 可选:打印POP3服务器的欢迎文字:
        print(server.getwelcome().decode('utf-8'))

        # 身份认证:
        server.user(email or 'wufj@chetong.net')
        server.pass_(password)
        # list()返回所有邮件的编号:
        resp, mails, octets = server.list()

        # 获取最新一封邮件, 注意索引号从1开始:
        index = len(mails)
        resp, lines, octets = server.retr(index)

        # lines存储了邮件的原始文本的每一行,
        # 可以获得整个邮件的原始文本:
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        # 稍后解析出邮件:
        msg = Parser().parsestr(msg_content)

        mail_from = msg.get('From')
        mail_from = decode_str(mail_from)
        mail_subject = msg.get('Subject')
        mail_subject = decode_str(mail_subject)

        print(mail_from)
        print(mail_subject)
        if mail_from=='Rang <wea13193081281@163.com>' and mail_subject=='shutdown':
            #print('shutdown')
            os.system('shutdown -a')
            # 可以根据邮件索引号直接从服务器删除邮件:
            server.dele(index)
            # 关闭连接:
            server.quit()
        
        time.sleep(2)

if __name__=='__main__':
    # 输入邮件地址, 口令和POP3服务器地址:
    email = input('Email: ')
    password = input('Password: ')
    pop3_server = input('POP3 server: ')

    import threading

    th = threading.Thread(target=loop_get_mail)
    th.start()

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        loop = False

    print("sleep finished")
    th.join()