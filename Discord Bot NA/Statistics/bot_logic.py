import pandas

data1 = pandas.read_csv(r"Statistics\bestna.csv", header=0)
data = pandas.read_csv(r"Statistics\iosna ratings.csv", header=0)


class highest:
    def highestnames():
        name = list(data.Name)
        rate = list(data.Rating)

        x = [[name[i]] for i in range(len(rate))]

        blah = [newlst for sublist in x for newlst in [sublist]]

        highest_names =[item[0] for item in blah]

        lol = list(map(' '.join, zip(["1.","2.","3.","4.","5.","6.","7.","8.","9.","10."], highest_names)))
        return lol

    def highestpos():
        pos = list(data.Position)
        rate = list(data.Rating)

        x = [[pos[i]] for i in range(len(rate))]

        blah = [newlst for sublist in x for newlst in [sublist]]

        highest_pos = [item[0] for item in blah]

        return highest_pos

    def highestratings():
        rate = list(data1.Rating)

        x = [[rate[i]] for i in range(len(rate))]

        blah = [newlst for sublist in x for newlst in [sublist]]

        highest_ratings =[item[0] for item in blah]

        return highest_ratings
