from bs4 import BeautifulSoup
import requests
import json
from opencage.geocoder import OpenCageGeocode

def crawl_kompas(url, key):
    result = []

    #search only relevant pages
    women=["woman","girl","girls","female","women","lady","daughter","aunt","mother","sister"]
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    
    #find paging page
    pages=[]
    pages.append(url)
    new_pages=soup.find_all("li",{'class':'pager-item'})
    for k in  new_pages:
        pages.append("https://www.indiatoday.in"+k.find('a')['href'])
        pg=1
    for k in pages:
        req_page=requests.get(k)
        soup_page = BeautifulSoup(req_page.text, "lxml")
        
        #list_pages
        paging = soup_page.find_all("div",{'class':'catagory-listing'})
        print(pg)
        pg=pg+1
        for i in paging:
            # page title
            title=i.find('a').text
            title.lower()
            for j in women:
               if j in title:
                    news_link="https://www.indiatoday.in"+i.find('a')['href']
                    req_news = requests.get(news_link)
                    soup_news = BeautifulSoup(req_news.text, "lxml")
                    try:
                        details = soup_news.find("dl",{'class':'profile-byline'})

                        # retrieving location
                        location=details.find_all('dt')
                    except:
                        continue
                    geocoder = OpenCageGeocode(key)
                    query = location[1].text + ',India'
                    results = geocoder.geocode(query)
                    try:
                        state = results[0]['components']['state_code']
                    except:
                        continue
                    print(location[1].text, state)
                    result.append("https://www.indiatoday.in"+i.find('a')['href'])

    print ('a')
    print (result)
    return result

url = 'https://www.indiatoday.in/crime'
crawl = crawl_kompas(url,key='9100acb25e54414aa064c19b6c6a9937')
with open("kompas.json","w") as f:
    json.dump(crawl,f)
