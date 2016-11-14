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
    data = collect_data()# move collect_data() into main function and call it from there then just put that variable into this function
    number = {}
    for i in data:# change data into list of year that you want to use
        number[i] = {}
        for j in data[i]:
            number[i][j] = {}
            for k in data[i][j]:
                if not k[0] in number[i][j]:
                    number[i][j][k[0]] = 1
                else:
                    number[i][j][k[0]] += 1
    all_year = {}
    for i in number:
        all_year[i] = {}
        for j in number[i]:
            for k in number[i][j]:
                if not k in all_year[i]:
                    all_year[i][k] = number[i][j][k]
                else:
                    all_year[i][k] += number[i][j][k]
    all_year['sum_year'] = 0
    for i in all_year:
        if i.isdigit():
            all_year[i]['one_year'] = 0
            for j in all_year[i]:
                if j.isdigit():
                    all_year['sum_year'] += all_year[i][j]
                    all_year[i]['one_year'] += all_year[i][j]
    return number# half raw data contain how many crime happen each state and each month
    return all_year# data contain how many crime happen each month each year and all

numberofcrime()
