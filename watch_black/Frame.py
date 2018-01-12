#!/usr/bin/env python
# -*- coding: gbk -*-
# Boa:Frame:Frame1

import wx
import wx.lib.buttons
import wx.lib.analogclock
import wx.richtext
import os
import pymongo

import time

from drivers import MongoDB


def create(parent):
    return BeforeFrame(parent)
    # return Frame(parent)


[wxID_FRAME, wxID_WINDOW_LEFT, wxID_WINDOW_LEFT_LOG_TITLE, wxID_WINDOW_LEFT_LOG,
 wxID_WINDOW_LEFT_USER, wxID_WINDOW_MIDDLE, wxID_WINDOW_MIDDLE_BUTTON_PREV,
 wxID_WINDOW_MIDDLE_BUTTON_NEXT, wxID_WINDOW_MIDDLE_PANEL, wxID_WINDOW_MIDDLE_PANEL_TEXT,
 wxID_WINDOW_MIDDLE_PANEL_TITLE, wxID_WINDOW_RIGHT, wxID_WINDOW_RIGHT_ANALOGCLOCK,
 wxID_WINDOW_RIGHT_TASK_TITLE, wxID_WINDOW_RIGHT_TASK_TEXT, wxID_WINDOW_RIGHT_TASK_SUBMIT,
 wxID_WINDOW_RIGHT_TAG_TITLE, wxID_WINDOW_RIGHT_TAG_TEXT, wxID_WINDOW_RIGHT_TAG_SUBMIT, wxID_BEFORE_FRAME,
 wxID_BEFORE_WINDOW_LOGIN_TEXT, wxID_BEFORE_WINDOW_PANEL_TITLE, wxID_BEFORE_WINDOW_LOGIN_BUTTON,
 wxID_WINDOW_MIDDLE_BUTTON_FLUSH,
 ] = [wx.NewId() for _init_ctrls in range(24)]

code = "gbk"
version = 1.0


class BeforeFrame(wx.Frame):
    """
    login in 
    """

    def __init__(self, parent):

        self.width = 400
        self.length = 300
        wx.Frame.__init__(self, id=wxID_BEFORE_FRAME, name='', parent=parent,
                          pos=wx.Point((1920 - self.width) / 2, (1080 - self.length) / 2),
                          size=wx.Size(self.width, self.length),
                          style=wx.DEFAULT_FRAME_STYLE, title='login in')
        self.SetClientSize(wx.Size(self.width, self.length))

        self.beforeWindow = wx.SplitterWindow(id=wxID_WINDOW_LEFT,
                                              name='before', parent=self, pos=wx.Point(0, 0),
                                              size=wx.Size(self.width, self.length), style=wx.SP_3D)

        self.windowMiddlePanel = wx.Panel(id=wxID_WINDOW_MIDDLE_PANEL, name="middle", parent=self.beforeWindow,
                                          pos=wx.Point(10, 10),
                                          size=wx.Size((self.width - 20), (self.length - 20)),
                                          style=wx.TAB_TRAVERSAL)

        isFile = os.path.isfile("user_name.txt")
        user_name = "名字的全拼"
        if isFile:
            fo = open("user_name.txt", "r+")
            user_name = fo.read()
            fo.close()

        self.windowMiddlePanelText = wx.richtext.RichTextCtrl(id=wxID_BEFORE_WINDOW_LOGIN_TEXT,
                                                              parent=self.windowMiddlePanel, pos=wx.Point(30, 100),
                                                              size=wx.Size(200, 30),
                                                              style=wx.richtext.RE_MULTILINE, value=user_name)

        self.windowMiddlePanelTitle = wx.StaticText(id=wxID_BEFORE_WINDOW_PANEL_TITLE,
                                                    label="LOGIN IN", name="login in", parent=self.windowMiddlePanel,
                                                    pos=wx.Point(150, 30), size=wx.Size(100, 18), style=0)

        self.loginInButton = wx.Button(id=wxID_BEFORE_WINDOW_LOGIN_BUTTON,
                                       label='登陆', name='login', parent=self.windowMiddlePanel,
                                       pos=wx.Point(250, 100), size=wx.Size(80, 30), style=0)

        self.loginInButton.Bind(wx.EVT_BUTTON, self.onLoginButton, id=wxID_BEFORE_WINDOW_LOGIN_BUTTON)

    def onLoginButton(self, event):
        user_name = self.windowMiddlePanelText.GetValue()
        isFile = os.path.isfile("user_name.txt")
        if not isFile:
            fo = open("user_name.txt", "wb")
            fo.write(user_name)
            fo.close()
        else:
            fo = open("user_name.txt", "w+")
            user_name_old = fo.read()
            if user_name != user_name_old:
                fo.write(user_name)
            fo.close()

        db = MongoDB().db
        user = db.user.find_one({"user": user_name})
        if not user:
            self.windowMiddlePanelTitle.SetLabel("No such user!")
        else:
            self.Close()
            user = user.get(user_name)
            self.main = Frame(None, user.get("user_name"), user.get("real_name"), user.get("user_email"))
            self.main.Show()
        event.Skip()


