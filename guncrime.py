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
        print(i)
        if not i[2] in crime[i[1]]:
            crime[i[1]][i[2]] = []
            crime[i[1]][i[2]].append([i[0], i[3], i[4]])
        else:
            crime[i[1]][i[2]].append([i[0], i[3], i[4]])
    return crime
# data is in {'year':{'state':[month, kill, injured]}}

print(collect_data())
