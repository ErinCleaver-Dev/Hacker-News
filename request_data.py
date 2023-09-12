#https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# allows you to download the html
import requests 
# allows you to script the data with python
from bs4 import BeautifulSoup

# used to dipslay different error messages 
def error_message(txt, err):
    return f'{txt}: {err}'

def request_url(url):
    """
        Used to request a url and test if it has sucessfully connected

        returns True and the request if it has connected
        returns False and a error message if it failes to connect 

        Returns: True, res
        Returns: False, err
    """
    try:
        # requests the url
        res = requests.get(url)
        # returns a error message if the server dose not give a 200
        if res.status_code == 200:
            return True, res
        else:
            return False, 'Failed to to connect to website'
    # if something that is not a string is put in as the url, it will give a error.
    except TypeError as err:
        return False, error_message('Failed to find website', err)
    


         