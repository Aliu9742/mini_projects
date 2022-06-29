# This repository contains mini projects I made for fun
## wikipedia scraper
I made this project after learning about webscraping. Given an initial topic with a wikipedia page (ghost, dog, frog), it will jump to the first non-citation link that the crawler hasn't visited yet until it either gets stuck on a page or finds the philosophy page. It will print out the pages it's visiting and how many links it has visited at the end.
The user can provide an initial wikipedia page with -i flag in command prompt. Default is frog if none given.

## int to string
Given an integer between -9999 to 9999, this script outputs the number's name as a string. Use -n flag in command line to give integer

## CracklePop
Made for Recurse Center application.

##Evaluating a simple hash function
This is is side project I made while working on the speller problem for one of CS50's psets. One of the tasks is to load a list of words into a hash table. My idea for a simple hash function is to sum up the ASCII values of all characters in the word and take the value of the sum mod 26. I wanted to see how evenly distributed the output indices are, so I scraped the 100 most common words in the English language from a wikipedia page and put them through my hash function. The results are visualized as a histogram printed in the command prompt. I was pleased with the result that every index had at least 1 word mapped to it, and the most popular index 21 had 8 words mapped to it. Overall, I think this simple hash function should keep my hash table relatively flat. 
