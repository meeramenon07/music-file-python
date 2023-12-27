from replit import audio
import os,time

def play():
  source = audio.play_file('mysongs.mp3')
  source.paused = False
  while True:
    stop_playback = int(input("press 2 anytime to stop playbackand and  go back to the menu"))
    if stop_playback == 2:
       source.paused = True
       return
    else:
       continue
while True:
  os.system("clear")
  print("My python music player")
  time.sleep(7)
  print("press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Yeah my song is playing")
    play()
  elif userInput == 2 :
    exit()
  else:
    continue 

    

    

    
  











