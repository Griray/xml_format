import xml.etree.ElementTree as ET
from collections import Counter

parser = ET.XMLParser(encoding= "utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()

all_words = []
pop_words = []

chanel_node = root.find("channel")
items_list = root.findall("channel/item/title")

for title in items_list:
    news = title.text.split()
    all_words.extend(news)
    for word in all_words:
        if len(word) > 6:
            pop_words.append(word)

stat = Counter(pop_words)
sort_stat = sorted(((say, number) for say, number in stat.items()), key=lambda pair: pair[1], reverse=True)
print("Топ 10 слов в новостной ленте: ")
for i in range (10):
    print(sort_stat[i])




