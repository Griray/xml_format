import xml.etree.ElementTree as ET
from collections import Counter

parser = ET.XMLParser(encoding= "utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()

all_words = []
pop_words = []

chanel_node = root.find("channel")
descr_list = root.findall("channel/item/description")

for descr in descr_list:
    news = descr.text
    news = news.lower()
    news = news.split()
    all_words.extend(news)

for word in all_words:
    if len(word) > 6:
        pop_words.append(word)

stat = Counter(pop_words)
sort_stat = stat.most_common(10)
print("Топ 10 слов", sort_stat)






