#Import the modules

import easygui
import time

minutes_ = int(input("Minutes: "))
seconds = 0
seconds = minutes_ * 60

for i in range(seconds):
  time.sleep(1)

easygui.msgbox("Times up!")
