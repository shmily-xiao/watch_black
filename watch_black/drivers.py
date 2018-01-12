#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pymongo import MongoClient
import time

from singleton import singleton

@singleton
class MongoDB(object):
    def __init__(self):
        self.connect = MongoClient("127.0.0.1",27017)
        self.db = self.connect["watch_black"]


if __name__ == '__main__':
    connect = MongoClient("127.0.0.1",27017)
    dbName = "watch_black"
    db = connect[dbName]
    user_data = {
        "user":"wangzaijun",
        "wangzaijun":
            {"real_name":"王再军",
             "user_name":"wangzaijun",
             "user_email":"wangzaijun1234@126.com",
             "day_summary":[
                 {"create_time": time.time() + 10,"title":"nihao1", "content":"njlnlklknlknyuyuiiyukktyunlksad"},
                 {"create_time": time.time(),"title":"nihao2", "content":"njlnlklknl;/plop';oi;poiknnlksad"}
             ],
             "note":{"create_time": time.time(), "content":"haiyouhenduo meiyouzuo 你", "update_time":time.time()}
             }
    }
    db.user.insert(user_data)
    user_log = {"create_time":time.time(), "user_name":"王再军", "title": "nihao1"}
    db.oper_log.insert(user_log)
    user_log = {"create_time":time.time(), "user_name":"王再军", "title": "nihao2"}
    db.oper_log.insert(user_log)