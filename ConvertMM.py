#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 30, 2019 03:32:14 PM PST  platform: Windows NT

import sys
import os

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import ConvertMM_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    ConvertMM_support.set_Tk_var()
    top = Toplevel1 (root)
    ConvertMM_support.init(root, top)
    root.mainloop()


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#000000'  # X11 color: 'black'
        _fgcolor = '#838383'  # Closest X11 color: 'gray51'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font19 = "-family Consolas -size 16 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font20 = "-family {Courier New} -size 16 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("213x133+905+93")
        top.minsize(350, 1)
        top.maxsize(3844, 1061)
        top.resizable(1, 1)
        top.title("Gimme Inches")
        top.iconbitmap(resource_path('mmicon.ICO'))
        top.configure(background="#000000")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.15, rely=0.35,height=40, relwidth=0.7)
        self.Entry1.focus_set()
        self.Entry1.configure(background="#000000")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font20)
        self.Entry1.configure(foreground="#999999")
        self.Entry1.configure(highlightbackground="#730e8c")
        self.Entry1.configure(insertbackground="#730e8c")
        self.Entry1.configure(justify='center')
        self.Entry1.configure(textvariable=ConvertMM_support.inputVAR)
        self.Entry1.bind('<Return>', ConvertMM_support.enter)

        # self.Button1 = tk.Button(top)
        # self.Button1.place(relx=0.15, rely=0.526, height=40, width=149)
        # self.Button1.configure(activebackground="#730e8c")
        # self.Button1.configure(activeforeground="white")
        # self.Button1.configure(activeforeground="#838383")
        # self.Button1.configure(background="#000000")
        # self.Button1.configure(command=ConvertMM_support.gimmeInches)
        # self.Button1.configure(disabledforeground="#a3a3a3")
        # self.Button1.configure(font=font19)
        # self.Button1.configure(foreground="#838383")
        # self.Button1.configure(highlightbackground="#000000")
        # self.Button1.configure(highlightcolor="black")
        # self.Button1.configure(pady="0")
        # self.Button1.configure(text='''Gimme Inches''')

if __name__ == '__main__':
    vp_start_gui()





