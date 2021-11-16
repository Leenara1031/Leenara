import random

# scores = random.sample(range(50, 100), 20)
# print(f'scores: {scores}')

#속도 느림
# ranks = []
# for i in range(len(scores)):
#     ranks.append(0)

#속도 빠름
# ranks = [0 for i in range(len(scores))]
# #print(f'ranks: {ranks}')
#
# for idx, sco1 in enumerate(scores):
#     for sco2 in scores:
#         if sco1 < sco2:
#             ranks[idx] += 1
#
# print(f'ranks: {ranks}')
#
# for i, s in enumerate(scores):
#     print(f'{s}: {ranks[i] +1}')

#01 학급 학생(20명)의 중간고사와 기말고사 성적을 이용해서 각각의 순위를 구하고
#02 중간고사 대비 기말고사 순위 변화(편차)를 출력하는 프로그램을 만들어보자!

#score : 50~100

#1: mid_scor : 10     end_scor : 5      deviaion : ↑5
#2: mid_scor : 8     end_scor : 20      deviaion : ↓12

import rankModule as rm
import random

midStuScroes = random.sample(range(50, 100), 20)
endStuScroes = random.sample(range(50, 100), 20)
print(f'midStuScroes : {midStuScroes}')
print(f'endStuScroes : {endStuScroes}')

rd = rm.RankDeviation(midStuScroes, endStuScroes)
rd.setMidRank()
print(f'mid_rank: {rd.getMidRank()}')

rd.setEndRank()
print(f'end_rank: {rd.getEndRank()}')

rd.printRankDeviation()