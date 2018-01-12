# wxCalc1 a simple GUI calculator using wxPython
# created with the Boa Constructor which generates all the GUI components
# all I had to do is add some code for each button click event
# Boa free from: http://boa-constructor.sourceforge.net/
# note that  boa-constructor-0.3.1.win32.exe
# still uses  wxPythonWIN32-2.4.2.4-Py23.exe
# but is expected to work with wxPython version 2.5 soon
# tested with Python23  vegaseat  26feb2005
from wxPython.wx import *

# some Boa generated global IDs ...
[wxID_WXFRAME1, wxID_WXFRAME1BTN0, wxID_WXFRAME1BTN1, wxID_WXFRAME1BTN2,
 wxID_WXFRAME1BTN3, wxID_WXFRAME1BTN4, wxID_WXFRAME1BTN5, wxID_WXFRAME1BTN6,
 wxID_WXFRAME1BTN7, wxID_WXFRAME1BTN8, wxID_WXFRAME1BTN9,
 wxID_WXFRAME1BTNCLEAR, wxID_WXFRAME1BTNDIV, wxID_WXFRAME1BTNDOT,
 wxID_WXFRAME1BTNEQUAL, wxID_WXFRAME1BTNMINUS, wxID_WXFRAME1BTNMULTI,
 wxID_WXFRAME1BTNPLUS, wxID_WXFRAME1EDIT,
 ] = map(lambda _init_ctrls: wxNewId(), range(19))


