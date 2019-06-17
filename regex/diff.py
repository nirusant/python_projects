import argparse
import highlighter
import re
import sys
import os.path


def save_text(text):
    """
        Writes a texfile to disc.    
    
    Input:  
        text, a list where each element is a textline

    Output:
        a texfile to current director
    """
    file = open('diff_output.txt', "w")
    for line in text:
        file.write(line)    
    file.close()

def diff(original, modified):
    """
    To implement diff there have been done some assumptions and this reflects on how this task has been solved.
    The assumptions wil be made clear as you read the code line by line. 
    There are two main assumptions.

    The overarching logic that has been used to solve this task that, each possible scenario(line deletion/insertion, deletion/insertion of a character) is going to invoke different "states".
     These states are based on different tests and assumptions.
    
    Input:
        original, a list where each element is a line from the original textfile
        modified, a list where each element is a line from the modified textfile

    Output:
        text_out, a list where each element contains a line, where the line starts with 0:, +: or -:, indicating change or not.               
    """

    """
    MODIFIED:

    Here I'm going to change when a character is deleted/inserted from/to the line, because when you do so the diff_output will be wrong
    if you run: 
        - diff.py diff_original diff_modified
    you get the diff_output.txt file, and then after you run:
        - python3 highlighter.py diff.syntax diff.theme diff_output.txt
    the output would be:
        -:AB
        0:DEF
        +:GHS
        0:JKL
        +:MNO
        +:PQR
    But this is wrong since you added AB, you didnt delete it, the original file had ABC, and because you search for charachters that was deleted you get - instead of +.
    The other case is GHS there you do the same thing but this time it makes it right, but that's hust because you insert S after deleting I. 
    Therefore its best to remove the charachter matching and just check if the lines are equal. The output should look like this:
        -:ABC
        +:AB
        0:DEF
        -:GHI
        +:GHS
        0:JKL
        -:
        +:MNO
        +:PQR

    So everything you did was good and right, but the way you added it to text_out needed to be modified.
    """
    text_out = []
    while len(original) > 0 and len(modified) > 0:
        """
        Val1 and val2 represent the different states the while-loop can be inn.
        The states val1, val2 can be inn are:
         Val1 Val2 
          1    1 Default/catch all state.
          1    0 A character has been deleted.
          0    1 A character had been inserted.
          0    0 The line has not been altered.
        """
        #Default state
        val1 = 1 
        val2 = 1 

        if original[0] == modified[0]: 
            #The lines are similar
            val1 = 0
            val2 = 0
        else:
            """ 
            If the lines are not similar there are four possible reasons: 
               A character in the line has been deleted
               A character in the line has veen insterted
               An extra line has been insterted
               A line has been deleted
            """
                
            #The two nex for-loops is designed with a assumption in mind:
            #Assumption1: If one line has had an insertion and a deletion, the insertion is considered more important this leads to +:
            for char in original[0]: #Checking each character for deletion
                if(modified[0].find(char) == -1):
                    print('deleted', char)
                    val1 = 1
                    val2 = 0

            for char in modified[0]: #Checking each character for insertion
                if(original[0].find(char) == -1):
                    print('insterted', char)
                    val1 = 0
                    val2 = 1

        #These statements checks what state the current line ended up inn.    
        if(val1 == 0 and val2 == 0 ):
            print('No change')
            text_out.append("0:"+modified[0])
            original.remove(original[0])
            modified.remove(modified[0])

        elif(val1 == 0 and val2 == 1):
            #Modification/character was inserted to line
            text_out.append("-:"+original[0])
            text_out.append("+:"+modified[0])
            original.remove(original[0])
            modified.remove(modified[0])

        elif(val1 == 1 and val2 == 0):
            #deletion/character was deleted from line
            text_out.append("-:"+original[0])
            text_out.append("+:"+modified[0])
            original.remove(original[0])
            modified.remove(modified[0])

        elif(val1 == 1 and val2 == 1):
            #If the line contains the same characters, but the sequence of characters have changed this counts as a modification 
            text_out.append("+:"+modified[0])
            original.remove(original[0])
            modified.remove(modified[0])
            
        if(len(original) == 0 and len(modified) > 0):
            #Assuming that the modified file has more lines in the bottom than the original file
            print("Line insertion")
            text_out.append("+:"+modified[0])
            modified.remove(modified[0])
    
        if(len(modified) == 0 and len(original) > 0):
            #Assuming that the modified has less lines in the bottom than the original file
            print("Line deletion")
            text_out.append("-:"+" ")
            original.remove(original[0])
            
    #Assumption2: A line is only not modified(0:) if it is in the same linenumber in both files, everythin else is either a deletion or modification

    return text_out

if __name__ == '__main__':
    """
    When called makes sure if the proper arguement are given and runs appropiate functions 

    Input:
        from terminal
            original_file, a file wit some text
            modified_file, an altered version of the original_file
     
     Output:
        none
    """

    parser = argparse.ArgumentParser(description='Superdiff: A python implementation of diff ')
    parser.add_argument('original_file', metavar='original_file', help = 'The file before changes')
    parser.add_argument('modified_file', metavar='modified_file', help= 'The file after changes')
    
    args = parser.parse_args()

    original = args.original_file
    modified = args.modified_file

    if os.path.isfile(original) and os.path.isfile(modified):
        original_text = open(original, "r")
        modified_text = open(modified, "r")
        new_text = diff(original_text.readlines(), modified_text.readlines())
        save_text(new_text)
    else:
        print('Did not find the specified files')
        sys.exit()
