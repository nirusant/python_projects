<H1>INF4431 - Assignment 5 </H1>

<H2>Practical information</H2>
<b> Operating  system:</b> Ubuntu 18 <br />
<b> Terminal:</b> Gnome terminal 3.28.2 <br />


<H2>The assignement tasks</H2>

<H3>5.1 Syntax highlighting:</H3>
General usage: python3 highlighter.py syntaxfile themefile sourcefile_to_color  <br />

To see the results when using highlighter.py with the provided natyhon files, please look in the images folder and open task5_1.png  

<H3>5.2 Python syntax:</H3> 
The things I have tried to syntaxhighlight:

<ol type="1">
 <li>Comments</li>
 <li>Function definitions</li>
 <li>Class definitions</li>
 <li>Strings</li>
 <li>Imports</li>
 <li>"Special" statements None, True, False</li>
 <li>Decorators</li>
 <li>for-loops</li>
 <li>while-loops</li>
 <li>if/elif/else blocks</li>
</ol> 

The theme file are based on the standard syntaxhighlighting provided by the neovim editor, running on a Gnome terminal 

<H4>Usage:</H4>
python3 highlighter.py python.syntax python.theme hello.py  <br />
or <br />
python3 highlighter.py python.syntax python2.theme hello.py  <br />
or <br />
python3 highlighter.py python.syntax python.theme highlighter.py <br /> 
or <br />
python3 highlighter.py python.syntax python2.theme highlighter.py <br /> 

Images of the first two usages are available in the images folder, the two images are task5_2_theme1.png and task5_2_theme2.png

<H3> 5.3 Syntax for your favorite language (Bonus)</H3>
The language I have chosen is Java, and  the things I have tried to syntaxhighlight are:

<ol type="1">
 <li>Comments</li>
 <li>Function definitions</li>
 <li>Class definitions</li>
 <li>Strings</li>
 <li>Imports</li>
 <li>"Special" statements None, True, False</li>
 <li>for-loops</li>
 <li>while-loops</li>
 <li>if/elif/else blocks</li>
 <li>integer highligthing</li>
</ol>
The theme file are based on the standard syntaxhighlighting provided by the neovim editor, running on a Gnome terminal

<H4>Usage:</H4>
python3 highlighter.py java.syntax java.theme hello.java  <br />
<br />
An image of this usage is available in the images folder, task5_3.png.

<H3>5.4 Grep </H3>
To test grep.py I have used the text file grep_text.txt. 
I have also used my grep on the python files in this folder.
Usage examples are provided.

<H4> Usage:</H4>
General usage: grep.py [--highlight] regex [regex ...] filedirectory
<br /> <br />
Some usage examples:
<br />
python3 grep.py CD grep_text.txt
<br />
python3 grep.py --highlight CD grep_text.txt  
<br />
python3 grep.py --highlight CD book "\sbook\s" "b(?:ow)" "\sl\w{1,}" grep_text.txt  
<br />
python3 grep.py --highlight "\w{1,}(?=\()" highlighter.py   
<br/> 
The last usage example is by taking a regex command in python.syntax and giving it to grep.py. 
<br/><br/>    

Images of the three last usages is available in in the images folder. 
These images are task5_4_grep1.png, task5_4_grep2.png and task5_4_grep3.png 

<H3>5.5 Superdiff </H3>

<H4> Usage: </H4>
General usage: python3 diff.py [-h] original_file modified_file
<br /> <br />
Some usage examples:
<br />
python3 diff.py diff_original.txt diff_modified.txt
<br />
python3 diff.py diff_modified.txt diff_original.txt
<br />
By switching places one can test both insertion and deletion.  

<H3>5.6 Coloring diff </H3>
<H4> Usage: </H4>
python3 highlighter.py diff.syntax diff.theme diif_output.txt  <br/>
<br/><br/>    
An image of the result using this is found in the images folder, name of image is task5_6.png


