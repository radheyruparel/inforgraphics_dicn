#
##Author: Radhey Ruparel
##Description: This program reads in a text file (perhaps containing the contents of a book, poem, article, etc) 
##and produces an infographic based on the text. The inforgraphic is a display of bar graphs, it shows word lenght, 
##cap/non-cap and punct/non-punct on these graphs. 
#

#Required to import all the os functions and program is able to locate the file
import os
os.chdir(os.path.dirname(__file__))

#Importing all the modules for the program execution  
import sys

#Important code for using graphics.py
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, cwd)
from graphics import graphics

def processing_the_words(selected_file):
    
    '''This function will read the user selected files, and load all the words from the text file
    into list.
    This function has parameter varaible as selected_file, which is a string.'''
   
    #The main list of words
    words=[]
   
   #Opening the user selected file
    file_choosen=open(selected_file,'r')
    
    #This loop will read the file, and split lines into single words and then load them into a word list
    for lines in file_choosen:
        
        #Striping the default \n from 
        line=lines.rstrip('\n')
        #Splitting the line into words
        line_words=line.split(' ')
        
        #Loading those words into a word list
        for word in line_words:
            words.append(word)
    
    #Closing the user selected file
    file_choosen.close()
    
    #Retuning the words list for futher processing
    return words

def unique_words(gui,selected_file):
    
    '''This funtion will use the total words, and find unique words in them. These unique words will be
    load into a dictonary. With the uniques word as key and number of repeatation as value.
    This function has parameter varaible as selected_file, which is a string.
    Another parameter varaible is gui, which is graphic'''
    
    #Calling this function would give the total word list into this functiion
    words=processing_the_words(selected_file)
    
    #Declaring a dictonary to store unique words
    words_count={}
    
    #This loop will find load the unique words in
    for word in words:
        #If the words in not in the dictonary then add it 
        if word not in words_count:
            words_count[word]=0
        #If the word is repeated then increase the value by one
        words_count[word]+=1
    
    #If the dictonary as empty strings while reading the file, then remove them
    if '' in words_count:
        del words_count['']
    
    #Printing on the canvas the total unique words
    gui.text(50,70,'Total Unique Words: '+str(len(words_count)),'white',25)
    return words_count

def detemining_the_word_length(gui,selected_file):
    
    '''This funtion will use unique words dictonary and categories those into short, medium and large, 
    based on their word length.
    This function has parameter varaible as selected_file, which is a string.
    Another parameter varaible is gui, which is graphic'''
    
    #Calling this function would give the unqiue words dictonary into the this function
    words_count=unique_words(gui,selected_file)
    
    #Declaring a dictonary to store short words
    short_words={}
    
    #Declaring a dictonary to store medium words
    medium_words={}
    
    #Declaring a dictonary to store large words
    large_words={}
    
    #This loop will will segrate unique words into short, medium and large
    for unique_word in words_count:
        #The words is considered to be short if it is length is equal or less than 4
        if len(unique_word)<=4:
            #This load short words into short_words dictonary
            short_words[unique_word]=words_count[unique_word]
        
        #The words is considered to be short if it is length is equal or greater than 5 and equal or less than 7
        if len(unique_word)>=5 and len(unique_word)<=7:
            #This load medium words into medium_words dictonary
            medium_words[unique_word]=words_count[unique_word]
        
        #The words is considered to be short if it is length is equal or greater than 8
        if len(unique_word)>=8:
            #This load large words into large_words dictonary
            large_words[unique_word]=words_count[unique_word]
    
    #Declaring a int varible to represent the time of repeatation for most short repeated short words
    value_short_word=0
    #Declaring a string varible to represent most short repeated short words
    most_ocurring_short_word=''
    #This loop will idenfity the most repeated short word
    for short_word in short_words:
        if value_short_word<short_words[short_word]:
            value_short_word=short_words[short_word]
            most_ocurring_short_word=short_word
    
    #Declaring a int varible to represent the time of repeatation for most medium repeated short words
    value_medium_word=0
    #Declaring a string varible to represent most medium repeated short words
    most_ocurring_medium_word=''
    #This loop will idenfity the most repeated medium word
    for medium_word in medium_words:
        if value_medium_word<medium_words[medium_word]:
            value_medium_word=medium_words[medium_word]
            most_ocurring_medium_word=medium_word
    
    #Declaring a int varible to represent the time of repeatation for most large repeated short words
    value_large_word=0
    #Declaring a string varible to represent most large repeated short words
    most_ocurring_large_word=''
    #This loop will idenfity the most repeated large word
    for large_word in large_words:
        if value_large_word<large_words[large_word]:
            value_large_word=large_words[large_word]
            most_ocurring_large_word=large_word

    #This will print the file name has the top main heading on the infographic canvas
    gui.text(50,25,selected_file,'cyan',30)
    #This will printthe static text Most used words (s/m/l): on the
    gui.text(50,110,'Most used words (s/m/l):','white',20)
    #This will print most repeated short word with its times of repeatation into the infographic canvas
    gui.text(275,110,most_ocurring_short_word+'('+str(value_short_word)+'x)','cyan',20)
    #This will most repeated medium word with its times of repeatation into the infographic canvas
    gui.text(375,110,most_ocurring_medium_word+'('+str(value_medium_word)+'x)','cyan',20)
    #This will print most repeated large word with its times of repeatation into the infographic canvas
    gui.text(485,110,most_ocurring_large_word+'('+str(value_large_word)+'x)','cyan',20)
    
    #Determinging the lenght of the bar for short words
    bar_height_short_words=((450/len(words_count))*len(short_words))
    #Determinging the lenght of the bar for medium words
    bar_height_medium_words=((450/len(words_count))*len(medium_words))
    #Determinging the lenght of the bar for large words
    bar_height_large_words=((450/len(words_count))*len(large_words))
    
    #This will print static heading of the bar graph
    gui.text(50,150,'Word Lenghts','white',20)
    
    #This will print bar for the short words on the whole graph
    gui.rectangle(50,175,150,bar_height_short_words,'cyan')
    gui.text(60,180,'small words','white',15)

    #This will print bar for the medium words on the whole graph
    gui.rectangle(50,175+bar_height_short_words,150,bar_height_medium_words,'green')
    gui.text(60,180+bar_height_short_words,'medium words','white',15)

    #This will print bar for the large words on the whole graph
    gui.rectangle(50,175+bar_height_short_words+bar_height_medium_words,150,bar_height_large_words,'cyan')
    gui.text(60,175+bar_height_short_words+bar_height_medium_words,'large words','white',15)