class Frame(wx.Frame):
    def __init__(self, parent, username, realName, userEmail):
        self.page = 1
        self.total = 0
        self.username = username
        self.realName = realName
        self.userEmail = userEmail
        self._init_ctrls(parent)

    def _init_ctrls(self, prnt):
        self.width = 1920
        self.length = 1080
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME, name='', parent=prnt,
                          pos=wx.Point(0, 0), size=wx.Size(self.width, self.length),
                          style=wx.DEFAULT_FRAME_STYLE, title='看板{0}'.format(version))
        self.SetClientSize(wx.Size(self.width, self.length))

        self.createLeft()
        self.createMiddle()
        self.createRight()

        self.SetTransparent(230)  # 设置透明
        # self.windowLeft.SetTransparent(250)

    def db(self):
        db = MongoDB().db
        return db

    def createLeft(self):
        """
        左边布局
        :return: 
        """

        oper_logs = self.db().oper_log.find({}).sort("create_time",pymongo.DESCENDING).limit(50)

        log_content = LeftView.operLogView(oper_logs)

        self.windowLeft = wx.SplitterWindow(id=wxID_WINDOW_LEFT,
                                            name='left', parent=self, pos=wx.Point(0, 0),
                                            size=wx.Size((self.width * 2) / 9, self.length - 10), style=wx.SP_3D)

        self.windowLeftLogTitle = wx.lib.buttons.GenButton(id=wxID_WINDOW_LEFT_LOG_TITLE,
                                                           label='日志记录', name='notify', parent=self.windowLeft,
                                                           pos=wx.Point(50, 22), size=wx.Size(328, 64), style=0)

        self.windowLeftLog = wx.richtext.RichTextCtrl(id=wxID_WINDOW_LEFT_LOG,
                                                      parent=self.windowLeft, pos=wx.Point(16, 120),
                                                      size=wx.Size(400, self.length - 250),
                                                      style=wx.richtext.RE_MULTILINE,
                                                      value=log_content)

        self.windowLeftUser = wx.StaticText(id=wxID_WINDOW_LEFT_USER,
                                            label='当前操作用户：{0}'.format(self.userEmail), name='genStaticText1',
                                            parent=self,
                                            pos=wx.Point(10, self.length - 100), size=wx.Size(240, 15), style=0)
        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        self.windowLeftUser.SetFont(font)

    def createMiddle(self):
        """
        中间布局
        :return: 
        """
        self.windowMiddle = wx.SplitterWindow(id=wxID_WINDOW_MIDDLE,
                                              name='middle', parent=self, pos=wx.Point((self.width * 2) / 9, 0),
                                              size=wx.Size((self.width * 5) / 9, self.length - 10), style=wx.SP_3D)

        self.createUserContentByPage()

        self.windowMiddleButtonPrev = wx.Button(id=wxID_WINDOW_MIDDLE_BUTTON_PREV, label='上一页',
                                                name='button11', parent=self.windowMiddle,
                                                pos=wx.Point(700, self.length - 100),
                                                size=wx.Size(100, 32), style=0)

        self.windowMiddleButtonNext = wx.Button(id=wxID_WINDOW_MIDDLE_BUTTON_NEXT, label='下一页',
                                                name='button11', parent=self.windowMiddle,
                                                pos=wx.Point(810, self.length - 100),
                                                size=wx.Size(100, 32), style=0)

        self.windowMiddleButtonFlush = wx.Button(id=wxID_WINDOW_MIDDLE_BUTTON_FLUSH, label='刷  新',
                                                 name='button11', parent=self.windowMiddle,
                                                 pos=wx.Point(920, self.length - 100),
                                                 size=wx.Size(100, 32), style=0)

        self.windowMiddleButtonPrev.Bind(wx.EVT_BUTTON, self.onMiddlePreButton, id=wxID_WINDOW_MIDDLE_BUTTON_PREV)
        self.windowMiddleButtonNext.Bind(wx.EVT_BUTTON, self.onMiddleNextButton, id=wxID_WINDOW_MIDDLE_BUTTON_NEXT)
        self.windowMiddleButtonFlush.Bind(wx.EVT_BUTTON, self.onMiddleFlushtButton, id=wxID_WINDOW_MIDDLE_BUTTON_FLUSH)

    def createRight(self):
        """
        右边布局
        :return: 
        """
        user = self.db().user.find_one({"user": self.username})

        self.windowRight = wx.SplitterWindow(id=wxID_WINDOW_RIGHT,
                                             name='right', parent=self, pos=wx.Point(self.width * 7 / 9, 0),
                                             size=wx.Size((self.width * 2) / 9, self.length - 10), style=wx.SP_3D)

        self.windowRightAnalogclock = wx.lib.analogclock.analogclock.AnalogClock(id=wxID_WINDOW_RIGHT_ANALOGCLOCK,
                                                                                 name='analogClock1',
                                                                                 parent=self.windowRight,
                                                                                 pos=wx.Point(10, 16),
                                                                                 size=wx.Size(400, 200),
                                                                                 style=0)

        self.windowRightTaskTitle = wx.TextCtrl(id=wxID_WINDOW_RIGHT_TASK_TITLE,
                                                parent=self.windowRight, pos=wx.Point(10, 230),
                                                size=wx.Size((self.width * 2) / 9 - 20, 40),
                                                style=wx.richtext.RE_MULTILINE,
                                                value='<标题> 正在做的任务和百分比')

        self.windowRightTaskText = wx.TextCtrl(id=wxID_WINDOW_RIGHT_TASK_TEXT,
                                               parent=self.windowRight, pos=wx.Point(10, 280),
                                               size=wx.Size((self.width * 2) / 9 - 20, 270),
                                               style=wx.richtext.RE_MULTILINE,
                                               value='<详细> 几句话概括自己做的事情，大概的进度')

        self.windowRightTaskSubmit = wx.Button(id=wxID_WINDOW_RIGHT_TASK_SUBMIT,
                                               label='点击提交', name='notify', parent=self.windowRight,
                                               pos=wx.Point(50, 560), size=wx.Size(328, 40), style=0)

        self.windowRightTagTitle = wx.lib.buttons.GenButton(id=wxID_WINDOW_RIGHT_TAG_TITLE,
                                                            label='↓ ~记录你还有什么任务~ ↓', name='notify',
                                                            parent=self.windowRight,
                                                            pos=wx.Point(50, 620), size=wx.Size(328, 40), style=0)

        self.windowRightTagText = wx.TextCtrl(id=wxID_WINDOW_RIGHT_TAG_TEXT,
                                              parent=self.windowRight, pos=wx.Point(10, 670),
                                              size=wx.Size(self.width * 2 / 9 - 20, 270),
                                              style=wx.richtext.RE_MULTILINE,
                                              value=user.get(self.username, {}).get("note", {}).get("content", ""))

        self.windowRightTagSubmit = wx.Button(id=wxID_WINDOW_RIGHT_TAG_SUBMIT,
                                              label='保存', name='notify', parent=self.windowRight,
                                              pos=wx.Point(20, self.length - 100), size=wx.Size(150, 40), style=0)

        self.windowRightTagSubmit.Bind(wx.EVT_BUTTON, self.onRightTagSubmitButton, id=wxID_WINDOW_RIGHT_TAG_SUBMIT)
        self.windowRightTaskSubmit.Bind(wx.EVT_BUTTON, self.onRightTaskSubmitButton, id=wxID_WINDOW_RIGHT_TASK_SUBMIT)

    def cleanThePage(self):
        x = 1
        y = 1
        for indx in xrange(9):
            if (indx) % 3 == 0 and indx != 0:
                y = y + 1
                x = 1
            else:
                if indx != 0:
                    x = x + 1
            self.createMiddleItem(x, y, "", str(indx + 1), "")

    def createUserContentByPage(self, page=1):
        """
        根据分页查找的信息来渲染中间用户版块
        :param page: 
        :return: 
        """
        size = 9
        if page <= 1:
            page = 1
        db = self.db()
        users = db.user.find({}).skip((int(page) - 1) * int(size)).limit(int(size))
        if self.total == 0:
            self.total = db.user.find({}).count()
        x = 1
        y = 1
        for indx, user in enumerate(users):

            if (indx) % 3 == 0 and indx != 0:
                y = y + 1
                x = 1
            else:
                if indx != 0:
                    x = x + 1

            content = MiddleView.createUserSummary(user.get(user.get("user")).get("day_summary", []))
            self.createMiddleItem(x, y, user.get(user.get("user")).get("real_name"), str(indx + 1), content)

    def createMiddleItem(self, x, y, lableName, name, content):

        width = 315
        length = self.length / 3.4
        self.windowMiddlePanel = wx.Panel(id=wxID_WINDOW_MIDDLE_PANEL, name=name, parent=self.windowMiddle,
                                          pos=wx.Point(10 + (x - 1) * (width + 5), 10 + (y - 1) * (length + 5)),
                                          size=wx.Size(width, length),
                                          style=wx.TAB_TRAVERSAL)

        self.windowMiddlePanelText = wx.richtext.RichTextCtrl(id=wxID_WINDOW_MIDDLE_PANEL_TEXT,
                                                              parent=self.windowMiddlePanel, pos=wx.Point(20, 30),
                                                              size=wx.Size(width - 40, length - 50),
                                                              style=wx.richtext.RE_MULTILINE, value=content)

        self.windowMiddlePanelTitle = wx.StaticText(id=wxID_WINDOW_MIDDLE_PANEL_TITLE,
                                                    label=lableName, name=name, parent=self.windowMiddlePanel,
                                                    pos=wx.Point(120, 10), size=wx.Size(100, 18), style=0)

    def onMiddlePreButton(self, event):

        self.cleanThePage()
        if self.page - 1 <= 1:
            self.page = 1
        else:
            self.page = self.page - 1
        self.createUserContentByPage(self.page)
        print ("pre page")
        event.Skip()

    def onMiddleNextButton(self, event):

        self.cleanThePage()
        size = 9
        if (self.page * size) < self.total:
            self.page = self.page + 1

        self.createUserContentByPage(self.page)
        print ("next page")
        event.Skip()

    def onRightTagSubmitButton(self, event):
        note = {"update_time": time.time(), "content": self.windowRightTagText.GetValue()}
        self.db().user.update({"user": self.username}, {"$set": {"{0}.note".format(self.username): note}})
        event.Skip()

    def onRightTaskSubmitButton(self, event):
        now = time.time()
        day_summary = {"create_time": now, "content": self.windowRightTaskText.GetValue(),
                       "title": self.windowRightTaskTitle.GetValue()}
        self.db().user.update({"user": self.username},
                              {"$push": {"{0}.day_summary".format(self.username): day_summary}})

        log = {"create_time": now, "user_name": self.realName, "title": self.windowRightTaskTitle.GetValue()}
        self.db().oper_log.insert(log)

        logs = self.db().oper_log.find({}).sort("create_time",pymongo.DESCENDING).limit(50)
        self.windowLeftLog.SetValue(LeftView.operLogView(logs))

        self.createUserContentByPage(self.page)

        event.Skip()

    def onMiddleFlushtButton(self, event):
        # self.windowMiddle.Close()
        # self.createUserContentByPage(self.page)
        #
        # logs = self.db().oper_log.find({}).sort("create_time",pymongo.DESCENDING).limit(50)
        # self.windowLeftLog.SetValue(LeftView.operLogView(logs))
        username = self.username
        realName = self.realName
        userEmail = self.userEmail

        self.Close()

        self.main = Frame(None, username ,realName, userEmail)
        self.main.Show()

        event.Skip()


