from pywinauto import mouse
from pywinauto import keyboard
from python_imagesearch.imagesearch import imagesearch,imagesearch_count
import time
import pyautogui
import random
#啟動倒數

################################################################################################
def wait_fight(turn): #判斷是否在 pk 畫面; 是->wait 否->第一回合
    if turn[0] != -1 :     #找到 turn -> 進入第一回合
        return 1            
    else:                   #找不到 turn -> 須卡住
        return 0            

def X(): #防按錯機制 -> 出現 X -> 按 X
    x = imagesearch("photo\\X.png")
    if x[0] != -1 :
        print("出現錯誤啦")
        time.sleep(0.5)
        mouse.double_click(button='left', coords=(x[0]-1900, x[1]))

def play_card():
    # 第一張牌:815 ,857 1:793,682  2:965,682 3:1153,682
    location= [(777,688),(960,675),(1140,681)]

    for i in range (3):                             
        x=random.randint(0,2)
        time.sleep(0.5)
        mouse.press(button='left', coords=(840 ,857))                  #點第一張牌
        time.sleep(0.5)
        mouse.release(button='left', coords=location[x])               #放置區域
        time.sleep(0.5)
    X()
    time.sleep(0.5)
    mouse.double_click(button='left', coords=(1269, 978))              #點結束回合


#################################################################################################
for count in range(10):
    time.sleep(2)
    print("---------------------------------------------------")
    print("目前執行階段: ",count+1)
    #開戰
    stay = 0
    while(stay != 1):
        time.sleep(0.5)
        turn = imagesearch("photo\\fight.png")
        stay = wait_fight(turn)
        
    time.sleep(0.5)
    mouse.double_click(button='left', coords=(turn[0]-1900, turn[1])) #點開戰

    #與對手 pk 畫面
    print("正在尋找對手...")
    stay = 0
    while(stay != 1):
        turn = imagesearch("photo\\turn1.png")
        stay = wait_fight(turn)

    #第1回合
    print("進入第1回合")
    play_card()
    stay = 0
    while(stay != 1):
        turn = imagesearch("photo\\turn2.png")
        stay = wait_fight(turn)

    #第2回合
    print("進入第2回合")
    play_card()
    stay = 0
    while(stay != 1):
        turn = imagesearch("photo\\turn3.png")
        stay = wait_fight(turn)

    #第3回合
    print("進入第3回合")
    play_card()
    stay = 0
    while(stay != 1):
        turn = imagesearch("photo\\turn4.png")
        stay = wait_fight(turn)

    #第4回合
    print("進入第4回合")
    play_card()
    stay = 0
    while(stay != 1):
        turn = imagesearch("photo\\turn5.png")
        stay = wait_fight(turn)

    #第5回合
    print("進入第5回合")
    mouse.double_click(button='left', coords=(964,129))
    print("snap!")
    play_card()
    stay = 0
    while(stay != 1):
        turn = imagesearch("photo\\turn6.png")
        stay = wait_fight(turn)

    #第6回合
    print("進入第6回合")
    play_card()
    stay = 0
    while(stay != 1):
        turn = imagesearch("photo\\reward.png")
        stay = wait_fight(turn)

    time.sleep(1)
    print("領取獎勵")
    mouse.double_click(button='left', coords=(turn[0]-1900, turn[1]))      #點領取獎勵

    #下一步
    print("下一步")
    stay = 0
    while(stay != 1):
        turn = imagesearch("photo\\next.png")
        stay = wait_fight(turn)

    time.sleep(1)
    mouse.double_click(button='left', coords=(turn[0]-1900, turn[1]))      #點下一步
    