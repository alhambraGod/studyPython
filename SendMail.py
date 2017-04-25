# -*- coding: utf-8 -*-

# MUA: Mail User Agent
# MTA: Mail Transfer Agent
# MDA: Mail Delivery Agent
# 发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

########### msn.com info ###############
# 服务器名称: pop-mail.outlook.com
# 端口: 995
# 加密方法: TLS
#
# 服务器名称: imap-mail.outlook.com
# 端口: 993
# 加密方法: TLS
#
#
# 服务器名称: smtp-mail.outlook.com
# 端口: 587
# 加密方法: STARTTLS

from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def sendMail():
    import pickle
    mailInfoPath = r'D:\temp\python_mail_info.txt'
    #############################################
    # write mail info to local file
    # with open(mailInfoPath, 'wb') as f:
    #     info = {'from'        : 'xxxx@xxxx.com',
    #             'password'    : 'xxxxxxxxx',
    #             'to'          : 'xxxx@xxxx.com',
    #             'smtp server' : 'xxxxxxxxx',
    #             'smtp port'   : 'xxxx'}
    #     f.write(pickle.dumps(info))
    #############################################

    import os
    if (not os.path.exists(mailInfoPath)):
        print('FAIL TO SEND MAIL. mail info file does not exist: %s' % mailInfoPath)
        return
    info = None
    with open(mailInfoPath, 'rb') as f:
        info = pickle.load(f)
        print(info)

    # construct mail message
    msg = MIMEText(
        'hello, send by python',  # text
        'plain',   # subtype
        'utf-8')
    msg['From'] = _format_addr('JingweiPythonTester <%s>' % info['from'])
    msg['Subject'] = Header('Test email sent from python by Jingwei', 'utf-8').encode()

    import smtplib

    print('smtplib.SMTP(). Connecting to (%s, %s)' % (info['smtp server'], info['smtp port']))
    server = smtplib.SMTP(info['smtp server'], int(info['smtp port']))
    print('smtplib.SMTP(). Connected')
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()

    print('server.login()...')
    server.login(info['from'], info['password'])

    print('server.sendmail()...')
    server.sendmail(info['from'], [info['to']], msg.as_string())
    print('server.sendmail() done')

    server.quit()