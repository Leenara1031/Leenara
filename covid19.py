import pandas as pd
import numpy as np
import webbrowser
import openpyxl
import folium
import os

from matplotlib import pyplot as plt
from matplotlib import rcParams, style
from matplotlib import font_manager, rc

co19Clinic = pd.read_csv('../resources/covid19.csv',
                         encoding = 'CP949',
                         index_col = 0,
                         header = 0,
                         engine = 'python')
print(f'covid19Clinic : {co19Clinic}')

co19Clinic_geoData = pd.read_csv('../resources/covid19.csv',
                                    encoding = 'CP949',
                                    engine = 'python')

def saveTempCSV(df, loc='../resources/covid19Clinic.csv', m='w', e='cp949'):
    df.to_csv(loc, mode=m, encoding=e)

map_co19Clinic = folium.Map(location= [37.51632268, 127.0421105], zoom_start = 15)
map_co19Clinic.save('../resources/map_covid19Clinic.html')

for i, covid19 in co19Clinic_geoData.iterrows():
    folium.Marker(location = [covid19['위도'], covid19['경도']],
                  popup = covid19['의료기관명'],
                  icon = folium.Icon(color = 'blue', icon = 'star')).add_to(map_co19Clinic)

map_co19Clinic.save('../resources/map_covid19Clinic.html')
webbrowser.open('C:/lnr_scraping/analysis/resources/map_covid19Clinic.html')

addr = pd.DataFrame(co19Clinic['주소'].apply(lambda v: v.split()[:2]).tolist(), columns = ('시도', '군구'))
print(addr['시도'].unique())

addr_aliases = {'서울':'서울특별시', '서울시':'서울특별시', '부산':'부산광역시', '부산시':'부산광역시', '대구':'대구광역시',
                '인천':'인천광역시', '광주':'광주광역시', '대전':'대전광역시', '울산':'울산광역시', '경기':'경기도',
                '강원':'강원도', '충북':'충청북도', '충남':'충청남도', '전북':'전라북도', '전남':'전라남도',
                '경북':'경상북도', '경남':'경상남도', '제주':'제주특별자치도'}
addr['시도'] = addr['시도'].apply(lambda v : addr_aliases.get(v, v))
print(addr['시도'].unique())

print(addr['군구'].unique())

addr['시도군구'] = addr.apply(lambda r : r['시도'] + ' ' + r['군구'], axis = 1)
print(f'addr: {addr}')

addr['count'] = 0
print(f'addr: {addr}')

addr_group = pd.DataFrame(addr.groupby(['시도', '군구', '시도군구'], as_index = False).count())
pd.DataFrame(addr_group)
addr_group = addr_group.set_index('시도군구')
print(f'addr_group : {addr_group}')


population = pd.read_excel('../resources/행정구역_시군구_별_성별_인구수2.xlsx')
print(f'population : {population}')

population = population.rename(columns = {'행정구역(시군구)별(1)' : '시도',
                                          '행정구역(시군구)별(2)' : '군구'})
print(f'population : {population}')

# for element in range(0, len(population)):
#     population['군구'][element] = population['군구'][element].strip()

for element in range(len(population)):
    population.at[element, '군구'] = population.at[element, '군구'].strip()

population['시도군구'] = population.apply(lambda r : r['시도'] + ' ' + r['군구'], axis = 1)
population = population[population['군구'] != '소계']
population = population.set_index("시도군구")
print(f'population : {population}')

addr_population_merge = pd.merge(addr_group, population,
                                 how = 'inner',
                                 left_index = True,
                                 right_index = True)
print(f'addr_population_merge : {addr_population_merge}')

local_MC_Population = addr_population_merge[['시도_x',
                                             '군구_x',
                                             'count',
                                             '총인구수 (명)']]
print(f'local_MC_Population : {local_MC_Population}')

local_MC_Population = local_MC_Population.rename(columns = {'시도_x':'시도',
                                                            '군구_x':'군구',
                                                            '총인구수 (명)':'인구수'})

MC_count = local_MC_Population['count']
local_MC_Population['MC_ratio'] = MC_count.div(local_MC_Population['인구수'], axis = 0) * 100000
print(f'local_MC_Population : {local_MC_Population}')


