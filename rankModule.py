class RankDeviation:

    def __init__(self, mss, ess):
        self.midStuScores = mss
        self.endStuScoros = ess
        self.midRanks = [0 for i in range(len(mss))]
        self.endRanks = [0 for i in range(len(ess))]
        self.rankDeviaion = [0 for i in range(len(mss))]

    def setRank(self, ss, rs):
        for idx, sco1 in enumerate(ss):
            for sco2 in ss:
                if sco1 < sco2:
                    rs[idx] += 1

    def setMidRank(self):
        self.setRank(self.midStuScores, self.midRanks)

    def getMidRank(self):
        return self.midRanks

    def setEndRank(self):
        self.setRank(self.endStuScoros, self.endRanks)

    def getEndRank(self):
        return self.endRanks

    def printRankDeviation(self):
        for idx, mRank in enumerate(self.midRanks):
            deviation = mRank - self.endRanks[idx]

            if deviation > 0:
                #순위 다운
                deviation = '↑' + str(abs(deviation))
            elif deviation < 0:
                #순위 업
                deviation = '↓' + str(abs(deviation))
            else:
                #순위 변동 없음
                deviation = '=' + str(abs(deviation))

            print(f'mid_rank: {mRank} \t end_rank: {self.endRanks[idx]} \t deviation: {deviation}')
