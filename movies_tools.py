import csv

row_lst = []
with open("movies_clean.csv","r") as csvdata:
    reader = csv.reader(csvdata)
    for row in reader:
        row_lst.append(row)

class Movie:
    def __init__(self,row):
        self.row = row

    def get_name_rating(self):
        return "The IMDB Rating of {} is {}<br>".format(self.row[0],self.row[-2])

class MovieFilter:
    filter_lst = []
    n = 0
    result_str = ""
    def __init__(self,csv_lst,score):
        self.lst = csv_lst
        self.score = score

    def filter(self):
        for item in self.lst[1:]:
            if item[-2] != "NA":
                if float(item[-2]) > float(self.score):
                    self.n += 1
                    self.filter_lst.append(item)


        for i in range(self.n):
            self.result_str += "{} | {}<br>".format(self.filter_lst[i][0],self.filter_lst[i][-2])
        return self.result_str

if __name__ == '__main__':
    test = MovieFilter(row_lst,8)
    test.filter()
