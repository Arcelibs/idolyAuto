# -*- encoding=utf8 -*-
__author__ = "jimmy"
from airtest.core.api import *
import random
auto_setup(__file__)

count = 0  # 計數器

while True:  # 無限迴圈
    # 直接選最新的歌曲
    touch(Template(r"tpl1688023425085.png", record_pos=(0.353, 0.689), resolution=(720, 1280)))
    sleep(5)

    if exists(Template(r"tpl1688025813623.png", record_pos=(-0.265, 0.633), resolution=(720, 1280))):
        touch(Template(r"tpl1688025823554.png", record_pos=(-0.274, 0.632), resolution=(720, 1280)))
    sleep(5)

    if exists(Template(r"tpl1688025840441.png", record_pos=(0.344, 0.689), resolution=(720, 1280))):
        touch(Template(r"tpl1688025846359.png", record_pos=(0.34, 0.693), resolution=(720, 1280)))

    sleep(60)
    #如果NEXT了就點他，不然繼續等
    if exists(Template(r"tpl1688026467926.png", record_pos=(0.253, 0.792), resolution=(720, 1280))):
        touch(Template(r"tpl1688026486986.png", record_pos=(0.246, 0.797), resolution=(720, 1280)))

    sleep(5)

    #如果終了就點他
    if exists(Template(r"tpl1688026591845.png", record_pos=(0.351, 0.685), resolution=(720, 1280))):
        touch(Template(r"tpl1688026602111.png", record_pos=(0.35, 0.686), resolution=(720, 1280)))

    sleep(5)

    count += 1  # 執行次數加1

    if count >= 100:  # 執行100次後終止迴圈
        break
