#!/usr/bin/python

"""
This program checks for adjacent repeated words in a text file, i.e., the same word written back to back.
The intention is catch typos in which the document's author may have accidentally typed the same word twice.
For example, "Let's go to the the movies." 
"""

import sys

def join_dupes(words):

    words[1] = '*' + words[1]
    words[2] = words[2] + '*'

    return ' '.join(words)

def find_dupes(word_list):

    # Searches through the list for instances when the (i)th word 
    # is the same as the one immediately preceding it.
    duplicates = []
    for i in range(len(word_list)):
        if word_list[i] == word_list[i-1]:
            if word_list[i].isalpha():     
                joined_string = join_dupes(word_list[i-2:i+2])
                duplicates.append(joined_string)
    return duplicates


def checkdoc(file_name):

    try:
        with open(file_name, 'r+') as f:
            read_file = f.read()
    except IOError:
        return

    # Split text into array of single words
    split_words = read_file.split()

    duplicates = find_dupes(split_words)

    print '#', file_name
    if not duplicates:
        print('No duplicates found')
        return

    for index, instances in enumerate(duplicates):
        print "[%d]" % (index + 1), instances


if __name__ == "__main__":
    print
    file_names = sys.argv[1:]
    while file_names:
        checkdoc(file_names.pop())
        print

    
