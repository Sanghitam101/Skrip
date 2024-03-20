import json
import requests
from bs4 import BeautifulSoup
import csv


def get_html_links(url, head):
	r = requests.get(url, headers=head).text
	return r


def get_links(html):
	dic_categories = {}
	soup = BeautifulSoup(html, "lxml")
	divs = soup.find_all(class_="uk-flex mzr-tc-group-item")
	for div in divs:
		url = 'https://health-diet.ru' + div.find('a').get('href')
		item_text = div.find('a', class_="mzr-tc-group-item-href").text
		dic_categories[item_text] = url

	return dic_categories


def get_html_for_items(url, head):
	r = requests.get(url, headers=head).text
	return r


def try_get(url, head):
	r = requests.get(url, headers=head).status_code
	return r


def get_values(html, part):
	part = part
	soup = BeautifulSoup(html, 'lxml')
	Title = soup.find('div', class_="uk-overflow-container").find('thead').find_all('th')

	product = Title[0].text
	weight = 'вес'
	calories = Title[1].text
	proteins = Title[2].text
	fats = Title[3].text
	carbohydrates = Title[4].text

	with open(f'data.csv', 'a', encoding='utf-8') as file:
		writer = csv.writer(file)
		writer.writerow((
			product,
			weight,
			calories,
			proteins,
			fats,
			carbohydrates
		))

	divs = soup.find('div', class_="uk-overflow-container").find_all('tr')

	product_info = []
	for div in divs[1:]:
		product = div.find('a').text
		weight = '100'
		calories = div.find_all('td')[1].text.split(' ')[0].replace(',', '.')
		proteins = div.find_all('td')[2].text.split(' ')[0].replace(',', '.')
		fats = div.find_all('td')[3].text.split(' ')[0].replace(',', '.')
		carbohydrates = div.find_all('td')[4].text.split(' ')[0].replace(',', '.')

		product_info.append(
			{
				'Title': product,
				'Weight': weight,
				'Calories': calories,
				'Proteins': proteins,
				'Fats': fats,
				"Carbohydrates": carbohydrates
			}
		)

		with open(f'data.csv', 'a', encoding='utf-8') as file:
			writer = csv.writer(file)
			writer.writerow((
				product,
				weight,
				calories,
				proteins,
				fats,
				carbohydrates
			))
	with open(f'Data_{part}.json', 'a', encoding='utf-8') as file:
		json.dump(product_info, file, indent=4, ensure_ascii=False)


def main():
	head = {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
	}
	url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
	url2 = 'https://health-diet.ru/base_of_food/food_24507/'
	# get_values(get_html_for_items(url2, head), 1)
	part = 0
	for dic in get_links(get_html_links(url, head)).items():
		if try_get(dic[1], head) == 200:
			get_values(get_html_for_items(dic[1], head), part)
			print(part)
			part += 1
		else:
			continue


if __name__ == "__main__":
	main()import json
import requests
from bs4 import BeautifulSoup
import csv


def get_html_links(url, head):
	r = requests.get(url, headers=head).text
	return r


def get_links(html):
	dic_categories = {}
	soup = BeautifulSoup(html, "lxml")
	divs = soup.find_all(class_="uk-flex mzr-tc-group-item")
	for div in divs:
		url = 'https://health-diet.ru' + div.find('a').get('href')
		item_text = div.find('a', class_="mzr-tc-group-item-href").text
		dic_categories[item_text] = url

	return dic_categories


def get_html_for_items(url, head):
	r = requests.get(url, headers=head).text
	return r


def try_get(url, head):
	r = requests.get(url, headers=head).status_code
	return r


def get_values(html, part):
	part = part
	soup = BeautifulSoup(html, 'lxml')
	Title = soup.find('div', class_="uk-overflow-container").find('thead').find_all('th')

	product = Title[0].text
	weight = 'вес'
	calories = Title[1].text
	proteins = Title[2].text
	fats = Title[3].text
	carbohydrates = Title[4].text

	with open(f'data.csv', 'a', encoding='utf-8') as file:
		writer = csv.writer(file)
		writer.writerow((
			product,
			weight,
			calories,
			proteins,
			fats,
			carbohydrates
		))

	divs = soup.find('div', class_="uk-overflow-container").find_all('tr')

	product_info = []
	for div in divs[1:]:
		product = div.find('a').text
		weight = '100'
		calories = div.find_all('td')[1].text.split(' ')[0].replace(',', '.')
		proteins = div.find_all('td')[2].text.split(' ')[0].replace(',', '.')
		fats = div.find_all('td')[3].text.split(' ')[0].replace(',', '.')
		carbohydrates = div.find_all('td')[4].text.split(' ')[0].replace(',', '.')

		product_info.append(
			{
				'Title': product,
				'Weight': weight,
				'Calories': calories,
				'Proteins': proteins,
				'Fats': fats,
				"Carbohydrates": carbohydrates
			}
		)

		with open(f'data.csv', 'a', encoding='utf-8') as file:
			writer = csv.writer(file)
			writer.writerow((
				product,
				weight,
				calories,
				proteins,
				fats,
				carbohydrates
			))
	with open(f'Data_{part}.json', 'a', encoding='utf-8') as file:
		json.dump(product_info, file, indent=4, ensure_ascii=False)


def main():
	head = {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
	}
	url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
	url2 = 'https://health-diet.ru/base_of_food/food_24507/'
	# get_values(get_html_for_items(url2, head), 1)
	part = 0
	for dic in get_links(get_html_links(url, head)).items():
		if try_get(dic[1], head) == 200:
			get_values(get_html_for_items(dic[1], head), part)
			print(part)
			part += 1
		else:
			continue


if __name__ == "__main__":
	main()

