import requests
from bs4 import BeautifulSoup as BS

def hash(key):
    """
    This hash function takes in string key, 
    sums up ASCII value of character
    and take sum % 26 to return an index as integer (0 -> 25)
    """
    sum = 0
    for char in key:
        sum += ord(char)
    
    return sum % 26

def scrape_common_words():
    """
    scrape wikipedia page of 100 most common words
    and return them in a list of strings
    """
    words = [''] * 100
    url = 'https://en.wikipedia.org/wiki/Most_common_words_in_English'
    response = requests.get(url)
    soup = BS(response.content, 'html.parser')
    words_table = soup.find('table').find('tbody').find_all("tr")
    
    for index, w in enumerate(words_table):
        #skip header row
        if index != 0:
            words[index - 1] = w.find('td').get_text()
    return words

def display_graph(arr):
    for i, num in enumerate(arr):
        row = "x"*num
        print("{:3} | {}".format(i, row))


if __name__ == '__main__':
    words = scrape_common_words()
    indices = [0] * 26

    for w in words:
        indices[hash(w)] += 1

    display_graph(indices)



