import Adafruit_DHT 
from gpiozero import LED
from requests import get 
import json
import time                                                     
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

hum, temp = Adafruit_DHT.read_retry(11,4)
doc_ref = db.collection('heating').document('TEST')


while True:
    
    try:
      doc_ref.update({u'humidity' : "hum"}) 
      doc_ref.update({u'temperature' : "temp"})
      doc_ref = db.collection('heating').document('TEST')
	  docs = doc_ref.get()
      docs = docs.to_dict() 
	  HumState = docs['humidity']
      TempState = docs['temperature']
    except :
      print( "Device no register" )
    time.sleep(60)


