# This repository contains mini projects I made for fun
## wikipedia scraper
I made this project after learning about webscraping. Given an initial topic with a wikipedia page (ghost, dog, frog), it will jump to the first non-citation link that the crawler hasn't visited yet until it either gets stuck on a page or finds the philosophy page. It will print out the pages it's visiting and how many links it has visited at the end.
The user can provide an initial wikipedia page with -i flag in command prompt. Default is frog if none given.
