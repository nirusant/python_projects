import argparse
import highlighter
import re
import sys
import os.path

def main(regex_dict, file_directory, highlight):
    """
    Parses the file provided, then uses the provided regex rule(s) to find every instance of string that matches the rule.
    After finding  match the function fetches the whole line.

    If the user wants the text one is searching for highlighted (highlight == true) the string/word that matches the regex gets colored 

    Everthing gets printed on the terminal

    Input: 
        regex_dict, a dictionary containing regex commands.
        file_directory, a list containing names over files we want to search.
        highlight, a boolean telling if the user wants highligthing.
    
    Output:
        none
    """
    if os.path.isfile(file_directory): # checking if file to be searched is a valid file
        with open(file_directory) as text_file: 
            read_text_file = text_file.read() # reading the whole file
            
            color_num = 91 #To cycle between colors the functions loops through values that corresponds to a color
            for regex_key in regex_dict:
                if color_num > 96:
                    color_num = 91

                matches = re.findall(".*" + regex_dict[regex_key]+".*", read_text_file, re.M)# Finding al lines that contains the searchword
                for sentence in matches: #Prints every match 
                    if highlight: #Checks if the highligt flag is invoked
                        print(highlighter.color(regex_dict[regex_key], "0;"+str(color_num), sentence))
                    else:
                        print(sentence) #just prints the line containing the word
                color_num += 1
    else:
        print('The given file does not exist')
        sys.exit()

if __name__ == '__main__':
    """
    Handles the input arguments using argaprse and runs the appropriate functions.
    My understanding of the assignment is that the main purpose of this exercise is to only show how to use regex with grep.
    I have therefore focused on the functionality that facilitates the use of regex, and therefore have not implemented some grep features.
    An example of an unimplemented feature is, being able to give * as an argument to search every file in current directory after the text one want's to search for.
    Another example is to display line number of the line containing the string that matched the search-term. 
    I have made these decisions since the assignment does not spesify how detailed the grep implementation should be.  
    
    Input:
        From terminal,
            * regex, this can either be a single regex, a set of regexes seperated by space.
            * file_directory, a single file you want to search through.
            * (optional) -- highlight, this highlights all the words the regex-rule matched with.

    Output:
        none
    """
    #Using argparse to parse the incoming arguments
    parser = argparse.ArgumentParser(description='A python implementation of grep')
    parser.add_argument('regexcommand', metavar='regex', nargs = '+', help='Regex command for fetching instances that match the given regex')
    parser.add_argument('file_directory', metavar='filedirectory', help='The file you want to search')
    parser.add_argument('--highlight', dest='highlight', action='store_true', help='Highlighting option')
    args = parser.parse_args()
 
    regexcommand = args.regexcommand #Fetching the regex from argparse
    
    regex_dict = {}# An empty dictionary that is going to contain the regex rules
    if len(regexcommand) > 1: #Checking if regexcommand gave us a list with one or more elements.
        #The user has given us several arguments via the terminal
        counter = 1
        for regex in regexcommand:
            txt = 'color' + str(counter) #Giving each regex an unique key when placing it in the dictionary 
            regex_dict[txt] = regex
            counter +=1
    else: # This means that we have a single entry 
        regex_dict = {'color1': regexcommand[0]}# When the input ws s single regex string, the string gets placed in the dictionary  

    main(regex_dict, args.file_directory, args.highlight) #sending the arguments for further processing
