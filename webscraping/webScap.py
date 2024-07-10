import requests
import bs4
# Sending request to the web page(URL)
URL ="https://www.yahoo.com"

response =requests.get(URL)
parsed_data=bs4.BeautifulSoup(response.text)
all_links=parsed_data.select('a')
#print(len(all_links))
for l in all_links:
    print(l.attrs)


