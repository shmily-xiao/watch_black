#!/usr/bin/env python

# simple.py

import  wx

app = wx.App()

frame = wx.Frame(None, style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION |	 wx.CLOSE_BOX)
# frame2 = wx.Frame(None, -1, 'simple2.py')
frame.Show()
# frame2.Show()

app.MainLoop()