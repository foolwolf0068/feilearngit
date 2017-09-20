#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:39:26 2017
小甲鱼视频 35 easygui
@author: foolwolf0068
"""

from easygui import *
from random import randint
import sys

def main():
    while True:
        Title = "EasyGUi Game"
        msgbox(msg='嗨，欢迎来到飞哥写的第一个界面小游戏^_^',
                     title=Title, ok_button='OK', image=None, root=None)    
        msgbox("请点击OK来开始游戏")
        number = randint(0,10)
        num = enterbox(msg='不妨猜一下飞哥心中想的数字（0-10）.',
                 title='EasyGUi Game', default='', strip=True, image=None, root=None)
    
        while True:
            num1 = int(num)
            if num1 == number:
                msg1 = "你真厉害，你猜对了！！！"
                Title1 = "请选择"
                if ccbox(msg1, Title1):     # show a Continue/Cancel dialog
                        break  # user chose Continue
                else:
                        break     # user chose Cancel
            elif num1 < number :
                msg1 = "猜错了哟！往大了猜..."
            else :
                msg1 = "猜错了哟！往小了猜..."
            num = enterbox(msg=msg1, title='EasyGUi Game')
        msg1 = "你希望继续小游戏吗？"
        title1 = "请选择"
        if ccbox(msg1, title1):     # show a Continue/Cancel dialog
                pass  # user chose Continue
        else:
                sys.exit(0)     # user chose Cancel

if __name__ == "__main__":
    main()    