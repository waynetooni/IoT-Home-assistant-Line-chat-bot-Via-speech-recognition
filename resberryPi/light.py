#!/usr/bin/python

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

# Light Default 

ledBathroom = LED(2)   #red
ledKitchen = LED(3)    #green
ledBedroom = LED(4)    #yellow


doc_ref = db.collection('light').document('10427126')
docs = doc_ref.get()
docs = docs.to_dict()
ledBathState = docs['bathroom']
ledKitchState = docs['kitchen']
ledBedState = docs['bedroom']
Time = docs['time']

# Light Default 


while True:
    
    time.sleep(Time)
    try:
      ledBathState = docs['bathroom']
      ledKitchState = docs['kitchen']
      ledBedState = docs['bedroom']
      Time = docs['time']
      ledBathroom.value = ledBathState
      ledKitchen.value = ledKitchState
      ledBedroom.value = ledBedState
    
      print("Change!!")
      docs = doc_ref.get()
      docs = docs.to_dict()
      print("Done!!")
    except :
      print( "Device no register" )
     

