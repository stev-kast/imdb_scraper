import requests 
import lxml.html as html
# import os
import datetime


LINK_TO_RESUME =  '//div/h3/a/@href'
NAMES = '//div/h3/a/text()'


def extract():
	MAIN_URL = 'https://www.imdb.com/search/name/?birth_monthday=date&ref_=rlm'
	try:
		today = datetime.date.today().strftime('%m-%d')
		MAIN_URL = MAIN_URL.replace('date',today)
		response = requests.get(MAIN_URL)
		if response.status_code == 200:
			birthdays = response.content.decode('utf-8')
			parsed = html.fromstring(birthdays)
			links_to_news = parsed.xpath(LINK_TO_RESUME)
			names = parsed.xpath(NAMES)
			#print(links_to_news)
			today = datetime.date.today().strftime('%d-%m-%Y')
			# if not os.path.isdir(today):
			# 	os.mkdir(today)


			i = 0
			with open(f'{today}.txt','w', encoding='utf-8') as f:
				for link in links_to_news:
					link = 'https://www.imdb.com' + link + '/bio?ref_=nm_ov_bio_sm'				
					f.write(names[i])
					f.write(' ')
					f.write(link)
					f.write('\n')
					# print(link)
					# print(names[i])
					i = i + 1
		else:
			raise ValueError(f'Error: {response.status_code}')
	except ValueError as ve:
		print(ve)


def run():
	extract()



if __name__ == '__main__':
    run()