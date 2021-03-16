
import paho.mqtt.client as mqttclient
import time
import base64
import pytesseract
from PIL import Image   
import cv2
import os
import numpy as np

part1 = ""
part2 = ""
picture = ""


def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("Client is connected")
        global connected
        connected=True
    else:
        print("Client is not connected")

def on_message(client,userdata,message):
    if str(message.topic) == "Office/SecureCo/webcam/feed/part1":
        global part1
        part1 = str(message.payload.decode("utf-8"))
        print("gotch you 1")

    elif str(message.topic) == "Office/SecureCo/webcam/feed/part2":
        global part2
        part2 = str(message.payload.decode("utf-8"))
        print("gotch you again!")
        global messagerecieved 
        messagerecieved=True

        
connected=False
messagerecieved=False

broker_address = "35.225.10.98"
port = 1883
user="iot"
password="iot"


web_user = "administrator"
web_pass = "SeCUReP@55W0rD1"

client = mqttclient.Client("MQTT")
client.on_message=on_message
client.username_pw_set(user,password=password)
client.on_connect=on_connect
client.connect(broker_address,port=port)
client.loop_start()
client.subscribe("#")
while connected!=True:
    time.sleep(0.2)
while messagerecieved!=True:
    time.sleep(0.2)


client.loop_stop()
client.disconnect()

if part1 != "" and part2 != "":
    picture = part1 + part2
    picture = base64.b64decode(picture)


    f = open("testtest.png","wb")
    f.write(picture)
    f.close()
    print("file written!!")

    img = cv2.imread('testtest.png')

    cropped = img[130:145, 175:235]
   


    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    
    gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)

    cv2.imshow("Image", cropped)
    cv2.imshow("Output", gray)
    cv2.waitKey(0)

    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
    print(pytesseract.image_to_string(r'/home/iotvm/Desktop/CTF/nahacon/testtest.jpg'))
    result = str(pytesseract.image_to_string(img, config='--psm 13 --oem 3 '))  
    print(result)
else:
    print("Time out!!")
