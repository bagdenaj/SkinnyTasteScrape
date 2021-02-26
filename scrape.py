import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_rescourse():
	links = []
	content = []
	for i in range(1,3):
		res =requests.get(f'https://www.skinnytaste.com/page/{i}')
		soup = BeautifulSoup(res.text, 'lxml')

		content.extend(soup.select('.post'))
	return content

def create_custom_st():
	content = get_rescourse()
	st = []
	for item in content:
		if len(item.select('.icon-star')) != 0:
			calories = item.select('.icon-star')[0].getText()
			title = item.h2.getText()
			points_blue = item.select('.icon-sp')[0].getText().split()[0] if len(item.select('.icon-sp')) != 0 else None
			points_green = item.select('.icon-sp')[0].getText().split()[1] if len(item.select('.icon-sp')) != 0 else None
			points_purple = item.select('.icon-sp')[0].getText().split()[2] if len(item.select('.icon-sp')) != 0 else None
			summary = item.p.getText()
			st.append({'title': title, 'points_blue': points_blue, 'points_green': points_green, 'points_purple': points_purple, 'calories': calories, 'summary': summary})
	return st

df = pd.DataFrame(columns=create_custom_st()[0].keys())
for entry in create_custom_st():
	df = df.append(entry, ignore_index=True)
#print(create_custom_st()[0].keys())
print(df)
#print(get_rescourse()[1].find('div', class_='recipe-meta').find('span', class_='icon-star').text)