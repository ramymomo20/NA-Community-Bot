import pandas

data = pandas.read_csv(r"iosna ratings.csv", header=0)
data1 = pandas.read_csv(r"bestna.csv", header=0)

class highest:
    def __init__(self, file):
        self.file = file

    def highestnames(self):
        name = list(self.file.Name)
        rate = list(self.file.Rating)

        x = [[name[i]] for i in range(len(rate))]

        blah = [newlst for sublist in x for newlst in [sublist]]

        highest_names =[item[0] for item in blah]

        lol = list(map(' '.join, zip(["1.","2.","3.","4.","5.","6.","7.","8.","9.","10."], highest_names)))
        return lol

    def highestpos(self):
        pos = list(self.file.Position)
        rate = list(self.file.Rating)

        x = [[pos[i]] for i in range(len(rate))]

        blah = [newlst for sublist in x for newlst in [sublist]]

        highest_pos = [item[0] for item in blah]

        return highest_pos

    def highestratings(self):
        rate = list(self.file.Rating)

        x = [[rate[i]] for i in range(len(rate))]

        blah = [newlst for sublist in x for newlst in [sublist]]

        highest_ratings =[item[0] for item in blah]

        return highest_ratings