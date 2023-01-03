# Import standard library python modules
led1 = 21
import RPi.GPIO as GPIO
import sys, board, adafruit_dht
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
dhtDevice = adafruit_dht.DHT11(board.D21)
# This example uses the MQTTClient instead of the REST client
from Adafruit_IO import MQTTClient

# Set to your Adafruit IO Key
# Remember not to publish it when you publish this code
ADAFRUIT_IO_KEY = 'aio_IbOT84Rs6ypUMTnoLWYPCTiJMjg4'

# Set to your Adafruit IO username.
ADAFRUIT_IO_USERNAME = 'Jashiel'

# Set to the ID of the FEED to subscribe to for update
FEED_ID = 'led'


# Called when we're connected to adafruit mqtt server
def connected(client):
    """Connected function will be called when the client is connected to
    Adafruit IO. This is a good place to subscribe to feed changes. The client
    parameter passed to this function is the Adafruit IO MQTT client so you
    can make calls against it easily
    """
    # Subscribe to changes on a feed named Counter.
    print('Subscribing to feed {0}'.format(FEED_ID))
    client.subscribe(FEED_ID)
    print('Waiting for feed data')


# this function will be automatically called, if we're disconnected from adafruit mqtt server

def disconnect(client):
    """Disconnected function will be called when the client disconnects."""
    sys.exit(1)


# this function will be called whenever there is a new data to the feeds to which we'ver subscribed
def message(client, feed_id, payload):
    """Message function will be called when a subscribed feed has a new value.
    The feed_id parameter identifies the feed, and the payload parameter has
    the new value.
    """
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    print('Actual payload is ', payload)
    if feed_id == 'led':
        if payload == 'ON':
            GPIO.output(led1, True)
        if payload == 'OFF':
            GPIO.output(led1, False)


# Create an MQTT client instance
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect = connected
client.on_disconnect = disconnect
client.on_message = message

# Connect to the Adafruit IO server
client.connect()

#The first option is to run a thread in the background so you can continue
# doing things in your program, to do so use below line
client.loop_background()

#Alternatively, you can simply block your program for waiting for incoming stream of
# data from subscription and the message function will take care of stuffs
while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        client.publish('temp', temperature_c)
        print('temperature published')

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(10)
