from pywinauto import mouse
from pywinauto import keyboard
from python_imagesearch.imagesearch import imagesearch,imagesearch_count
import time
import pyautogui

#啟動倒數
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("開始!!!")

#點遊戲畫面
game_screen = imagesearch("photo\\fight.png")
turn1 = imagesearch("photo\\turn1.png")
turn2 = imagesearch("photo\\turn2.png")
turn1 = imagesearch("photo\\turn1.png")
turn2 = imagesearch("photo\\turn2.png")
"""
if game_screen[0] != -1 :
    #print("position : ", sale[0], sale[1])
    mouse.double_click(button='left', coords=(game_screen[0]-1900, game_screen[1]))
else:
    mouse.double_click(button='left', coords=(1249,975))                                 #點領取獎勵+結束遊戲
time.sleep(0.5)
"""




stun = 1
while(stun != 0):
    if turn1[0] != -1:
        # 第一張牌:815 ,857 1:793,682  2:965,682 3:1153,682
        mouse.press(button='left', coords=(815 ,857))
        mouse.release(button='left', coords=(1153, 682))
        mouse.press(button='left', coords=(815 ,857))
        mouse.release(button='left', coords=(1153, 682))
        mouse.press(button='left', coords=(815 ,857))
        mouse.release(button='left', coords=(1153, 682))
        print("出招完畢")
        mouse.double_click(button='left', coords=(1269, 978))
    else:
        print("dead")
        stun -= 1
print("第二回合")
stun =0



def start_game(game_screen):#點開戰
    if game_screen[0] != -1 :
        #print("position : ", sale[0], sale[1])
        mouse.double_click(button='left', coords=(game_screen[0]-1900, game_screen[1]))
    else:
        mouse.double_click(button='left', coords=(1249,975))                                 #點領取獎勵+結束遊戲

start_game(game_screen)