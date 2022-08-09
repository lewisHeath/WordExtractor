import requests 
import click
import re
from bs4 import BeautifulSoup

page_links = []

def get_html_of(url):
	resp = requests.get(url)

	if resp.status_code != 200:
		print(f'HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting...')
		exit(1)
	
	return resp.content.decode()

def count_occurences_in(word_list, min_length):
	word_count = {}
	for word in word_list:
		if len(word) < min_length:
			continue
		if word not in word_count:
			word_count[word] = 1
		else:
			current_count = word_count.get(word)
			word_count[word] = current_count + 1
	return word_count

def get_all_words_from(url, get_links=False):
	html = get_html_of(url)
	soup = BeautifulSoup(html, 'html.parser')
	raw_text = soup.get_text()
	links = []
	if get_links:
		# save all links 
		for link in soup.find_all('a'):
			# check if the link is a http link
			if link.get('href') != None:
				if link.get('href')[:5] == 'https':
					links.append(link.get('href'))
					# print(link.get('href'))
				elif link.get('href')[:4] == 'http':
					links.append(link.get('href'))
					# print(link.get('href'))
	return re.findall(r'\w+', raw_text), links

def get_top_words_from(all_words, min_length):
	occurences = count_occurences_in(all_words, min_length)
	return sorted(occurences.items(), key=lambda item: item[1], reverse=True)

def print_top_words_from(words, amount=10):
	for i in range(amount):
		# if there are no more words, break
		if i >= len(words):
			break
		print(f'- {i+1}: {words[i][0]}')

@click.command()
@click.option('--url', '-u', prompt='Web URL', help='URL of the webpage to extract from.')
@click.option('--length', '-l', default=0, help='Minimum word length (default: 0, no limit).')
@click.option('--amount', '-a', default=10, help='Amount of top words to print (default: 10).')
@click.option('--link-depth', '-ld', default=1, help='The depth of how many links to trace. (default: 1)')
def main(url, length, amount, link_depth):
	the_words, links = get_all_words_from(url, True)
	top_words = get_top_words_from(the_words, length)

	print_top_words_from(top_words, amount)

	for i in range(link_depth):
		temp_links = []
		for link in links:
			the_words_from_links, more_links = get_all_words_from(link, True)
			temp_links = more_links
			top_words = get_top_words_from(the_words_from_links, length)
			print(f'New Page: {link}')
			print_top_words_from(top_words, amount)
		links = temp_links

if __name__ == "__main__":
	main()

