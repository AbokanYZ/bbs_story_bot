import pyautogui as pag
import PIL
import time
import keyboard

def findAndClick(path):
    # Will find the image, then click it. 
    # Returns false and terminates if nothing is found
    coords = pag.locateCenterOnScreen(path, confidence = 0.8)

    if coords == None:
        return False
    else:
        x, y = coords
        pag.click(x, y)
        return True

def storyMode():
    inMission = True # We consider starting the bot in a mission

    startFailed = 0

    print('Press "Ctrl+C" for break the script')

    while 1: 

        if startFailed < 10:
            if inMission:
                if findAndClick('assets\\skip.jpg'):
                    print('Conversation skipped')
                    continue

                elif findAndClick("assets\\auto.png"):
                    print('The bot is running...')
                    time.sleep(60)
                    print('The bot completed the quest')
                    continue

                elif findAndClick('assets\\skip.jpg'):
                    time.sleep(2)
                    continue 

                elif findAndClick('assets\\friend_request.jpg'):
                    continue

                elif findAndClick('assets\\touch_screen.jpg'):
                    continue

                elif findAndClick("assets\\next_quest.png"):
                    inMission = False
                    time.sleep(5)
                    continue

            else: # What to do when we're not in a mission

                if findAndClick('assets\\prep_quest.jpg'):
                    continue
                elif findAndClick('assets\\start_quest.jpg'):
                    inMission = True
                    time.sleep(5)
                    continue
                else:
                    print('The quest failed to start')
                    startFailed += 1
        else:
            return

storyMode()