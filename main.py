import request_data
import hacker_news
import pprint

#setup to automically get a number of page numbers and print them out based on a range
for page_number in range(1,7):
    #prints the page number 
    print(f'page {page_number}')

    #gets a boolen and a res
    boolen, res =request_data.request_url(f'https://news.ycombinator.com/?p={page_number}')
    #prints out the hacker news function using pretty print
    pprint.pprint(hacker_news.get_hacker_news(res, boolen))