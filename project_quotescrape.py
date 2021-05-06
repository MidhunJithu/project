import requests
import bs4

# to import the homepage
home_url ="https://quotes.toscrape.com/" 
req_result = requests.get(home_url)
page_content = bs4.BeautifulSoup(req_result.text,"lxml")
author_data = page_content.select(".author")
#quote_data = page_content.select(".text")
#top_tag_data= page_content.select(".tag-item")
next_page = page_content.select("span")

authors =[]

def authour_collect(author_data):
	for author_name in author_data:
		if author_name.text not in authors:
			authors.append(author_name.text)
	print(authors)
#for quote in quote_data:

#   print(quote.text)
#for tag in top_tag_data:
#	print(tag.text)
def check_next(next_page):

	for item in next_page:
		try:
			if item['aria-hidden'] == 'true':
				return True
		except:
			pass
	return False

if __name__ == '__main__':
	authour_collect(author_data)
	
	goto =check_next(next_page)
	home_url ="https://quotes.toscrape.com/page/{}/"
	req= requests.get(home_url.format('5'))
	req_soup = bs4.BeautifulSoup(req.text,'lxml')
	author_data1 = page_content.select(".author")
	print(author_data1)
	



