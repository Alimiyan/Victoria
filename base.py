import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

# animation effect on terminal
# importing the necessary packages
import time
import sys
import os

# Function for implementing the loading animation
def load_animation():

	# String to be displayed when the application is loading
	load_str = "initiating in T minus ten seconds"
	ls_len = len(load_str)


	# String for creating the rotating line
	animation = "|/-\\"
	anicount = 0
	
	# used to keep the track of
	# the duration of animation
	counttime = 0		
	
	# pointer for travelling the loading string
	i = 0					

	while (counttime != 100):
		
		# used to change the animation speed
		# smaller the value, faster will be the animation
		time.sleep(0.075)
							
		# converting the string to list
		# as string is immutable
		load_str_list = list(load_str)
		
		# x->obtaining the ASCII code
		x = ord(load_str_list[i])
		
		# y->for storing altered ASCII code
		y = 0							

		# if the character is "." or " ", keep it unaltered
		# switch uppercase to lowercase and vice-versa
		if x != 32 and x != 46:			
			if x>90:
				y = x-32
			else:
				y = x + 32
			load_str_list[i]= chr(y)
		
		# for storing the resultant string
		res =''			
		for j in range(ls_len):
			res = res + load_str_list[j]
			
		# displaying the resultant string
		sys.stdout.write("\r"+res + animation[anicount])
		sys.stdout.flush()

		# Assigning loading string
		# to the resultant string
		load_str = res

		
		anicount = (anicount + 1)% 4
		i =(i + 1)% ls_len
		counttime = counttime + 1
	
	# for windows OS
	if os.name =="nt":
		os.system("cls")
		
	# for linux / Mac OS
	else:
		os.system("clear")

# Driver program
if __name__ == '__main__':
	load_animation()

	# Your desired code continues from here
	# s = input("Enter your name: ")
	s ="Alimiyan"
	sys.stdout.write("Hello "+str(s)+"\n")


# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():

	r = sr.Recognizer()

	# from the speech_Recognition module
	# we will use the Microphone module
	# for listening the command
	with sr.Microphone() as source:
		print('Listening')

		
		# seconds of non-speaking audio before
		# a phrase is considered complete
		r.pause_threshold = 0.7
		audio = r.listen(source)
        
		
		# Now we will be using the try and catch
		# method so that if sound is recognized
		# it is good else we will have exception
		# handling
		try:
			print("Recognizing")
			
			# for Listening the command in indian
			# english we can also use 'hi-In'
			# for hindi recognizing
			Query = r.recognize_google(audio, language='en-in')
			print("the command is printed=", Query)
			
		except Exception as e:
			print(e)
			print("Say that again sir")
			return "None"
		
		return Query

def speak(audio):
	
	engine = pyttsx3.init()
	# getter method(gets the current value
	# of engine property)
	voices = engine.getProperty('voices')
	
	# setter method .[0]=male voice and
	# [1]=female voice in set Property.
	engine.setProperty('voice', voices[1].id)
	
	# Method for the speaking of the the assistant
	engine.say(audio)
	
	# Blocks while processing all the currently
	# queued commands
	engine.runAndWait()

def tellDay():
	
	# This function is for telling the
	# day of the week
	day = datetime.datetime.today().weekday() + 1
	
	#this line tells us about the number
	# that will help us in telling the day
	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)


def tellTime():
	
	# This method will give the time
	time = str(datetime.datetime.now())
	
	# the time will be displayed like
	# this "2020-06-05 17:50:14.582630"
	#nd then after slicing we can get time
	print(time)
	hour = time[11:13]
	min = time[14:16]
	speak( "The time is sir" + hour + "Hours and" + min + "Minutes")	

def Hello():
	
	# This function is for when the assistant
	# is called it will say hello and then
	# take query
	speak("hello ali ,how is your day. Tell me how may I help you")


def Take_query():

	# calling the Hello function for
	# making it more interactive
	Hello()
	
	# This loop is infinite as it will take
	# our queries continuously until and unless
	# we do not say bye to exit or terminate
	# the program
	while(True):
		
		# taking the query and making it into
		# lower case so that most of the times
		# query matches and we get the perfect
		# output
		query = takeCommand().lower()
		if "what's the weather today" in query:
			speak("the weather today in sunny and thirty one degree celcius")
			continue
		
		elif "open google" in query:
			speak("Opening Google ")
			webbrowser.open("www.google.com")
			continue
			
		elif "which day it is" in query:
			tellDay()
			continue
		
		elif "tell me the time" in query:
			tellTime()
			continue
		
		# this will exit and terminate the program
		elif "bye" in query:
			speak("Bye. Have a great day")
			exit()
		
		elif "from wikipedia" in query:
			
			# if any one wants to have a information
			# from wikipedia
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			
			# it will give the summary of 4 lines from
			# wikipedia we can increase and decrease
			# it also.
			result = wikipedia.summary(query, sentences=4)
			speak("According to wikipedia")
			speak(result)
        
		
		elif "tell me your name" in query:
			speak("I am Jarvis. Your deskstop Assistant")


if __name__ == '__main__':
	
	# main method for executing
	# the functions
	Take_query()
