import pandas

data = pandas.read_csv(r"iosna ratings.csv", header=0)
data1 = pandas.read_csv(r"bestna.csv", header=0)


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
        rate = list(data.Rating)

        x = [[rate[i]] for i in range(len(rate))]

        blah = [newlst for sublist in x for newlst in [sublist]]

        highest_ratings =[item[0] for item in blah]

        return highest_ratings

class topna:
    def highestnames2():
        name = list(data1.Name)
        rate = list(data1.Rating)

        x = [[name[i]] for i in range(len(rate))]

        blah = [newlst for sublist in x for newlst in [sublist]]

        highest_names =[item[0] for item in blah]

        lol = list(map(' '.join, zip(["1.","2.","3.","4.","5.","6.","7.","8.","9.","10."], highest_names)))
        return lol

    def highestpos2():
        pos = list(data1.Position)
        rate = list(data1.Rating)

        x = [[pos[i]] for i in range(len(rate))]

        blah = [newlst for sublist in x for newlst in [sublist]]

        highest_pos = [item[0] for item in blah]

        return highest_pos

    def highestratings2():
        rate = list(data1.Rating)

        x = [[rate[i]] for i in range(len(rate))]

        blah = [newlst for sublist in x for newlst in [sublist]]

        highest_ratings =[item[0] for item in blah]

        return highest_ratings
