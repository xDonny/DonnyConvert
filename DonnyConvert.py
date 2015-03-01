# Donny Bridgen
# February 2015
#
# Purpose:
# To convert audio/video files to whatever format I want.
#
# This program is created using ffmpeg, licensing for which can be found in the /license directory
# 
# This program is provided for free to use, distribute, sell, include in whatever you like.
# However it comes with no warranty, anything that happens as a result of using this program is not
# my fault.

#imports
import os
#define clear for clearing the screen
clear = lambda: os.system("cls")
clear()
#define input to exit the while loop
input = int(0);

#while loop
while input != 3:
	#display menu and pleasantries
	print "Welcome to DonnyConvert v0.1 Beta"
	print "Main Menu"
	print "1: Convert"
	print "2: About"
	print "3: Exit"
	#get menu selection
	input = int(raw_input("Enter a menu item:"))
	
	#menu item 1 selected
	if input == 1:
		#clear screen
		clear()
		print 'Convert File'
		#get options/files
		inputFilePath = str(raw_input("Input Path + File:"))
		outputFilePath = str(raw_input("Output Path + File:"))
		outputQuality = str(raw_input("Output Quality (0[best/slowest]...31[poor/fastest] enter for 0):"))
		options = str(raw_input("Options (blank for default [advanced]): "))
		#options added?
		if options == "":
			print "Converting... (this may take awhile)"
			#check if quality was skipped
			if outputQuality == "":
				os.system(os.getcwd() + "/binary/ffmpeg.exe -loglevel error -i " + inputFilePath + " -qscale 0 "  + outputFilePath)
			else:
				os.system(os.getcwd() + "/binary/ffmpeg.exe -loglevel error -i " + inputFilePath + " -qscale " + outputQuality + " " + outputFilePath)
			print "Done."
			raw_input("Enter to go back to main menu.")
		else:
			print "Converting... (this may take awhile)"
			os.system(os.getcwd() + "/binary/ffmpeg.exe -loglevel error -i " + inputFilePath + " " + options + " " + outputFilePath)
			print "Done."
			raw_input("Enter to go back to main menu.")
	if input == 2:
		clear()
		print 'About'
		print 'Created using ffmpeg in Python by Donny Bridgen'
		print 'Licensing information can be found in the license folder'
		print 'This software is provided without warranty'
		print ''
		raw_input("Enter to go back to main menu.")
	clear()
