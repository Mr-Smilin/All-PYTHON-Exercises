# -*- coding: utf-8 -*-

import config
import post
import bugData

if __name__ == "__main__":
    my_account = post.Post()
    my_account.login(config.USERNAME, config.PASSWORD)
    my_account.newthread(config.FID, config.TITLE, bugData.data)
#    my_account.reply('10', u'发帖回复')
