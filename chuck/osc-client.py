#!/usr/bin/python3

import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client

import RPi.GPIO as GPIO

client = None

def send_signal(channel = 0):
	global client
	msg = osc_message_builder.OscMessageBuilder(address="/myChucK/OSCNote")
	# Our OSC Server in ChucK is expecting an int, a float, and a string
	if (channel == 0 or channel == 3):
		msg.add_arg(0)
	else:
		msg.add_arg(1)
	msg.add_arg(0.5)
	msg.add_arg("Yahoo!")
	msg = msg.build()

	print("Sending", msg.dgram)
	client.send(msg)
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip", default="127.0.0.1", help="The ip of the OSC server")
	parser.add_argument("--port", type=int, default=6449, help="The port the OSC server is listening on")
	args = parser.parse_args()

	client = udp_client.UDPClient(args.ip, args.port)

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(3, GPIO.IN)
	GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(3, GPIO.RISING, callback=send_signal, bouncetime=100)
	GPIO.add_event_detect(4, GPIO.RISING, callback=send_signal, bouncetime=100)

	fugget = 0
	while (1):
		# Do nothing
		fugget = fugget + 1

