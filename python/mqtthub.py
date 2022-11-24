import paho.mqtt.client as mqtt
import sys
import asyncio
import io
import os
import datetime
from base64 import b64encode, b64decode
from time import time, sleep
from urllib import parse
from hmac import HMAC
from hashlib import sha256
from ssl import SSLContext, PROTOCOL_TLS_CLIENT, CERT_REQUIRED

def on_connect(client, obj, flags, rc):
    print("connect: " + str(rc))
    client.subscribe("devices/myDevice1/location/")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def generate_sas_token(IOT_HUB_HOSTNAME, IOT_HUB_DEVICE_ID, IOT_HUB_SAS_KEY):
    ttl = int(time()) + 300
    uri = IOT_HUB_HOSTNAME + "/devices/" + IOT_HUB_DEVICE_ID
    sign_key = uri + "\n" + str(ttl)

    signature = b64encode(HMAC(b64decode(IOT_HUB_SAS_KEY), sign_key.encode('utf-8'), sha256).digest())

    return "SharedAccessSignature sr=" + uri + "&sig=" + parse.quote(signature, safe="") + "&se=" + str(ttl)

if len(sys.argv) != 4:
    exit

IOT_HUB_HOSTNAME = sys.argv[1]
IOT_HUB_DEVICE_ID = sys.argv[2]
IOT_HUB_SAS_KEY = sys.argv[3]

client = mqtt.Client(client_id=IOT_HUB_DEVICE_ID, protocol=mqtt.MQTTv311)
client.on_connect    = on_connect
client.on_message    = on_message

client.username_pw_set(username=IOT_HUB_HOSTNAME + "/" + IOT_HUB_DEVICE_ID + "/?api-version=2021-04-12", 
                            password=generate_sas_token(IOT_HUB_HOSTNAME, IOT_HUB_DEVICE_ID, IOT_HUB_SAS_KEY))

ssl_context = SSLContext(protocol=PROTOCOL_TLS_CLIENT)
ssl_context.load_default_certs()
ssl_context.verify_mode = CERT_REQUIRED
ssl_context.check_hostname = True
client.tls_set_context(context=ssl_context)

client.connect(host=IOT_HUB_HOSTNAME, port=8883, keepalive=120)

# start the MQTT processing loop
client.loop_start()

# send messages
curdir = os.path.dirname(os.path.realpath(__file__))
with open(curdir + "\\data.json","r") as data:
    list = []
    list = data.readlines()
    i = 0
    while i < len(list):
        # Send a single message
        topic = "devices/" + IOT_HUB_DEVICE_ID + "/location/"
        client.publish(topic, list[i], qos=1)
        print("[{0}] topic:{1} msg:{2}".format(datetime.datetime.utcnow(), topic, list[i]))
        i += 1
        sleep(1)