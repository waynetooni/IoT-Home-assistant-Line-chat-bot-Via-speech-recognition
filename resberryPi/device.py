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


Device1 = LED(2) 
Device2 = LED(3)
doc_ref = db.collection('device').document('10427137')
docs = doc_ref.get()
docs = docs.to_dict()


while True:
    
    try:
      Device1State = docs['fan']
      Device2State = docs['fan']
      Device1.value = ledBathState
      Device2.value = ledKitchState
      print("Change!!")
      docs = doc_ref.get()
      docs = docs.to_dict()
      print("Done!!")
    except :
      print( "Device no register" )
#fan tome turntable tv

