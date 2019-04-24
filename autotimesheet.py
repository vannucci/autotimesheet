import pyautogui
import os
import json
import datetime
import psutil

#Settings
default_pause = 1.0
pyautogui.PAUSE = default_pause
timesheetsfile = 'timesheetbatch.json'
with open(timesheetsfile) as json_file:
  timesheets = json.load(json_file)
typewrite_interval = 0.15


def inputSchedule(idx,schedule):
  pyautogui.typewrite(schedule)
  if(idx % 8 != 0): #since the first cell entries fill the cell, the terminal automatically advances
    pyautogui.press('tab')

def pause(time):
  pyautogui.PAUSE = time
  pyautogui.press('ctrl')
  pyautogui.PAUSE = default_pause

def confirm_login():
  login_confirmation = pyautogui.screenshot(f'{USERNAME}-loginscreen.png',region=(0,0,652,412))
  #if main menu is not shown, then fail and end the job, return the failure notice
  return True

def killprocess():
  # Tried to find a ways to kill the process, but this is just easier
  button_x, button_y = pyautogui.locateCenterOnScreen('killprocess.png')
  pyautogui.click(button_x,button_y)
  pyautogui.press('enter')


def entertimesheets(USERNAME,PASSWORD,TIMESHEET,COMMANDS):
  # input credentials
  pyautogui.typewrite(f'{USERNAME}', interval=typewrite_interval)
  pyautogui.press('tab')
  pyautogui.typewrite(f'{PASSWORD}', interval=typewrite_interval)
  pyautogui.press('enter')
  if(not confirm_login):
    return False


  #navigate to timesheet, wait extra before final command
  for i in COMMANDS:
    if(i == "timm"):
      pause(5)
      pyautogui.typewrite(i,interval=typewrite_interval)
      pyautogui.press('enter')
    else:
      pyautogui.typewrite(i,interval=typewrite_interval)
      pyautogui.press('enter')

  
  #enter timesheet
  #temporarily speed up input
  pyautogui.PAUSE = 0.2
  for idx, schedule in enumerate(TIMESHEET):
    inputSchedule(idx,schedule)
  #slow down input again
  pyautogui.PAUSE = 0.5

  #screenshot
  timesheet_confirmation = pyautogui.screenshot(f'./confirmationimages/{USERNAME}-{datetime.datetime.now().strftime("%m%d%Y")}.png',region=(0,0,652,412))
  pause(1)

  #end timesheets
  pyautogui.press('enter')
  pyautogui.press('f12')
  pyautogui.press('f12')
  pause(10)
  return True

def main():
  if timesheets is not None:
    #start up terminal
    os.startfile(r"C:\Users\cimav\Desktop\MVSP.lnk")
    
    #possible fail point, term doesn't open
    pause(2.0)

    for user in timesheets['employees']:
      entertimesheets(user['username'],user['password'],user['timesheet'].split(','),user['commands']);
    
    killprocess()

  else:
    print('Batch JSON file not found, please create and store in same directory as this file.')


#kill process name NOVTRM32.EXE
main()