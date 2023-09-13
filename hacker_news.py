from bs4 import BeautifulSoup

def sort_stories_by_votes(stories):
    return sorted(stories, key= lambda key:key['score'], reverse=True)

def get_hacker_news(res, boolen = False):
    """
    Give the res data and a boolen to verifiy that you have connected to the server.
    """
    if boolen:
        soup = BeautifulSoup(res.text, 'html.parser')
        info = list(zip(soup.select('.subtext'), soup.select('.titleline>a')))
        hacker_news = []
        try:
            for subtext, link in info:
                    score = subtext.find('span', class_ ='score')
                    age = subtext.find('span', class_ ='age')
                    try:
                        score = score.getText().strip(' points')
                        age = age.getText()
                        score = int(score)
                    except:
                        score = 0
                    if score > 100 and link != '' and age.__contains__('hours ago'):
                        url = link['href']
                        title = link.getText()
                        if(url.startswith('item?id')):
                            continue
                        else:
                            hacker_news.append({'score': score, 'title': title, 'url': url})
        except AttributeError as err:
            print(err)
        except ValueError as err:
            print(err)

        return sort_stories_by_votes(hacker_news)
               
    elif boolen == False and res.status_code == 200:
        return f'Failed to provide True and connected to server.'
    else: 
        return f'Error when connecting to server: {res}.'

    