class LeftView(object):
    @staticmethod
    def operLogView(oper_logs):
        # oper_logs = sorted(oper_logs, key=lambda x: time.mktime(x.get("create_time").timetuple()), reverse=True)
        logs = []

        for log in oper_logs:
            timeArray = time.localtime(log.get("create_time"))
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            log_string = "[" + otherStyleTime + "] " + log.get("user_name", "") + " 【添加】 ".decode(code) + log.get("title", "")
            logs.append(log_string)

        return "\n".join(logs)


class MiddleView(object):
    @staticmethod
    def createUserSummary(daySummarys):
        import time
        daySummarys = sorted(daySummarys, key=lambda x: x.get("create_time"), reverse=True)
        contents = []
        for index, summary in enumerate(daySummarys):
            if index >= 3: break

            timeArray = time.localtime(summary.get("create_time"))
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            content = "-------------------------"
            content = content + "\n[title]-->" + summary.get(
                "title") + "\n[time]-->" + otherStyleTime + "\n[content]-->" + summary.get("content") + "\n"
            contents.append(content)

        return "".join(contents)


if __name__ == '__main__':
    import datetime

    L = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
    print L
    L = sorted(L, cmp=lambda x, y: cmp(x[1], y[1]))

    # L.sort(cmp=lambda x, y: cmp(x[1], y[1]))

    print L
    # import time
    # print time.time()
    # print time.mktime(datetime.datetime.now().timetuple())
