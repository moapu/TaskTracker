# Project:Speech Recognition Time App
# Purpose Details: Listen and read in user speech to use as a timer
# Course: 412
# Author: Chris Valko, Mostafa apu
# Date Developed: 10/30/2018
# Last Date Changed: 11/03/2018
# Rev: 1

import speech_recognition as sr

class SpeechAppetizer:
# get audio from the microphone

	r = sr.Recognizer()  # RECOGNIZE

	def google_api(self):
		with sr.Microphone() as source:
			self.r.adjust_for_ambient_noise(source)
			print("Speak:")
			audio = self.r.listen(source)
		try:
			if self.r.recognize_google(audio) == "test":
				print("You said " + self.r.recognize_google(audio))
			elif self.r.recognize_google(audio) != "test":
				print(self.r.recognize_google(audio))

		except sr.UnknownValueError:
			print("Could not understand audio")
		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))

	def houndify_api(self):
		with sr.Microphone() as source:
			self.r.adjust_for_ambient_noise(source)
			print("Speak:")
			audio = self.r.listen(source)
		try:
			if self.r.recognize_houndify(audio) == "test":
				print("You said " + self.r.recognize_houndify(audio))
			elif self.r.recongize_houndify(audio) != "test":
				print(self.r.recognize_houndify(audio))

		except sr.UnknownValueError:
			print("Could not understand audio")
		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))

if __name__ == "__main__":

	s = SpeechAppetizer()
	#s.google_api()
	#s.houndify_api() needs to be paid for. This will not work for our application
