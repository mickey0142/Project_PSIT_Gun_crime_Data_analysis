"""US Guncrime data analysis"""
def collect_data():
    """get data from file .txt into variable 'crime'"""
    file = open('alldata.txt')
    crime = {'2013':{}, '2014':{}, '2015':{}, '2016':{}}
    for i in file:
        i = i.split()
        if len(i) > 5:
            i[2] = i[2] + i[3]
            i.remove(i[3])
        if len(i) > 5:
            i[2] = i[2] + i[3]
            i.remove(i[3])
        if not i[2] in crime[i[1]]:
            crime[i[1]][i[2]] = []
            crime[i[1]][i[2]].append([i[0], i[3], i[4]])
        else:
            crime[i[1]][i[2]].append([i[0], i[3], i[4]])
    return crime
# data is in {'year':{'state':[month, kill, injured]}}

def numberofcrime():
    """get data that what state have the highest number of crime and that number"""
    data = collect_data()
    number = {}
    for i in data:
        for j in data[i]:
            for k in data[i][j]:
                print(k)
                if not k[0] in number:
                    number[k[0]] = 1
                else:
                    number[k[0]] += 1
    number["all_year"] = 0
    for i in number:
        if i.isdigit():
            number["all_year"] += number[i]

numberofcrime()