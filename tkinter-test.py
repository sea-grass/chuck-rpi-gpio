#!/usr/bin/python
# Input on BCM 3, button
# When BCM 3 is toggled, it will send a positive signal on BCM 4

# Output on BCM 4, 3.3v
# Open a window with a button that triggers a function


import RPi.GPIO as GPIO
from Tkinter import *
from PIL import Image, ImageTk

class GPIOApp:
	def __init__(self, master):
		self.master = master
		frame = Frame(self.master)
		frame.pack()

		self.button = Button(
			frame, name="quit", text="QUIT", fg="red", command=self.destroy
		)
		self.button.pack(side=LEFT)

		self.toggle_output_button = Button(
			frame, name="toggle", text="TOGGLE", command=self.toggle_output
		)
		self.toggle_output_button.pack(side=LEFT)
		self.led_off_image = Image.open("led_off.png")
		self.led_on_image = Image.open("led_on.png")
		self.led_off_photo = ImageTk.PhotoImage(self.led_off_image)
		self.led_on_photo = ImageTk.PhotoImage(self.led_on_image)

		self.led_off_label = Label(image=self.led_off_photo)
		self.led_on_label = Label(image=self.led_on_photo)

	def toggle_output(self, channel = 0):
		self.num_toggled = self.num_toggled + 1
		# toggle the output
		self.do_output = not self.do_output

		GPIO.output(4, self.do_output)
		self.update_led_image()

		if (channel == 0):
			print "gui button press"
		else:
			print "hardware button press on channel " + str(channel)

		print "Toggled " + str(self.num_toggled) + " times!"
		print "LED is currently: " + str(self.do_output)
	def update_led_image(self):
		if (self.do_output):
			self.toggle_output_button.configure(image = self.led_on_photo)
		else:
			self.toggle_output_button.configure(image = self.led_off_photo)

	def start(self):
		self.max_toggles = 4
		self.num_toggled = 0
		self.do_output = False

		# Set up GPIO using BCM numbering
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(3, GPIO.IN)
		GPIO.setup(4, GPIO.OUT)
		GPIO.output(4, self.do_output)
		# Show the LED image
		self.update_led_image()
		GPIO.add_event_detect(3, GPIO.RISING, callback=self.toggle_output, bouncetime=300)
		self.master.bind_all("t", self.toggle_output)
		self.master.bind_all("T", self.toggle_output)

		self.master.mainloop()
	def destroy(self):
		#GPIO.cleanup()
		#self.master.destroy()
		self.master.quit()
root = Tk()
app = GPIOApp(root)

# Give app control of root, it starts and destroys it
# app also takes control of GPIO; may need root privileges
app.start()
app.destroy()
GPIO.cleanup()
