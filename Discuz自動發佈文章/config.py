# -*- coding: utf-8 -*-

import xlrd

book=xlrd.open_workbook('logindata.xlsx')
sheet=book.sheets()[0]


DOMAIN = ur""+(sheet.cell(0,0).value)
USERNAME = ur""+(sheet.cell(1,0).value)
PASSWORD = ur""+(sheet.cell(2,0).value)
FID = ur""+(str(sheet.cell(3,0).value))
TITLE = ur""+(sheet.cell(4,0).value)
TITLE=TITLE.encode('utf-8')

LOGINFIELD = r'username'
COOKIETIME = 2592000

HOMEURL = DOMAIN + 'forum.php'
LOGINURL = DOMAIN + 'member.php?mod=logging&action=login&loginsubmit=yes&frommessage&inajax=1'

POSTURL = DOMAIN + 'forum.php?mod=post&action=newthread&fid=FID&extra=&topicsubmit=yes'
REPLYURL = DOMAIN + 'forum.php?mod=post&action=reply&tid=TID&extra=&replysubmit=yes'
