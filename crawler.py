# . /tmp/crawler/bin/activate
import requests
import bs4

base_url = "https://www1.gogoanime.ai"
##keyword = input("anime search : ")
keyword = "kuroko no"
url = f"{base_url}//search.html?keyword={'%20'.join(keyword.split())}"

resp1 = requests.get(url)

soup1 = bs4.BeautifulSoup(resp1.content, features="html.parser")

link = soup1.find_all("p", attrs={"class":"name"} )

no = 1
for i in link:
        list = i.contents[0].contents[0]
        #print(str(no)+". "+str(list) )
        no += 1
#print('')
#print('')

no = 1
search_url_finds = []
for i in link:
        listi = i.contents[0]
        search_url_finds.append(str(base_url) + str(listi.get('href')))
        #print(str(no) + ". " + search_url_finds[no-1])
        print(listi.get('href'))
        no += 1


#'https://ajax.gogo-load.com/ajax/load-list-episode?ep_start=0&ep_end=25&id=1512&default_ep=0&alias=kuroko-no-baske' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0' -H 'Accept: text/html, */*; q=0.01' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Origin: https://www1.gogoanime.ai' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Referer: https://www1.gogoanime.ai/' -H 'Cache-Control: max-age=0' -H 'TE: Trailers'

resp2 = requests.get(search_url_finds[0])
print(search_url_finds[0])
soup2 = bs4.BeautifulSoup(resp2.content, features="lxml")
#print(soup2.prettify)
link = soup2.find("ul", attrs={"id":"episode_related"})
#link = soup2.find("div",attrs={"id":"load_ep"})
print(link)

#print(len(link))
#for i in link:
#        print(i.contents)

