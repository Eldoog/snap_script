from pywinauto import mouse
from pywinauto import keyboard
from python_imagesearch.imagesearch import imagesearch,imagesearch_count
import time
import pyautogui

#啟動倒數

"""
#點遊戲畫面
game_screen = imagesearch("photo\\fight.png")
def start_game(game_screen):
    if game_screen[0] != -1 :
        #print("position : ", sale[0], sale[1])
        mouse.double_click(button='left', coords=(game_screen[0]-1900, game_screen[1]))
    else:
        mouse.double_click(button='left', coords=(1249,975))                                 #點領取獎勵+結束遊戲
    time.sleep(0.5)

a(game_screen)
"""
game_screen= [1,imagesearch("photo\\turn1.png")]

print((game_screen[1]))