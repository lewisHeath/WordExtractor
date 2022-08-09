# Python Word Extractor
A web crawler that lists the most used words on a website, has the ability to follow links to a desired depth and continually list the top words.
## Install
Git clone
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
**-u**, **--url**    &emsp;           TEXT       &emsp;     URL of the webpage to extract from.  
  **-l**, **--length**    &emsp;      INTEGER    &emsp;     Minimum word length (default: 0, no limit).  
  **-a**, **--amount**     &emsp;     INTEGER    &emsp;     Amount of top words to print (default: 10).  
  **-ld**, **--link-depth**  &emsp;   INTEGER    &emsp;     The depth of how many links to trace. (default:1)  
  **--help**                                    Show this message and exit.