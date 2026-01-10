# YAWS (Yet Another Web-scraper)
A versatile CLI web scaper tool written in python 

# Rationality
This app is beign made with the express intent of learning how to better use python to interact
both with the web and the linux file system, and a way for me as a student to gather data independently.
There is no malicious intent at play here and i do not condone the use of this software for illegal gathering
of information.

# Functionality
the app will be divided into a couple of different modes:
* Mode 1 - parses the HTML of a webpage and allows the user to write it's contents to a HTML file
* Mode 2 - parses specific HTML tags and allows the user to write it's contents to a text file

# Instalation
* Clone this repository 
* Make script executable ```chmod +x yaws.py```
* Copy or move it to a $PATH directory (```cp yaws.py /usr/your/directory```) or (```mv yaws.py /usr/your/directory```)

# Notes
- Files will always be generated at the current working directory.
- File generation will always use the same file name, that is to say, the program will always overwrite the files it generated if run continuosly. This behaviour can be avoided by renaming the files after generation

