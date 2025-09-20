#Healthy programmer
#jop 9am - 5pm 
#reminder he will get : 1) water (3.5L) - play: water.mp3 , : 250ml every 35 minutes, 14 reminders 
#                          take input to turn off the music - Drank
#                          remaining water 
#                          record the timing of drink 
#                       2) Eyes - play: eyes.mp3, : every 30 min. 
#                          take input to turn off the music : Done
#                          reset the timer
#                       3) Physical activity - play: physical.mp3, : every 45 min.
#                          take input to turn off the music : Done
#                          reset the timer
# conditions : 1)the time slot shouldn't clash 
#              2) in such condition play one by one , like if first is done play the second one 
#              3) Use pygame module to play the song
# Module needs : datetime, time, pygame, 

#importing the needed module
import pygame
import sys
import time
import datetime
# import TimerModule as tm

#initializing the pygame module
pygame.init()
pygame.mixer.init()

#asking for permission
start_the_reminder = input(" Do you want to start the reminder?? [yes/no]: ")
#--------------------------------------------------asking-------------------------------------------------------------
def ask1():
    q1 = input(" Have you drank water?? [yes/no]: ")
    if q1 == 'yes':
        pygame.quit()
        with open("water_rem.txt","a") as f:
            f.write(f" Drank water at: {time.asctime(time.localtime(time.time()))}")
        print(" Keep going on.\n All the best")
    elif q1 == "no":
        print(" Please drink water in the next break!")
    else:
        print(" Please enter the correct one out of given options!")
        ask1()


def ask2():
    q2 = input(" Have you done eye relaxation workout?? [yes/no]: ")
    if q2 == 'yes':
        pygame.quit()
        print(" Keep going on.\n All the best.")
    elif q2 == 'no':
        print(" Please do in the next reminder!")
    else:
        print(" Plese enter the correct one out of give options!")
        ask2()
    #write the code for reset the timer

def ask3():
    q3 = input(" Have you done eye relaxation workout?? [yes/no]: ")
    if q3 == 'yes':
        pygame.quit()
        print(" Keep going on.\n All the best.")
    elif q3 == 'no':
        print(" Please do in the next reminder!")
    else:
        print(" Plese enter the correct one out of give options!")
        ask3()
    #write the code to reset the timer 


#--------------------------------------------------reminder-----------------------------------------------------------------------------------
def water_reminder():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("water.mp3")
    pygame.mixer.music.play()
    ask1()

def eyes_reminder():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("eyes.mp3")
    pygame.mixer.music.play()
    ask2()

def physical_reminder():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("physical.mp3")
    pygame.mixer.music.play()
    ask3()

#------------------------------------------------timer-----------------------------------------------------------------------------------------
count = 0
while start_the_reminder == "yes":
    if count == 2:
        start_the_reminder = "no"

    time.sleep(20*60)
    water_reminder()
    time.sleep(10*60)
    eyes_reminder()
    time.sleep(15*60)
    physical_reminder()
    time.sleep(15*60)
    count += 1

print("Thanks for visiting here.🙌🙌")