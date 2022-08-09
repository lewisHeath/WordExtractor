# Overview
A web crawler that lists the most used words on a website, has the ability to follow links to a desired depth and continually list the top words.
## Install
```
git clone https://github.com/lewisHeath/WordExtractor.git
cd WordExtractor
pip3 install beautifulsoup4
python3 wordextractor.py
```
## How to use
Simply run the script using Python like...  
`python3 wordextractor.py`  
**Options**:  
**--url**, **-u**     &emsp;           TEXT       &emsp;     URL of the webpage to extract from.  
**--length**, **-l**    &emsp;      INTEGER    &emsp;     Minimum word length (default: 0, no limit).  
**--amount**, **-a**     &emsp;     INTEGER    &emsp;     Amount of top words to print (default: 10).  
**--link-depth**, **-ld**  &emsp;   INTEGER    &emsp;     The depth of how many links to trace. (default:1)  
**--help**                                    Show this message and exit.