def counting_capitalized_words(gui,selected_file):
    
    '''This funtion will use unique words dictonary and categories those into capitalized and non capitalized
    words.
    This function has parameter varaible as selected_file, which is a string.
    Another parameter varaible is gui, which is graphic'''
   
    #Calling this function would give the unqiue words dictonary into the this function
    words_count=unique_words(gui,selected_file)
    
    #This is a varible which will count the capitalized words
    capitalized_words=0
    #This loop will look at the frist letter of the word and determine if it is capitalized or not
    for word in words_count:
        #Slicing the frist letter
        frist_letter=word[0]
        #If the frist word is capitalized, then add one the count
        if frist_letter.isupper()==True:
            capitalized_words+=1
    
    #This is a varible which will count the non capitalized words
    non_capitalized_words=len(words_count)-capitalized_words
    
    #Determinging the lenght of the bar for capitalized words
    bar_height_capitalized_words=((450/len(words_count))*capitalized_words)
    #Determinging the lenght of the bar for non capitalized words
    bar_height_non_capitalized_words=((450/len(words_count))*non_capitalized_words)
    
    #This will print static heading of the bar graph
    gui.text(250,150,'Cap/Non-Cap','white',20)
    
    #This will print bar for the capitalized words on the whole graph
    gui.rectangle(250,175,150,bar_height_capitalized_words,'cyan')
    gui.text(255,180,'Captaized','white',15)
    
    #This will print bar for the capitalized words on the whole graph
    gui.rectangle(250,175+bar_height_capitalized_words,150,bar_height_non_capitalized_words,'green')
    gui.text(255,180+bar_height_capitalized_words,'Non Captaized','white',15)

def punctuation_word_count(gui,selected_file):
    
    '''This funtion will use unique words dictonary and categories those into puncted and non puncted
    words.
    This function has parameter varaible as selected_file, which is a string.
    Another parameter varaible is gui, which is graphic'''
    
    #Calling this function would give the unqiue words dictonary into the this function
    words_count=unique_words(gui,selected_file)
    
    #This is a varible which will count the punctuated word
    count_punctuation_word=0
    
    #This loop will look at the last letter of the word and determine if it is punctuated or not
    for word in words_count:
        #Slicing the last letter
        last_charc=word[-1]
        #If the last word is punctuated, then add one the count. Punctuation such as '!','.',',','?'
        if last_charc=='!' or last_charc=='.' or last_charc=='?' or last_charc==',':
            count_punctuation_word+=1
    
    #This is a varible which will count the non punctuated words
    non_count_punctuation_word=len(words_count)-count_punctuation_word
   
    #Determinging the lenght of the bar for punctuated words
    bar_height_count_punctuation_word=((450/len(words_count))*count_punctuation_word)
    #Determinging the lenght of the bar for non punctuated words
    bar_height_non_count_punctuation_word=((450/len(words_count))*non_count_punctuation_word)
    
    #This will print static heading of the bar graph
    gui.text(450,150,'Punct/Non-Punct','white',20)
    
    #This will print bar for the punctuated words on the whole graph
    gui.rectangle(450,175,150,bar_height_count_punctuation_word,'cyan')
    gui.text(455,180,'Punctuated','white',15)

    #This will print bar for the non punctuation words on the whole graph
    gui.rectangle(450,175+bar_height_count_punctuation_word,150,bar_height_non_count_punctuation_word,'green')
    gui.text(455,180+bar_height_count_punctuation_word,'Non Punctuated','white',15)


#Declaring the main function
def main():
    #This prints out the canvas of 650 by 700 pixils
    CANVAS_HEIGHT=650
    CANVAS_WIDTH=700
    #Creating a Graphical Canvas 
    gui=graphics(CANVAS_WIDTH,CANVAS_HEIGHT,'Infographic') 
    #Making the canvas with a black background
    gui.rectangle(-100,-100,850,900,'black')
    
    #User is selecting the text file for the program
    selected_file=input('Enter a text file: ')
    
    #Calling this function will print the bar graph of the lengh of the words
    detemining_the_word_length(gui,selected_file)
    #Calling this function will print of the bar graph capitalized and non capitalized words
    counting_capitalized_words(gui,selected_file)
    #Calling this functiion will print the bar graph punctuated and non punctuation words
    punctuation_word_count(gui,selected_file)

#Calling the main function
main()