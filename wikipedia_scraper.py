import requests
from bs4 import BeautifulSoup as BS
import time
import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description="given a topic with wikipedia page, hop to the next first link on the page until reaching philosophy page or gets stuck on same page")
    parser.add_argument("-i", type=str, help="topic with wikipedia page like frog", default="frog")
    return parser.parse_args()

def wiki_crawler(extension):
    url = 'https://en.wikipedia.org/wiki/'

    previous_request = ""
    current_request = url + extension
    response = requests.get(current_request)

    counter = 0
    urls_visited = [extension]

    
    while previous_request != current_request and extension != "Philosophy":
        previous_request = url + extension
        print(current_request)
        print('------------')

        soup = BS(response.content, 'html.parser')
        content = soup.find('div', id='bodyContent', class_='vector-body')
        paragraphs = content.find_all('p')

        for p in paragraphs:
            break_flag = False
            links = p.find_all('a')
            if len(links) != 0:
                for index, link in enumerate(links):
                    #[6:] gets the web page topic without /wiki/
                    extension = links[index]['href'][6:]
                    #print("extension:{}".format(extension))
                    
                    if extension in urls_visited:
                        print(extension, ' has been visited')
                    elif 'cite_note' in links[index]['href']:
                        print(links[index]['href'], ' is a citation')
                    else:
                        #set break_flag to true once a link has been found
                        break_flag = True
                        break

            #stop looking for links in the current paragraph
            if break_flag:
                break

        current_request = url + extension
        response = requests.get(current_request)
        
        
        urls_visited.append(extension)
        counter += 1

        #avoid making too many requests at once
        time.sleep(0.5)
    if previous_request == current_request:
        return False, counter-1
    else:
        return True, counter-1

if __name__ == "__main__":
    args = get_args()
    reaches_philophy, count =  wiki_crawler(args.i)

    if reaches_philophy:
        print("Arrived at philosophy in {} links".format(count))
    else:
        print("Visited {} links but did not find philosophy".format(count))