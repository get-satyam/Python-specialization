import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter Url: ")
count = 7
position = 18
for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)

    tags = soup("a")
    s = list()  
    t = list()
    for tag in tags:
        x = tag.get("href", None)
        s.append(x)
        y = tag.text
        t.append(y)

    print(s[position - 1])
    print(t[position - 1])
    url = s[position - 1]
