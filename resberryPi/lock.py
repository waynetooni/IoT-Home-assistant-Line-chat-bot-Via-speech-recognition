from gpiozero import LED
from requests import get  
import json
import time                                                     
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("finalkey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Lock Default
LockBack = LED(2) 
UnlockBack = LED(3)
LockFront = LED(4)
UnlockFront = LED(11)
LockWindow = LED(13)
UnlockWindow = LED(15)
doc_ref = db.collection('lock').document('10427135')
docs = doc_ref.get()
docs = docs.to_dict()

try :
  BackdoorState = docs['backdoor']
  FrontdoorState = docs['frontdoor']
  WindowsState = docs['windows']
  Time = docs['time']
except:
  print("Device not regist")
# Lock Default


while True:
    
    time.sleep(Time)
    try:
      BackdoorState = docs['backdoor']
      FrontdoorState = docs['frontdoor']
      WindowsState = docs['windows']
      Time = docs['time']
      if BackdoorState == False  :
        LockBack.value = True
        UnlockBack.value = False
      elif BackdoorState == True :
        LockBack.value = False
        UnlockBack.value = True

      if FrontdoorState == False :
        LockFront.value = True
        UnlockFront.value = False 
      elif FrontdoorState == True :
        LockFront.value = False
        UnlockFront.value = True 

      if WindowsState == False :
        LockWindow.value = True
        UnlockWindow.value = False 
      elif WindowsState == True :
        LockWindow.value = False
        UnlockWindow.value = True 
   
      print("Change!!")
      docs = doc_ref.get()
      docs = docs.to_dict()
      print("Done!!")
    except:
      print( "Device not regist" )



