import sys, os
import paho.mqtt.client as mqtt
import time
# try:
#     import RPi.GPIO as GPIO
# except RuntimeError:
#     print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

TOPIC_PATH="/omnihacks/record/10"
OFF=0
ON=1
CHANNELS = [3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26,29,31,32,33,35,36,37]
DEBUG = False

def dbg(msg):
    global DEBUG
    if DEBUG:
        print(msg)
        sys.stdout.flush()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    dbg("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    dbg("Subscribing to " + TOPIC_PATH)# +"#")
    client.subscribe( TOPIC_PATH)# +"#")

# Function that abstracts on/off condition for GPIO state
# def gpioStateFor(on):
#     if on:
#         return GPIO.HIGH
#     return GPIO.LOW

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("received")
    f = open('new_doctor.wav', 'wb')
    f.write(msg.payload)
    f.close()
    # os.system("afplay new_doctor.wav")

if len(sys.argv) > 1 and sys.argv[1] == '-d':
    DEBUG = True
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("connecting")
client.connect("mqtt.eclipse.org")
print("connected")
# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
# GPIO.setup(CHANNELS, GPIO.OUT)
# GPIO.output(CHANNELS, gpioStateFor(OFF))
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
