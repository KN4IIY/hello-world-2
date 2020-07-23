#! /usr/bin/python3

from requests_html import HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

article = html.find('div.article', first=True)
headline = article.find('h2', first=True)
summary = article.find('p', first=True)

print(headline.text)
print(summary.text)