style.use('ggplot')
font_name = font_manager.FontProperties(fname= "c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)

MC_count = local_MC_Population[['count']]
MC_count = MC_count.sort_values('count', ascending=False)
plt.rcParams['figure.figsize'] = (25, 5)
MC_count.plot(kind = 'bar', rot = 90)
plt.show()

MC_ratio = local_MC_Population[['MC_ratio']]
MC_ratio = MC_ratio.sort_values('MC_ratio', ascending=False)
plt.rcParams['figure.figsize'] = (25, 5)
MC_ratio.plot(kind = 'bar', rot = 90)
plt.show()

path = os.getcwd()
print(f'path++++: {path}')
data_draw_korea = pd.read_csv(path + '/data_draw_korea.csv',
                              index_col = 0,
                              encoding = 'UTF-8',
                              engine = 'python')

data_draw_korea['시도군구'] = data_draw_korea.apply(lambda r: r['광역시도'] + ' ' + r['행정구역'], axis= 1)
data_draw_korea = data_draw_korea.set_index('시도군구')

data_draw_korea_MC_Population_all = pd.merge(data_draw_korea, local_MC_Population,
                                             how='outer',
                                             left_index= True,
                                             right_index= True)
print(f'data_draw_korea_MC_Population_all : {data_draw_korea_MC_Population_all}')

print(f'empty\n{data_draw_korea_MC_Population_all[data_draw_korea_MC_Population_all["shortName"].isnull()]}')

BORDER_LINES = [
    [(3, 2), (5, 2), (5, 3), (9, 3), (9, 1)], # 인천,
    [(2, 5), (3, 5), (3, 4), (8, 4), (8, 7), (7, 7), (7, 9), (4, 9), (4, 7), (1, 7)], # 서울,
    [(1, 6), (1, 9), (3, 9), (3, 10), (8, 10), (8, 9), (9, 9), (9, 8), (10, 8), (10, 5), (9, 5), (9, 3)], # 경기도,
    [(9, 12), (9, 10), (8, 10)], # 강원도,
    [(10, 5), (11, 5), (11, 4), (12, 4), (12, 5), (13, 5), (13, 4), (14, 4), (14, 2)], # 충청남도,
    [(11, 5), (12, 5), (12, 6), (15, 6), (15, 7), (13, 7), (13, 8), (11, 8), (11, 9), (10, 9), (10, 8)], # 충청북도,
    [(14, 4), (15, 4), (15, 6)], # 대전시,
    [(14, 7), (14, 9), (13, 9), (13, 11), (13, 13)], # 경상북도,
    [(14, 8), (16, 8), (16, 10), (15, 10), (15, 11), (14, 11), (14, 12), (13, 12)], # 대구시,
    [(15, 11), (16, 11), (16, 13)], # 울산시,
    [(17, 1), (17, 3), (18, 3), (18, 6), (15, 6)], # 전라북도,
    [(19, 2), (19, 4), (21, 4), (21, 3), (22, 3), (22, 2), (19, 2)], # 광주시,
    [(18, 5), (20, 5), (20, 6)], # 전라남도,
    [(16, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9), (20, 10)], # 부산시,
    ]

def draw_bolckMap(blockMap, targetData, title, color):
    whitelabelmin = (max(blockMap[targetData]) - min(blockMap[targetData])) * 0.25 + min(blockMap[targetData])
    datalabel = targetData
    vmin = min(blockMap[targetData])
    vmax = max(blockMap[targetData])

    # print(f'whitelabelmin: {whitelabelmin}')
    # print(f'datalabel: {datalabel}')
    # print(f'vmin: {vmin}')
    # print(f'vmax: {vmax}')

    mapData = blockMap.pivot(index = 'y', columns= 'x', values = targetData)
    print(f'mapData: {mapData}')
    masked_mapData = np.ma.masked_where(np.isnan(mapData), mapData)
    print(f'masked_mapData: {masked_mapData}')

    plt.figure(figsize=(8, 13))
    plt.title(title)
    plt.pcolor(masked_mapData,
               vmin = vmin,
               vmax = vmax,
               cmap = color,
               edgecolor = '#aaaaaa',
               linewidth = 0.5)

    for idx, row in blockMap.iterrows():
        annocolor = 'white' if row[targetData] > whitelabelmin else 'black'

        if row['광역시도'].endswith('시') and not row['광역시도'].startswith('세종'):
            dispname = f'{row["광역시도"][:2]}\n{row["행정구역"][:-1]}'
            if len(row['행정구역']) <= 2:
                dispname += row['행정구역'][-1]

        else:
            dispname = row['행정구역'][:-1]

        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 9.5, 1.5
        else:
            fontsize, linespacing = 11, 1.2

        plt.annotate(dispname, (row['x'] + 0.5, row['y'] + 0.5),
                     weight = 'bold',
                     fontsize = fontsize,
                     ha = 'center',
                     va = 'center',
                     color = annocolor,
                     linespacing = linespacing)

    for path in BORDER_LINES:
        ys, xs = zip(*path)
        # print(f'ys ---> {ys}')
        # print(f'xs ---> {xs}')
        plt.plot(xs, ys, color='black', lw=1)

    plt.gca().invert_yaxis()
    plt.axis('off')

    cb = plt.colorbar(shrink = 1, aspect = 10)
    cb.set_label(datalabel)

    plt.tight_layout()
    plt.savefig('../resources/blockMap_' + targetData + '.png')

    plt.show()

draw_bolckMap(data_draw_korea_MC_Population_all,
              'count',
              '행정구역별 선별진료소 수',
              'Blues')

draw_bolckMap(data_draw_korea_MC_Population_all,
              'MC_ratio',
              '행정구역별 선별진료소 비율',
              'Reds')
