# -*- coding: utf-8 -*-

import re

import config
import discuz

class Post(discuz.Discuz):
    def __init__(self):
        super(Post, self).__init__()

        self.post_success_pattern = re.compile(r'<meta name="keywords" content="(?u)(.+)" />')  # 发帖成功时匹配
        self.post_fail_pattern = re.compile(r'<div id="messagetext" class="alert_error">')  # 发贴失败时匹配
        self.post_error_pattern = re.compile(r'<p>(?u)(.+)</p>')  # 发贴失败的错误信息
        
    def newthread(self, fid, subject, message):
        postdata = {
                    'subject': self._interception(subject, 80),
                    'message': message,
                    'formhash': self.formhash,
                    'htmlon': 1,
        }
        
        base_url = config.POSTURL
        url = base_url.replace('FID', fid)
        self.operate = self._get_response(url, postdata)
        
        #prefix = ur'主題 "%s" ' % postdata['subject']
        #self.__verify_post_status(prefix)
        
    def reply(self, tid, message):
        postdata = {
                    'message': message,
                    'formhash': self.formhash,
                    'htmlon': 1,
        }
        
        base_url = config.REPLYURL
        url = base_url.replace('TID', tid) 
        self.operate = self._get_response(url, postdata)
        
        prefix = ur'回復 "%s" ' % self._interception(message, 80)
        self.__verify_post_status(prefix)       
    
    def __verify_post_status(self, prefix):
        page_content = self.operate.read().decode('utf-8')
        
        if self.post_success_pattern.search(page_content):
            print "%s發布成功！" % prefix
        elif self.post_fail_pattern.search(page_content):
            post_error_message = self.post_error_pattern.search(page_content)
            try:
                print "%s發布失敗！原因是：%s。" % (prefix, post_error_message.group(1))
            except:
                print "%s發布失敗！原因是：未知原因。" % prefix
        else:
            print "無法確定%s發布狀態" % prefix
