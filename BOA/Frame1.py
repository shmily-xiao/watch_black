#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Boa:Frame:Frame1

import wx
import wx.lib.buttons
import wx.lib.analogclock
import wx.richtext

def create(parent):
    return Frame1(parent)

[wxID_FRAME, wxID_WINDOW_LEFT,wxID_WINDOW_LEFT_LOG_TITLE,wxID_WINDOW_LEFT_LOG,
wxID_WINDOW_LEFT_USER,wxID_WINDOW_MIDDLE,wxID_WINDOW_MIDDLE_BUTTON_PREV,
wxID_WINDOW_MIDDLE_BUTTON_NEXT,wxID_WINDOW_MIDDLE_PANEL,wxID_WINDOW_MIDDLE_PANEL_TEXT,
wxID_WINDOW_MIDDLE_PANEL_TITLE,wxID_WINDOW_RIGHT,wxID_WINDOW_RIGHT_ANALOGCLOCK,
wxID_WINDOW_RIGHT_TASK_TITLE,wxID_WINDOW_RIGHT_TASK_TEXT,wxID_WINDOW_RIGHT_TASK_SUBMIT,
wxID_WINDOW_RIGHT_TAG_TITLE,wxID_WINDOW_RIGHT_TAG_TEXT,wxID_WINDOW_RIGHT_TAG_SUBMIT
] = [wx.NewId() for _init_ctrls in range(19)]
class Frame1(wx.Frame):

    def __init__(self, parent):
        self._init_ctrls(parent)

    def _init_ctrls(self, prnt):
        self.width = 1920
        self.length = 1080
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME, name='', parent=prnt,
              pos=wx.Point(-8, -8), size=wx.Size(self.width, self.length),
              style=wx.DEFAULT_FRAME_STYLE, title='看板')
        self.SetClientSize(wx.Size(self.width, self.length))

        self.createLeft()
        self.createMiddle()
        self.createRight()

        self.SetTransparent(150)  # 设置透明
        # self.windowLeft.SetTransparent(250)


    def createLeft(self):
        """
        左边布局
        :return: 
        """
        self.windowLeft = wx.SplitterWindow(id=wxID_WINDOW_LEFT,
                                                 name='left', parent=self, pos=wx.Point(0, 0),
                                                 size=wx.Size((self.width*2)/9, self.length-10), style=wx.SP_3D)

        self.windowLeftLogTitle = wx.lib.buttons.GenButton(id=wxID_WINDOW_LEFT_LOG_TITLE,
                                                   label='日志记录', name='notify', parent=self.windowLeft,
                                                   pos=wx.Point(50, 22), size=wx.Size(328, 64), style=0)

        self.windowLeftLog = wx.richtext.RichTextCtrl(id=wxID_WINDOW_LEFT_LOG,
                                                      parent=self.windowLeft, pos=wx.Point(16, 120),
                                                      size=wx.Size(400, self.length-250), style=wx.richtext.RE_MULTILINE,
                                                      value='notify')

        self.windowLeftUser = wx.StaticText(id=wxID_WINDOW_LEFT_USER,
                                                            label='当前操作用户：wangzaijun@360.cn', name='genStaticText1', parent=self,
                                                            pos=wx.Point(10, self.length-100), size=wx.Size(240, 15), style=0)
        font = wx.Font(18, wx.ROMAN, wx.ITALIC , wx.NORMAL)
        self.windowLeftUser.SetFont(font)


    def createMiddle(self):
        """
        中间布局
        :return: 
        """
        self.windowMiddle = wx.SplitterWindow(id=wxID_WINDOW_MIDDLE,
                                                 name='middle', parent=self, pos=wx.Point((self.width*2)/9, 0),
                                                 size=wx.Size((self.width * 5)/9, self.length-10), style=wx.SP_3D)

        self.createMiddleItem(1,1,"Test11","1")
        self.createMiddleItem(2,1,"Test21","2")
        self.createMiddleItem(3,1,"Test31","3")
        self.createMiddleItem(1,2,"Test21","4")
        self.createMiddleItem(2,2,"Test22","5")
        self.createMiddleItem(3,2,"Test23","6")
        self.createMiddleItem(1,3,"Test31","7")
        self.createMiddleItem(2,3,"Test32","8")
        self.createMiddleItem(3,3,"Test33","9")


        self.windowMiddleButtonPrev = wx.Button(id=wxID_WINDOW_MIDDLE_BUTTON_PREV, label='上一页',
                                  name='button11', parent=self.windowMiddle, pos=wx.Point(700, self.length-100),
                                  size=wx.Size(100, 32), style=0)

        self.windowMiddleButtonNext = wx.Button(id=wxID_WINDOW_MIDDLE_BUTTON_NEXT, label='下一页',
                                  name='button11', parent=self.windowMiddle, pos=wx.Point(810, self.length-100),
                                  size=wx.Size(100, 32), style=0)


    def  createMiddleItem(self, x,y, lableName, name):

        width = 315
        length = self.length/3.4
        self.windowMiddlePanel = wx.Panel(id=wxID_WINDOW_MIDDLE_PANEL, name=name, parent=self.windowMiddle,
                               pos=wx.Point(10 + (x-1) * (width+5), 10+(y-1) * (length+5)), size=wx.Size(width, length),
                               style=wx.TAB_TRAVERSAL)

        content = """爱已无法回答所有的问题\nBABY\n1:30的我在回家的路上\n旅客名单没你的名字\n我想你已经做了最后决定\n哦 我已失去你\nBABY BABY BABY BABY BABY BABY"""
        self.windowMiddlePanelText = wx.richtext.RichTextCtrl(id=wxID_WINDOW_MIDDLE_PANEL_TEXT,
                                                      parent=self.windowMiddlePanel, pos=wx.Point(20, 30), size=wx.Size(width-40, length-50),
                                                      style=wx.richtext.RE_MULTILINE, value=content)

        self.windowMiddlePanelTitle = wx.StaticText(id=wxID_WINDOW_MIDDLE_PANEL_TITLE,
                                         label= lableName, name=name, parent=self.windowMiddlePanel,
                                         pos=wx.Point(104, 10), size=wx.Size(100, 18), style=0)

    def createRight(self):
        """
        右边布局
        :return: 
        """
        self.windowRight = wx.SplitterWindow(id=wxID_WINDOW_RIGHT,
                                                 name='right', parent=self, pos=wx.Point(self.width * 7 / 9, 0),
                                                 size=wx.Size((self.width*2)/9, self.length-10), style=wx.SP_3D)

        self.windowRightAnalogclock = wx.lib.analogclock.analogclock.AnalogClock(id=wxID_WINDOW_RIGHT_ANALOGCLOCK,
                                                                       name='analogClock1', parent=self.windowRight,
                                                                       pos=wx.Point(10,16), size=wx.Size(400, 200),
                                                                       style=0)

        self.windowRightTaskTitle = wx.TextCtrl(id=wxID_WINDOW_RIGHT_TASK_TITLE,
                                                      parent=self.windowRight, pos=wx.Point(10, 230),
                                                      size=wx.Size((self.width*2)/9-20, 40),style=wx.richtext.RE_MULTILINE,
                                                      value='<标题> 正在做的任务和百分比')

        self.windowRightTaskText = wx.TextCtrl(id=wxID_WINDOW_RIGHT_TASK_TEXT,
                                                      parent=self.windowRight, pos=wx.Point(10, 280),
                                                      size=wx.Size((self.width*2)/9 -20, 270), style=wx.richtext.RE_MULTILINE,
                                                      value='<详细> 几句话概括自己做的事情，大概的进度')

        self.windowRightTaskSubmit = wx.Button(id=wxID_WINDOW_RIGHT_TASK_SUBMIT,
                                                   label='点击提交', name='notify', parent=self.windowRight,
                                                   pos=wx.Point(50, 560), size=wx.Size(328, 40), style=0)

        self.windowRightTagTitle = wx.lib.buttons.GenButton(id=wxID_WINDOW_RIGHT_TAG_TITLE,
                                                   label='↓ ~记录你还有什么任务~ ↓', name='notify', parent=self.windowRight,
                                                   pos=wx.Point(50, 620), size=wx.Size(328, 40), style=0)

        self.windowRightTagText = wx.TextCtrl(id=wxID_WINDOW_RIGHT_TAG_TEXT,
                                                      parent=self.windowRight, pos=wx.Point(10, 670),
                                                      size=wx.Size(self.width * 2 / 9 - 20, 270),
                                                      style=wx.richtext.RE_MULTILINE,
                                                      value='记录你还有什么任务要做，把容易忘记的写在这里，保存之后才会存入数据库中')

        self.windowRightTagSubmit = wx.Button(id=wxID_WINDOW_RIGHT_TAG_SUBMIT,
                                                   label='保存', name='notify', parent=self.windowRight,
                                                   pos=wx.Point(20, self.length-100), size=wx.Size(150, 40), style=0)

        self.windowRightTagSubmit.Bind(wx.EVT_BUTTON, self.onRightTagSubmitButton, id = wxID_WINDOW_RIGHT_TAG_SUBMIT)



    def onRightTagSubmitButton(self, event):
        print ("my submit")
        event.Skip()

    def OnGenBitmapTextToggleButton1Button(self, event):
        event.Skip()
