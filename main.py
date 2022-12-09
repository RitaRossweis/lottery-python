# coding=utf-8
import sys
import os
from base import *

import tkinter as tk
from tkinter import *

import random


r = range(1, 1000)
data = list(r)
going = True
is_run = False
mode = 1


def lottery_roll(var1):
    global going, mode
    show_member1 = random.choice(data)
    show_member2 = random.choice(data)
    show_member3 = random.choice(data)
    show_member4 = random.choice(data)
    show_member5 = random.choice(data)
    show_member6 = random.choice(data)
    members = [show_member1, show_member2, show_member3, show_member4, show_member5, show_member6]
    if norepeat(members):
        if mode == 3:
            show_member = [show_member1, show_member2, show_member3, show_member4, show_member5, show_member6]
            var1.set('{}\t{}\t{}\n{}\t{}\t{}\n\n'.format(*show_member))
        elif mode == 2:
            show_member = [show_member1, show_member2]
            var1.set('{}\t{}\n\n\n'.format(*show_member))
        elif mode == 1:
            var1.set('{}\n\n\n'.format(show_member1))

    if going:
        window.after(50, lottery_roll, var1)
    else:
        going = True
        return


def lottery_start(var1):
    global is_run
    if is_run:
        return
    is_run = True
    lottery_roll(var1)


def lottery_end():
    global going, is_run
    if is_run:
        going = False
        is_run = False


def norepeat(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return False
    return True


def lottery_mode3():
    global mode, var1
    mode = 3
    button3.config(bg='#FFD700', fg='#913239')
    button4.config(bg='#913239', fg='#FFD700')
    button5.config(bg='#913239', fg='#FFD700')
    button6.config(bg='#913239', fg='#FFD700')
    button7.config(bg='#913239', fg='#FFD700')


def lottery_mode2():
    global mode, var1
    mode = 2
    button3.config(bg='#913239', fg='#FFD700')
    button4.config(bg='#FFD700', fg='#913239')
    button5.config(bg='#913239', fg='#FFD700')
    button6.config(bg='#913239', fg='#FFD700')
    button7.config(bg='#913239', fg='#FFD700')


def lottery_mode1():
    global mode, var1
    mode = 1
    button3.config(bg='#913239', fg='#FFD700')
    button4.config(bg='#913239', fg='#FFD700')
    button5.config(bg='#FFD700', fg='#913239')
    button6.config(bg='#913239', fg='#FFD700')
    button7.config(bg='#913239', fg='#FFD700')


def lottery_mode0():
    global mode, var1
    mode = 1
    button3.config(bg='#913239', fg='#FFD700')
    button4.config(bg='#913239', fg='#FFD700')
    button5.config(bg='#913239', fg='#FFD700')
    button6.config(bg='#FFD700', fg='#913239')
    button7.config(bg='#913239', fg='#FFD700')


def lottery_mode_re():
    global mode, var1
    mode = 1
    button3.config(bg='#913239', fg='#FFD700')
    button4.config(bg='#913239', fg='#FFD700')
    button5.config(bg='#913239', fg='#FFD700')
    button6.config(bg='#913239', fg='#FFD700')
    button7.config(bg='#FFD700', fg='#913239')


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('1553x867+200+50')
    window.title('                                                                                                                                                                2022年电子科学与工程学院迎新晚会抽奖系统')

    tmd = os.path.join(application_path, './1.png')

    photo1 = tk.PhotoImage(file=tmd)

# 数字滚动区域
    var1 = StringVar(value='即 将 开 始\n\n\n')

    show_label1 = Label(window,  textvariable=var1, justify='left', anchor=CENTER, width=1553, height=867, bg='#02070D',
                        image=photo1, compound=CENTER, bd=0,
                        font='阿里巴巴普惠 -60 bold', foreground='#FFD700')
    show_label1.place(anchor=NW, x=0, y=0)

    button1 = Button(window, text='开始', command=lambda: lottery_start(var1), width=20, height=3, bg='#913239',
                     font='微软雅黑 -18 bold', fg='#FFD700')
    button1.place(anchor=NW, x=1232, y=300)

    button2 = Button(window, text='结束', command=lambda: lottery_end(), width=20, height=3, bg='#913239',
                     font='微软雅黑 -18 bold', fg='#FFD700')
    button2.place(anchor=NW, x=1232, y=420)

    button3 = Button(window, text='三等奖', command=lambda: lottery_mode3(), width=8, height=2, bg='#913239',
                     font='微软雅黑 -18 bold', fg='#FFD700')
    button3.place(anchor=NW, x=1232, y=100)

    button4 = Button(window, text='二等奖', command=lambda: lottery_mode2(), width=8, height=2, bg='#913239',
                     font='微软雅黑 -18 bold', fg='#FFD700')
    button4.place(anchor=NW, x=1376, y=100)

    button5 = Button(window, text='一等奖', command=lambda: lottery_mode1(), width=8, height=2, bg='#913239',
                     font='微软雅黑 -18 bold', fg='#FFD700')
    button5.place(anchor=NW, x=1232, y=200)

    button6 = Button(window, text='特等奖', command=lambda: lottery_mode0(), width=8, height=2, bg='#913239',
                     font='微软雅黑 -18 bold', fg='#FFD700')
    button6.place(anchor=NW, x=1376, y=200)

    button7 = Button(window, text='补抽', command=lambda: lottery_mode_re(), width=8, height=2, bg='#913239',
                     font='微软雅黑 -18 bold', fg='#FFD700')
    button7.place(anchor=NW, x=1302, y=540)

    window.mainloop()

