import requests
import bs4

def check_next(next_page):

	for item in next_page:
		try:
			print(item.text)
			if item['aria-hidden'] == 'true':
				return True
		except:
			pass
	return False



i=1
names = []
while True:


	home_url ="https://quotes.toscrape.com/page/{}/".format(i)
	req= requests.get(home_url)
	req_soup = bs4.BeautifulSoup(req.text,'lxml')
	author_data1 = req_soup.select(".author")
	for author in author_data1:
		names.append(author.text)
	next_page = req_soup.select("span")
	print(next_page)
	print(check_next(next_page))
	if check_next(next_page):
		pass
	else:
		break
	i+=1
	break
print(set(names))
