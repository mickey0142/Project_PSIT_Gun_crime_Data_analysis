"""US Guncrime data analysis"""
import pygal
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
    for i in data:# change data into list of year from input change this after main function
        number[i] = {}#set dict year
        for j in data[i]:#loop in data in dict "i" year
            number[i][j] = {}#set state dict
            for k in data[i][j]:#loop in all state
                if not k[0] in number[i][j]:#if state k if not in dict number make it
                    number[i][j][k[0]] = 1#set number of crime in k state to 1
                else:#if state k is in dict number plus 1 to count how many crime in that state
                    number[i][j][k[0]] += 1
    all_year = {}#this variable is for count number of crime each month and each year
    for i in number:#loop in number variable
        all_year[i] = {}#set dict year
        for j in number[i]:# loop in each state in "i" year
            for k in number[i][j]:#loop in each month in "j" state
                if not k in all_year[i]:# if sum of numberofcrime in "k" month in "i" year is not in variable make it
                    all_year[i][k] = number[i][j][k]
                else:# if sum is in dict plus it
                    all_year[i][k] += number[i][j][k]
    all_year['sum_year'] = 0# create key and values to keep sum of each year
    for i in all_year:# loop in sum of numberofcrime
        if i.isdigit():#check condition to fix some bug
            all_year[i]['one_year'] = 0# create key and values to keep sum of one year
            for j in all_year[i]:# loop in each month in "i" year
                if j.isdigit():# check condition to fix some bug
                    all_year['sum_year'] += all_year[i][j]# add numberofcrime in sum of all year
                    all_year[i]['one_year'] += all_year[i][j]# add numberofcrime in "i" year
    # return number, all_year
    return sort_all(all_year)
    #number -> data contain how many crime happen each state and each month
    #all_year -> data contain how many crime happen each month each year and all

def sort_all(var):
    """sort data all_year and save into variable to send to another function"""
    cut_data = []
    temp3 = sorted(list(var.keys()))
    for i in temp3:
        if i.isdigit():
            if i == '2016':
                temp2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            else:
                temp2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
            temp = [var[i][j] for j in temp2 if j.isdigit()]
            cut_data.append(temp)
    return cut_data# this variable contain data from 2013 to 2016 and sort month data from jan to dec
    #maybe def two function sort in one year(12month) and sort in >1 year and graph too

def graph():
    """use data to plot graph with pygal module here"""
    all_year = numberofcrime()
    line_chart = pygal.Line()
    line_chart.title = 'guncrime'
    line_chart.x_labels = map(str, range(1, 13))# change x label here
    count = 0
    y_data = ['2013', '2014', '2015', '2016']
    for i in all_year:
        line_chart.add(y_data[count], all_year[count])
        count += 1
    line_chart.render_to_file('test.svg')

def main():
    """get input to choose what year to show here"""
    choose = input()

graph()