import pyautogui as pag
import PIL
import time
import sys

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

    startFailed = auto = 0

    print('Press "Ctrl+C" for break the script')

    while 1: 

        if startFailed < 10:
            if inMission:
                if findAndClick("assets\\auto.png") and auto == 0:
                    auto += 1
                    print('The bot is running...')
                    time.sleep(60) # Until the quest is over
                    print('The bot completed the quest')
            
                elif findAndClick('assets\\skip.jpg'):
                    print('Conversation skipped')
                    time.sleep(2)

                elif findAndClick('assets\\friend_request.jpg'):
                    pass

                elif findAndClick('assets\\touch_screen.jpg'):
                    pass

                elif findAndClick("assets\\next_quest.png"):
                    inMission = False
                    time.sleep(5)

            else: # What to do when we're not in a mission

                pag.click(x=1054, y=826)
                
                if findAndClick('assets\\skip.jpg'):
                    print('Conversation skipped')
                    time.sleep(5)

                elif findAndClick('assets\\prep_quest.jpg'):
                    time.sleep(5)

                elif findAndClick('assets\\start_quest.jpg'):
                    inMission = True
                    time.sleep(5)

                else:
                    print('The quest failed to start')
                    startFailed += 1
        else:
            return

def secondaryQuest(): 
    pass

if len(sys.argv) != 2:
    print("Usage: python main.py <mode> ('story', 'secondary')")
    sys.exit(1)

mode = sys.argv[1].lower()

if mode == "story":
    storyMode()
elif mode == "secondary":
    secondaryQuest()
else:
    print('No mode selected')