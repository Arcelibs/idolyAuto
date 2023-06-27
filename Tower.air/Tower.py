# -*- encoding=utf8 -*-
__author__ = "arcelibs"
from airtest.core.api import *
auto_setup(__file__)
count = 0
q = 0
while(count < 100):
    while not exists(Template(r"tpl1687758518301.png", threshold=0.8)):
        sleep(3)
    touch(Template(r"tpl1687758518301.png", record_pos=(0.328, 0.676), resolution=(720, 1280)))
    sleep(5)
    #while not exists(Template(r"tpl1687758526090.png", threshold=0.8)):
    touch(Template(r"tpl1687758526090.png", record_pos=(0.332, 0.026), resolution=(720, 1280)))
    sleep(3)
    while not exists(Template(r"tpl1687758531043.png", threshold=0.8)):
        sleep(3)
    touch(Template(r"tpl1687758531043.png", record_pos=(0.328, 0.699), resolution=(720, 1280)))
    sleep(3)
    # 檢查圖片存在後再執行點擊操作
    if exists(Template(r"tpl1687758533575.png", threshold=0.8)):
        touch(Template(r"tpl1687758533575.png", record_pos=(0.281, 0.822), resolution=(720, 1280)))
    sleep(10)
    while not exists(Template(r"tpl1687758577620.png", threshold=0.8)):
        print("檢測中，等待EXIT出現")
        sleep(5)

    touch(Template(r"tpl1687758577620.png", record_pos=(0.225, 0.815), resolution=(720, 1280)))
    sleep(10)
    
    while not exists(Template(r"tpl1687767147552.png", record_pos=(0.003, 0.778), resolution=(720, 1280))):
        print("檢測中，等待X出現")
        sleep(5)
        # 例外:如果檢測到EXIT出現則點EXIT
        if exists(Template(r"tpl1687758577620.png", threshold=0.8)):
            touch(Template(r"tpl1687758577620.png", record_pos=(0.225, 0.815), resolution=(720, 1280)))
        # 例外:如果檢測到終了出現則點終了
        if exists(Template(r"tpl1687758590394.png", threshold=0.8)):
            touch(Template(r"tpl1687758590394.png", record_pos=(0.225, 0.815), resolution=(720, 1280)))
    touch(Template(r"tpl1687767147552.png", record_pos=(0.003, 0.778), resolution=(720, 1280)))
    sleep(5)
    
    while not exists(Template(r"tpl1687758590394.png", threshold=0.8)):
        if q > 10:
            print("檢測中，等待EXIT出現")
            q = 0  # 重置q為0
            break
        print("檢測中，等待終了出現")
        sleep(3)
        q += 1

    if q <= 10:
        touch(Template(r"tpl1687758590394.png", record_pos=(0.343, 0.688), resolution=(720, 1280)))
        sleep(5)
    

    count += 1
