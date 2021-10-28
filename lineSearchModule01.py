class SearchData:

    def __init__(self, ds, d):
        self.datas = ds
        self.data = d
        self.searchResultIdx = -1

    def getIndexOfData(self):
        n = 0
        while True:

            if n == len(self.datas):
                self.searchResultIdx = -1
                break

            elif self.datas[n] == self.data:
                self.searchResultIdx = n
                break

            n += 1