from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import time
from opencage.geocoder import OpenCageGeocode
import nltk
from nltk.corpus import stopwords

def crawl_kompas(url, key):
    # the frontier
    result = []
    newsdf = pd.DataFrame(columns=['Title','City','State','StateCode'])

    # search only relevant pages
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    
    # find paging page
    pages=[]
    pages.append(url)
    new_pages=soup.find_all("li",{'class':'pager-item'})

    # removing stop words from title
    cachedStopWords = set(stopwords.words('english'))

    for k in new_pages:
        pages.append("https://www.indiatoday.in"+k.find('a')['href'])
        pg=1

    for k in pages:
        req_page=requests.get(k)
        soup_page = BeautifulSoup(req_page.text, "lxml")
        
        # list_pages
        paging = soup_page.find_all("div",{'class':'catagory-listing'})
        pg = pg+1

        # searching for only relevant pages
        women = re.compile(r'.*(woman|girl|girls|female|women|lady|daughter|aunt|mother|sister|wife|wives)+.*')
        for i in paging:
            # page title
            title = i.find('a').text
            if women.search(title):
                # visiting new link
                news_link="https://www.indiatoday.in"+i.find('a')['href']
                req_news = requests.get(news_link)
                soup_news = BeautifulSoup(req_news.text, "lxml")
                try:
                    details = soup_news.find("dl",{'class':'profile-byline'})
                    # retrieving location
                    location = details.find_all('dt')
                except:
                    continue
                geocoder = OpenCageGeocode(key)
                query = location[1].text + ',India'
                qresults = geocoder.geocode(query)
                try:
                    state_code = qresults[0]['components']['state_code']
                    state = qresults[0]['components']['state']
                    city = location[1].text

                    # cleaning data
                    city = city.strip()
                    title = ' '.join(
                        [word for word in title.split() if word not in cachedStopWords])
                    title = title.strip().upper()
                    
                    result = [title, city, state, state_code]
                    print(result)

                    newsdf.loc[len(newsdf)] = result
                except:
                    continue
    return newsdf

if __name__ == '__main__':
    web_url = 'https://www.indiatoday.in/crime'
    api_key = '9100acb25e54414aa064c19b6c6a9937'
    crawl = crawl_kompas(url=web_url, key=api_key)
    print(crawl)

    # saving the dataframe
    timestamp = str(int(time.time()))
    crawl.to_csv('news-' + timestamp + '.csv')
