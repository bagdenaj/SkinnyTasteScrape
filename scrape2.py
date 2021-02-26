import requests, csv, time
from bs4 import BeautifulSoup
import pandas as pd

for num in range(1):  # Pages number plus 1
    url = f'https://www.skinnytaste.com/page/{num}/'
    res = requests.get(url)
    time.sleep(res.elapsed.total_seconds())
    soup = BeautifulSoup(res.text, 'lxml')


    myfile = open('project.csv', 'w', encoding='utf-8')
    writer = csv.writer(myfile)
    writer.writerow(['Title', 'Image', 'Summary', 'Blue Point', 'Green Point', 'Purple Point', 'Calories', 'Recipe-Key'])


    # Grab everything in the post
    articles = soup.find_all('article', class_='post teaser-post odd')
    articles2 = soup.find_all('article', class_='post teaser-post even')
    mega_articles = articles + articles2


    for post in mega_articles:
        try:
            title = post.h2.text
            summary = post.p.text
            image = post.img['src']

            # Points & calories
            blue = post.find('div', class_='recipe-meta').find('span', class_='smart-points blue').text
            green = post.find('div', class_='recipe-meta').find('span', class_='smart-points green').text
            purple = post.find('div', class_='recipe-meta').find('span', class_='smart-points purple').text
            calories = post.find('div', class_='recipe-meta').find('span', class_='icon-star').text

            # Recipe-Keys
            keys = post.find('div', class_='icons')
            recipe_keys = []
            for tag in keys:
                img = tag.find('img')
                if img:
                    name = img['alt']
                    recipe_keys.append(name)
        except:
            pass

        writer.writerow([title, image, summary, blue, green, purple, calories, recipe_keys])

    myfile.close()

df = pd.read_csv('project.csv')
print(df)
