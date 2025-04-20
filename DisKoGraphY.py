from bs4 import BeautifulSoup, SoupStrainer
import requests

def DiscoG(url):
	if "?u" in url: url = url.replace("?u", "")

	response = requests.get(url)

	ayy = []

	for link in BeautifulSoup(response.text, 'html.parser', parse_only=SoupStrainer('a')):
		if link.has_attr('href') and "album" in link['href']: # or "track" in link['href'])
			if "https://tidal.com" + link['href'] not in ayy: ayy.append("https://tidal.com" + link['href'])

	return ayy