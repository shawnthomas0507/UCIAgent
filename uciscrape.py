import requests
import bs4
from bs4 import BeautifulSoup

def scrape(dataset_name):
    response=requests.get("https://archive.ics.uci.edu/ml/datasets/"+dataset_name)

    soup=BeautifulSoup(response.content,"html.parser")
    content=soup.find_all('pre')
    all_code = ""
    for snippet in soup.find_all('pre'):
        code = snippet.get_text(strip=True)
        if code:  
            all_code += code + "\n" 
    return all_code