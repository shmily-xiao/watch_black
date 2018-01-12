#!/usr/bin/python
# -*- coding: utf-8 -*-

# absolute.py

import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
                                      size=(300, 250))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI1(self):
        # panel = wx.Panel(self, -1)

        menubar = wx.MenuBar()
        filem = wx.Menu()
        editm = wx.Menu()
        helpm = wx.Menu()

        menubar.Append(filem, '&File')
        menubar.Append(editm, '&Edit')
        menubar.Append(helpm, '&Help')
        self.SetMenuBar(menubar)

        # wx.TextCtrl(panel, pos=(3, 3), size=(250, 150))
        wx.TextCtrl(self)

        # panel = wx.Panel(self)
        #
        # panel.SetBackgroundColour('#4f5049')
        # vbox = wx.BoxSizer(wx.VERTICAL)
        #
        # midPan = wx.Panel(panel)
        # midPan.SetBackgroundColour('#ededed')
        #
        # vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20)
        # panel.SetSizer(vbox)

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
        gs = wx.GridSizer(5, 4, 5, 5)

        gs.AddMany([(wx.Button(self, label='Cls'), 0, wx.EXPAND),
                    (wx.Button(self, label='Bck'), 0, wx.EXPAND),
                    (wx.StaticText(self), wx.EXPAND),
                    (wx.Button(self, label='Close'), 0, wx.EXPAND),
                    (wx.Button(self, label='7'), 0, wx.EXPAND),
                    (wx.Button(self, label='8'), 0, wx.EXPAND),
                    (wx.Button(self, label='9'), 0, wx.EXPAND),
                    (wx.Button(self, label='/'), 0, wx.EXPAND),
                    (wx.Button(self, label='4'), 0, wx.EXPAND),
                    (wx.Button(self, label='5'), 0, wx.EXPAND),
                    (wx.Button(self, label='6'), 0, wx.EXPAND),
                    (wx.Button(self, label='*'), 0, wx.EXPAND),
                    (wx.Button(self, label='1'), 0, wx.EXPAND),
                    (wx.Button(self, label='2'), 0, wx.EXPAND),
                    (wx.Button(self, label='3'), 0, wx.EXPAND),
                    (wx.Button(self, label='-'), 0, wx.EXPAND),
                    (wx.Button(self, label='0'), 0, wx.EXPAND),
                    (wx.Button(self, label='.'), 0, wx.EXPAND),
                    (wx.Button(self, label='='), 0, wx.EXPAND),
                    (wx.Button(self, label='+'), 0, wx.EXPAND)])

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='')
    app.MainLoop()