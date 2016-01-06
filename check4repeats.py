#!/usr/bin/python

"""
This program checks for adjacent repeated words in a text file, i.e., the same word written back to back.
The intention is catch typos in which the document's author may have accidentally typed the same word twice.
For example, "Let's go to the the movies." 
"""
import sys

def checkdoc():
	# The following block of code takes a user identified file 
	# and opens it and reads its contents
	file_name = raw_input("Enter file name: ")

	# strips all backslashes from path and file name. 
	## these backlashes are created if you drag a file into the terminal
	## and the file is in a director with spaces in its name
	for char in file_name:
		if "\\" in file_name:
			the_file = file_name.replace("\\", '')
		else:
			pass	

	opened_file = open(the_file, 'r+')
	read_file = opened_file.read()

	# The text in the read_file is then split and put into a list
	list = read_file.split()

	# Searches through the list for instances when the (i)th word 
	# is the same as the one immediately preceding it.
	duplicate_list = []
	for word in range(len(list)):
		if list[word] == (list[word-1]):
			if list[word].isalpha(): 
			    found_duplicates = list[word-2], '*'+list[word-1], list[word]+'*', list[word+1]
			    joined_string = " ".join(found_duplicates)
			    duplicate_list.append(joined_string) 
			else: # if the repeated word is not a alpha, pass over it.
				pass
		else:
			pass


	# Takes all instances within the list of duplicates (duplicate_list)
	# and enumerates and prints each one. 
	# Also writes each instance to the text file text_file

	if len(duplicate_list) == 0:
		print 'No duplicates found'
	else:
		print

		# (instances + 1) used to begin enumeration at 1 rather than 0
		for instances in range(len(duplicate_list)):
			print "[%d]" % (instances + 1), duplicate_list[instances]

		print
		print "Press 'S' to save output to textfile.\nPress 'N' to check new file.\nPress any other key to quit"
		user_input = raw_input("> ")
		lowercase_input= user_input.lower()
		
		if lowercase_input == 's':
			
			text_file = the_file + '_Duplicate_List.txt'
			output_file = open(text_file, 'w+')
			
			for instances in range(len(duplicate_list)):
				output_file.write('[%d]' % (instances + 1)), output_file.write(duplicate_list[instances])
				output_file.write('\n')
			
			print
			print "SAVED to %s" % text_file
			print
		elif lowercase_input == 'n':
			checkdoc()
		else:
			sys.exit()


if __name__ == "__main__":
	print "\nCHECK FOR REPEATS\n"
	checkdoc()
	while True:
		choice = raw_input("Check New File? Y/N: ")
		if choice.lower() == 'y':
			checkdoc()
		else:
			break

	
