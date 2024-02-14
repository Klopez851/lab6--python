# Author:  Dr. Adam R. Albina
# Filename: words.py
# Description:
#
# Python Random Word generator class.  This class will create a Words object and generate
# 25,386 words for use in your programs.  Calling the getRandomWordList(n) method returns a list of
# n random words.  The word list is based on the words provide from a URL: http://svnweb.freebsd.org/csrg/share/dict/words
# After a few semesters of students hitting the site - they stopped allowing the connection so
# now you are connecting to the CS Web Serve Apollo in order to get the file the first time.  You
# must be on the College network to get the file the first time.

# In order to avoid connecting to the CS Server everytime a program runs, this class creates
# a serialized byte code encoded file in the directory from which the python main program is
# is run named "words_list.ser".  It will check to see if the local file exists before connecting
# to the CS Server to create it.  If it exists it will reconstitute the serialized file into a list
# and use that instead.  If you delete the "words_list.ser" file - it will be recreated when you
# instantiate the object the next time by connecting to the CS Server.
#
# Once the object is instantiated, call the getRandomWord() method to get a string containing a random word, or
# call the getRandomWordList() method optionally including the number of words you want in your returned
# list as an argument.  If you omit the argument, the method defaults to a list of five words.

# Usage:
#       from words import Words
#
#       MyWords = Words()
#       myString = MyWords.getRandWord()
#       print(myString)

#       MyWords = Words()
#       myList = MyWords.getRandWordList(20)
#       print(myList)

import urllib.request
import urllib.response
import pickle
from pathlib import Path
import random
import time

class Words():

    global DEBUG
    DEBUG=True

    def __init__(self):
        __words=[]
        myPath = Path.cwd()
        qualifiedFileName = myPath / "words_list.ser"
        print("Looking for: ", qualifiedFileName) if DEBUG else ""

        if qualifiedFileName.exists():
            print('Reconstituting serialzed Word list from local resources.') if DEBUG else ''
            bench1_start=time.time_ns()
            self.__words = pickle.load(open(qualifiedFileName, 'rb'))
            bench1_stop=time.time_ns()
        else:
            try:
                print("Getting Word list from CS Server resource.") if DEBUG else ""
                response=None
                count = 0
                bench1_start = time.time_ns()
                while not response and count < 3:
                    try:
                        response = urllib.request.urlopen('http://apollo.anselm.edu/new_words.txt',timeout=10)
                    except urllib.error.URLError as err:
                        if count == 2:
                            raise urllib.error.URLError(myError)
                        print(err.reason)
                        myError = err.reason
                        count+=1

                try:
                    txt=response.read()
                except AttributeError as err:
                    print(err)
                    print("There was a problem creating the Words object.")
                    exit()
                self.__words=txt.splitlines()
                for i, item in enumerate(self.__words):
                    self.__words[i]=item.decode('utf-8')
                myPath=Path.cwd()
                qualifiedFileName=myPath / 'words_list.ser'
                print('Serializing Word list for future use in: ' + str(qualifiedFileName) + '.') if DEBUG else ''
                pickle_out=open(qualifiedFileName,'wb')
                pickle.dump(self.__words,pickle_out)
                pickle_out.close()
                bench1_stop = time.time_ns()


            except urllib.error.URLError as e:
                print(e.reason)
                self.__words = None
                print("Couldn't create Words list, make sure you are on the Campus Network.")
                exit()

        print("List creation time in milliseconds: ", (bench1_stop - bench1_start)/1000000) if DEBUG else ""

    def getRandWord(self)->str:
        """Method gets a random word from the word list and returns it as a string"""

        if self.__words is None:
                return ""
        index = random.randint(0,len(self.__words) - 1)
        return str(self.__words[index])

    def getRandWordList(self, n=None)->list:
        """Method returns a list of random words adding n words to the list.  If the parameter is
        omitted, the default is 5 words.  The words are unique in each list returned."""

        newList = []
        # Make sure we have a list with values
        if self.__words is None:
            return newList
        # Make sure we have a valid integer datatype as a parameter
        # if not default is set to 5
        if n is not None:
            try:
                num = int(n)
            except ValueError as err:
                print(err," : Returning a list of 5 words\n")
                num = 5
            except Exception as err:
                print(err," : Returning a list of 5 words\n")
                num = 5
        else:
            num = 5
        # make sure they are not asking for more items than we have
        # if so - give them everything we have regardless of what was asked
        if num > len(self.__words):
            num = (len(self.__words))

        # We should be all set now
        bench2_start=time.time_ns()
        for i in range(1, num+1):
            index = random.randint(0,len(self.__words) - 1)
            # Make sure that we aren't duplicating words which is possible
            # with random number generation.
            if self.__words[index] in newList:
                counter = 0
                while (self.__words[index] in newList):
                    counter += 1
                    print("Finding a new word .. already have that one.") if DEBUG else ""
                    index = random.randint(0,len(self.__words) - 1)
                    if self.__words[index] not in newList:
                        newList.append(self.__words[index])
                        print("\tGot one: ", counter, "trys.\n") if DEBUG else ""
                        break
            else:
                newList.append(self.__words[index])
        bench2_stop=time.time_ns()
        print("Word list created with ", len(newList), "items.") if DEBUG else ""
        print("Word List creation time in milliseconds: ",(bench2_stop - bench2_start) / 1000000,"\n") if DEBUG else ""
        return newList

