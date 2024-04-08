import requests
from bs4 import BeautifulSoup
import json


#url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'


headers = {
   'Accept': '*/*',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

#req = requests.get(url, headers=headers)
#src = req.text
#print(src)

#with open('index.html', 'w', encoding='utf-8') as file:
#    file.write(src)

# with open('index.html', encoding = 'utf-8') as file:
#     src = file.read()


# soup = BeautifulSoup(src, 'lxml')

# eat_block = soup.find_all(class_ = 'mzr-tc-group-item-href')


# all_categories_dict = {}
# for elem in eat_block:
#     elem_text = elem.text
#     elem_href = 'https://health-diet.ru' + elem.get("href")
#     print(f'{elem_text}: {elem_href}')
#     all_categories_dict[elem_text] = elem_href

# with open('all_categories_dict.json', 'w', encoding='utf-8') as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open('all_categories_dict.json', encoding = 'utf-8') as file:
    all_categories = json.load(file)

#print(all_categories)


count = 0

for category_name, category_href in all_categories.items():

    if count == 0:
        rep = [',', ' ', '-']
        for item in rep:
            if item in category_name:
                category_name = category_name.replace(item, '_')
        #print(category_name)
        
        req = requests.get(url=category_href, headers=headers)
        src = req.text



        with open(f"data/{count}_{category_name}.html", "w", encoding="utf-8") as file:
            file.write(src)

        with open(f"data/{count}_{category_name}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')

        table_head = soup.find(class_ = '')

        count += 1


