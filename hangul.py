import json
import re
import jpype
from konlpy.tag import Okt
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud

inputFileName = './baseResources/etnews.kr_facebook_2016-01-01_2018-08-01_4차 산업혁명'
data = json.loads(open(inputFileName + '.json', 'r', encoding= 'utf-8').read())
print(f'data : {data}')

message = ''
for item in data:
    if 'message' in item.keys():
        message = message + re.sub(r'[^\w]', ' ', item['message']) + ' '
print(f'message : {message}')

nlp = Okt()
message_N = nlp.nouns(message)
print(f'message_N : {message_N}')

count = Counter(message_N)
print(f'count : {count}')

word_count = dict()
for tag, counts in count.most_common(80):
    if(len(str(tag))>1):
        word_count[tag] = counts
        print("%s : %d " % (tag, counts))

font_path = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family = font_name)

plt.figure(figsize=(12, 5))
plt.xlabel('키워드')
plt.ylabel('빈도수')
plt.grid(True)
sorted_Keys = sorted(word_count, key = word_count.get, reverse= True)
sorted_Values = sorted(word_count.values(), reverse= True)
plt.bar(range(len(word_count)), sorted_Values, align= 'center')
plt.xticks(range(len(word_count)), list(sorted_Keys), rotation = '75')
plt.show()

wc = WordCloud(font_path, background_color= 'ivory', width= 800, height = 600)
cloud = wc.generate_from_frequencies(word_count)
plt.figure(figsize= (8, 8))
plt.imshow(cloud)
plt.axis('off')
plt.show()

cloud.to_file(inputFileName + '_cloud.jpg')