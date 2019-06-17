import re
import sys
import os.path

def get_regex_rules(regex_file):
    """
    Parses the input and extracst given regex rules and it's corresponding comment. 
    After extraction the data is placed in a dictionary.  

    Input:
	regex_file, a file containing regex rules

    Output:
        regex_dict, dictionary containing all the rules we want to use 
    """
    #Checking if the syntaxfile follows the set syntax    
    file = open(regex_file,"r")
    regex_rules = file.read()

    if not re.match("^\".{0,}\"", regex_rules): #checking if the first string in file starts with " and stops with ". 
        print('The provided syntaxfile seems not to contain any regex rules')
        sys.exit()
    # You forgot to write an r here, it should be: r": (\w{1,})"
    comments = re.findall(r": (\w{1,})",regex_rules, re.M) #Fetching the comments

    regex_dict = {}#Declaring an empty dictionary
    rules = re.findall("\"(.*)\"",regex_rules, re.M) #Fetching all rules made
    for i in range(len(rules)):
        regex_dict[comments[i]] = rules[i]
    
    file.close()
    return regex_dict 		

def get_themes(theme_file):
    """
    Parses the input and extracts colors that correspond to a rule. 
    After extraction the data is placed in a dictionary.
  
    Input:
        theme_file, a file containing a color and what regex-rule should be colored
    Output:
        theme_dict, dictionary containing all the colors we want to use 
    """
    
    file = open(theme_file)
    theme_text = file.read()
    colors = re.findall("0;.[0-9]",theme_text)

    theme_dict = {}
    
    # You forgot to write an r here, it should be: r"(^\w{1,}):"
    comments = re.findall(r"(^\w{1,}):",theme_text, re.M) #Fetching the comments
    for i in range(len(comments)):
        theme_dict[comments[i]] = colors[i]
    
    file.close()
    return theme_dict

def color(rule, color_val, out):
    """
    Given a regex rule an a color_value, the part of the text that matches the the regex gets colored.  
    
    Input:
        rule, a regex rule
        color_value, the color we want to color all instances of text that match the regex rule.
        out, text we want to color
    
    Output:
        out, the colored text        
    """
    # I added an r to this part to
    line_fix =r"(\\033\[\d+;\d+m)((?:(?!\\033\[0m).)*)(\\033\[\d+;\d+m)(.*?)(\\033\[0m)" # Colors text when there is a different color
    out = re.sub("("+rule+")", ("\033[{}m".format(color_val) + r"\1" + "\033[0m"), out, flags=re.M) #Colors a word 
    out = re.sub(line_fix, (r"\1\2" + "\033[0m" + r"\3\4\5\1"), out, flags=re.M) #fixing line
    return out

def color_text(target_file, regex_dict, theme_dict):
    """
    Highlights the provided text based on regex-rules and colors provided by the user

    Input:
        target_file, textfile we want to hightlight  
        regex_dict, a dictionary containing regex-rules
        theme_dict, a dictionary containing a color for each rule implemented 

    Output:
        out, a string containig the file we have colored
    """
    with open(target_file) as text_file: #Opens the text
        read_text_file = text_file.read() 
        out = read_text_file #The final output

        for color_key, color_val in theme_dict.items():
            if color_key in regex_dict:
                rule = regex_dict[color_key]
                out = color(rule, color_val, out)
    return out

def main(syntax, theme, target_file):
    """
    Calls appropiate functions that converts the necesarry files to dictionaries.
    The converted files with the file we want to highlight is then sent to a function that does the highlighting.
    The highlighted text is the printed on the terminal

    Input:
        syntax, a file containing regex-rules.
        theme, the desired theme containing different colors for different regex-rules.
        target_file, the file we want to color.

    Output:
        none
    """
    #Getting regex rules and the appropriate comment
    regex_dict = get_regex_rules(syntax)
                 
    #Getting the colors for the provided theme
    theme_dict = get_themes(theme)
   
    #Colors text
    colored_text = color_text(target_file, regex_dict, theme_dict)
    
    #Displaying text in terminal
    print(colored_text)
    
					
def help():
    """
    Function that is called to provide help regarding running this file
    
    Input:
        none
    
    Output:
        none
    """

    print("""Help screen for highlighter.py

    How to call this program with desired files:
        python3 highlighter.py syntaxfile themefile sourcfile_to_color
    
    syntaxfile:
        A file containing regex commands

    themefile:
        A file containing the colourscheme

    source_file_to_color:
        The file you want to color 
    """)

if __name__ == '__main__':
    """
    Checking if arguments are given and calling functions accordingly 

    Input:
        - From terminal three files:
            *syntax, a file containing regex-rules.
            *theme, a file with desired theme containing different colors for different regex-rules.
            *target_file, the file we want to color.
    Output:
        none
    """

    if len(sys.argv) == 4:
        if os.path.isfile(sys.argv[1]) and os.path.isfile(sys.argv[2]) and os.path.isfile(sys.argv[3]):
            main(sys.argv[1], sys.argv[2], sys.argv[3])
        else:
           print('Did not find one or more files, redirecting to help screen\n') 
           help()
           sys.exit()                   
    else:
        print('Necessary files not given, redirecting to help screen \n')
        help()
        sys.exit()