class wxFrame1(wxFrame):
    # startregion, below this marker is Boa generated code do not edit!!!
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxFrame.__init__(self, id=wxID_WXFRAME1, name='', parent=prnt,
                         pos=wxPoint(306, 270), size=wxSize(266, 265),
                         style=wxDEFAULT_FRAME_STYLE, title='Calculator1')
        self.SetClientSize(wxSize(258, 225))
        self.SetBackgroundColour(wxColour(0, 128, 0))
        self.btn1 = wxButton(id=wxID_WXFRAME1BTN1, label='1', name='btn1',
                             parent=self, pos=wxPoint(16, 136), size=wxSize(32, 32), style=0)
        EVT_BUTTON(self.btn1, wxID_WXFRAME1BTN1, self.OnBtn1Button)
        self.btn2 = wxButton(id=wxID_WXFRAME1BTN2, label='2', name='btn2',
                             parent=sekklf, pos=wxPoint(64, 136), size=wxSize(32, 32), style=0)
        EVT_BUTTON(self.btn2, wxID_WXFRAME1BTN2, self.OnBtn2Button)
        self.btn3 = wxButton(id=wxID_WXFRAME1BTN3, label='3', name='btn3',
                             parent=self, pos=wxPoint(112, 136), size=wxSize(32, 32), style=0)
        EVT_BUTTON(self.btn3, wxID_WXFRAME1BTN3, self.OnBtn3Button)
        self.btn4 = wxButton(id=wxID_WXFRAME1BTN4, label='4', name='btn4',
                             parent=self, pos=wxPoint(16, 96), size=wxSize(32, 32), style=0)
        EVT_BUTTON(self.btn4, wxID_WXFRAME1BTN4, self.OnBtn4Button)
        self.btn5 = wxButton(id=wxID_WXFRAME1BTN5, label='5', name='btn5',
                             parent=self, pos=wxPoint(64, 96), size=wxSize(32, 32), style=0)
        EVT_BUTTON(self.btn5, wxID_WXFRAME1BTN5, self.OnBtn5Button)
        self.btn6 = wxButton(id=wxID_WXFRAME1BTN6, label='6', name='btn6',
                             parent=self, pos=wxPoint(112, 96), size=wxSize(32, 32), style=0)
        EVT_BUTTON(self.btn6, wxID_WXFRAME1BTN6, self.OnBtn6Button)
        self.btn7 = wxButton(id=wxID_WXFRAME1BTN7, label='7', name='btn7',
                             parent=self, pos=wxPoint(16, 56), size=wxSize(32, 32), style=0)
        EVT_BUTTON(self.btn7, wxID_WXFRAME1BTN7, self.OnBtn7Button)
        self.btn8 = wxButton(id=wxID_WXFRAME1BTN8, label='8', name='btn8',
                             parent=self, pos=wxPoint(64, 56), size=wxSize(32, 32), style=0)
        EVT_BUTTON(self.btn8, wxID_WXFRAME1BTN8, self.OnBtn8Button)
        self.btn9 = wxButton(id=wxID_WXFRAME1BTN9, label='9', name='btn9',
                             parent=self, pos=wxPoint(112, 56), size=wxSize(32, 32), style=0)
        EVT_BUTTON(self.btn9, wxID_WXFRAME1BTN9, self.OnBtn9Button)
        self.btn0 = wxButton(id=wxID_WXFRAME1BTN0, label='0', name='btn0',
                             parent=self, pos=wxPoint(16, 176), size=wxSize(32, 32), style=0)
        EVT_BUTTON(self.btn0, wxID_WXFRAME1BTN0, self.OnBtn0Button)
        self.btnDot = wxButton(id=wxID_WXFRAME1BTNDOT, label='.', name='btnDot',
                               parent=self, pos=wxPoint(64, 176), size=wxSize(32, 32), style=0)
        EVT_BUTTON(self.btnDot, wxID_WXFRAME1BTNDOT, self.OnBtnDotButton)
        self.btnEqual = wxButton(id=wxID_WXFRAME1BTNEQUAL, label='=',
                                 name='btnEqual', parent=self, pos=wxPoint(112, 176),
                                 size=wxSize(32, 32), style=0)
        EVT_BUTTON(self.btnEqual, wxID_WXFRAME1BTNEQUAL, self.OnBtnEqualButton)
        self.edit = wxTextCtrl(id=wxID_WXFRAME1EDIT, name='edit', parent=self,
                               pos=wxPoint(16, 16), size=wxSize(224, 24), style=0, value='')
        self.btnPlus = wxButton(id=wxID_WXFRAME1BTNPLUS, label='+',
                                name='btnPlus', parent=self, pos=wxPoint(160, 56), size=wxSize(32,
                                                                                               32), style=0)
        EVT_BUTTON(self.btnPlus, wxID_WXFRAME1BTNPLUS, self.OnBtnPlusButton)
        self.btnMinus = wxButton(id=wxID_WXFRAME1BTNMINUS, label='-',
                                 name='btnMinus', parent=self, pos=wxPoint(160, 96),
                                 size=wxSize(32, 32), style=0)
        EVT_BUTTON(self.btnMinus, wxID_WXFRAME1BTNMINUS, self.OnBtnMinusButton)
        self.btnMulti = wxButton(id=wxID_WXFRAME1BTNMULTI, label='*',
                                 name='btnMulti', parent=self, pos=wxPoint(160, 136),
                                 size=wxSize(32, 32), style=0)
        EVT_BUTTON(self.btnMulti, wxID_WXFRAME1BTNMULTI, self.OnBtnMultiButton)
        self.btnDiv = wxButton(id=wxID_WXFRAME1BTNDIV, label='/', name='btnDiv',
                               parent=self, pos=wxPoint(160, 176), size=wxSize(32, 32), style=0)
        EVT_BUTTON(self.btnDiv, wxID_WXFRAME1BTNDIV, self.OnBtnDivButton)
        self.btnClear = wxButton(id=wxID_WXFRAME1BTNCLEAR, label='C',
                                 name='btnClear', parent=self, pos=wxPoint(208, 56),
                                 size=wxSize(32, 32), style=0)
        self.btnClear.SetToolTipString('btnClear')
        EVT_BUTTON(self.btnClear, wxID_WXFRAME1BTNCLEAR, self.OnBtnClearButton)

    def __init__(self, parent):
        self._init_ctrls(parent)

    # endregion, above this marker is Boa generated code, do not edit!!!
    # now respond to all the button click events ...
    def OnBtn0Button(self, event):
        val = '0'
        # get existing edit box text
        txt = self.edit.GetValue()
        # append text
        txt = txt + val
        # update edit box text
        self.edit.SetValue(txt)

    def OnBtn1Button(self, event):
        val = '1'
        txt = self.edit.GetValue()
        txt = txt + val
        self.edit.SetValue(txt)

    def OnBtn2Button(self, event):
        val = '2'
        txt = self.edit.GetValue()
        txt = txt + val
        self.edit.SetValue(txt)

    def OnBtn3Button(self, event):
        val = '3'
        txt = self.edit.GetValue()
        txt = txt + val
        self.edit.SetValue(txt)

    def OnBtn4Button(self, event):
        val = '4'
        txt = self.edit.GetValue()
        txt = txt + val
        self.edit.SetValue(txt)

    def OnBtn5Button(self, event):
        val = '5'
        txt = self.edit.GetValue()
        txt = txt + val
        self.edit.SetValue(txt)

    def OnBtn6Button(self, event):
        val = '6'
        txt = self.edit.GetValue()
        txt = txt + val
        self.edit.SetValue(txt)

    def OnBtn7Button(self, event):
        val = '7'
        txt = self.edit.GetValue()
        txt = txt + val
        self.edit.SetValue(txt)

    def OnBtn8Button(self, event):
        val = '8'
        txt = self.edit.GetValue()
        txt = txt + val
        self.edit.SetValue(txt)

    def OnBtn9Button(self, event):
        val = '9'
        txt = self.edit.GetValue()
        txt = txt + val
        self.edit.SetValue(txt)

    def OnBtnDotButton(self, event):
        val = '.'
        txt = self.edit.GetValue()
        txt = txt + val
        self.edit.SetValue(txt)

    def OnBtnEqualButton(self, event):
        txt = self.edit.GetValue()
        # needs to contain a float so eg. 3/5 is 3/5.0
        # otherwise division 3/5 would result in zero
        if '/' in txt:
            if '.' not in txt:
                txt = txt + '.0'
        # now evaluate the math string
        txt = repr(eval(txt))
        # and show result in edit box
        self.edit.SetValue(txt)

    def OnBtnPlusButton(self, event):
        val = '+'
        txt = self.edit.GetValue()
        txt = txt + val
        self.edit.SetValue(txt)

    def OnBtnMinusButton(self, event):
        val = '-'
        txt = self.edit.GetValue()
        txt = txt + val
        self.edit.SetValue(txt)

    def OnBtnMultiButton(self, event):
        val = '*'
        txt = self.edit.GetValue()
        txt = txt + val
        self.edit.SetValue(txt)

    def OnBtnDivButton(self, event):
        val = '/'
        txt = self.edit.GetValue()
        txt = txt + val
        self.edit.SetValue(txt)

    def OnBtnClearButton(self, event):
        self.edit.SetValue('')


# -------------------- end of class wxFrame1 ----------------------
def create(parent):
    return wxFrame1(parent)


class BoaApp(wxApp):
    def OnInit(self):
        wxInitAllImageHandlers()
        self.main = create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True


def main():
    application = BoaApp(0)
    application.MainLoop()


if __name__ == '__main__':
    main()