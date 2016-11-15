"""US Guncrime data analysis"""
import pygal
def collect_data():
    """get data from file .txt into variable 'crime'"""
    file = open('alldata.txt')
    crime = {'2014':{}, '2015':{}, '2016':{}}
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
# data is in {'year':{'state':[[month, kill, injured]]}}

def numberofcrime(cal, choose, data):
    """collect data about how many incident happen and save it to variable"""
    number = {}
    for i in cal:# loop in list of input
        number[i] = {}# set dict year
        for j in data[i]:# loop in data in dict "i" year
            number[i][j] = {}# set state dict
            for k in data[i][j]:# loop in all state
                if not k[0] in number[i][j]:# if state k if not in dict number make it
                    number[i][j][k[0]] = 1# set number of crime in k state to 1
                else:# if state k is in dict number plus 1 to count how many crime in that state
                    number[i][j][k[0]] += 1
    all_year = {}# this variable is for count number of crime each month and each year
    for i in number:# loop in number variable
        all_year[i] = {}# set dict year
        for j in number[i]:# loop in each state in "i" year
            for k in number[i][j]:# loop in each month in "j" state
                if not k in all_year[i]:# if sum of numberofcrime in "k" month in "i" year is not in variable make it
                    all_year[i][k] = number[i][j][k]
                else:# if sum is in dict plus it
                    all_year[i][k] += number[i][j][k]
    all_year['sum_year'] = 0# create key and values to keep sum of each year
    for i in all_year:# loop in sum of numberofcrime
        if i.isdigit():# check condition to fix some bug
            all_year[i]['one_year'] = 0# create key and values to keep sum of one year
            for j in all_year[i]:# loop in each month in "i" year
                if j.isdigit():# check condition to fix some bug
                    all_year['sum_year'] += all_year[i][j]# add numberofcrime in sum of all year
                    all_year[i]['one_year'] += all_year[i][j]# add numberofcrime in "i" year
    if len(cal) > 1:
        if choose == "all":
            return sort_all(all_year)
        elif choose == "sum":
            return sort_sum(all_year)
    else:
        return sort_state(number)
    #number -> data contain how many crime happen each state and each month
    #all_year -> data contain how many crime happen each month each year and all

def numberofdead():
    """collect data about dead in incident and save it to variable"""
    number = {}
    for i in cal:# loop in list of input
        number[i] = {}# set dict year
        for j in data[i]:# loop in data in dict "i" year
            number[i][j] = {}# set state dict
            for k in data[i][j]:# loop in all state
                if not k[0] in number[i][j]:#if state k if not in dict number make it
                    number[i][j][k[0]] = int(k[1])# set number of dead to k state
                else:# if state k is in dict number count how many dead in that state
                    number[i][j][k[0]] += int(k[1])
    all_year = {}# this variable is for count number of dead each month and each year
    for i in number:# loop in number variable
        all_year[i] = {}# set dict year
        for j in number[i]:# loop in each state in "i" year
            for k in number[i][j]:# loop in each month in "j" state
                if not k in all_year[i]:# if sum of numberofdead in "k" month in "i" year is not in variable make it
                    all_year[i][k] = number[i][j][k]
                else:# if sum is in dict plus it
                    all_year[i][k] += number[i][j][k]
    all_year['sum_year'] = 0# create key and values to keep sum of each year
    for i in all_year:# loop in sum of numberofdead
        if i.isdigit():# check condition to fix some bug
            all_year[i]['one_year'] = 0# create key and values to keep sum of one year
            for j in all_year[i]:# loop in each month in "i" year
                if j.isdigit():# check condition to fix some bug
                    all_year['sum_year'] += all_year[i][j]# add numberofdead in sum of all year
                    all_year[i]['one_year'] += all_year[i][j]# add numberofdead in "i" year
    return number, all_year
    #number -> data contain how many dead happen each state and each month
    #all_year -> data contain how many dead happen each month each year and all

def numberofinjured():
    """collect data about injured in incident and save it to variable"""
    number = {}
    for i in cal:# loop in input
        number[i] = {}# set dict year
        for j in data[i]:# loop in data in dict "i" year
            number[i][j] = {}# set state dict
            for k in data[i][j]:# loop in all state
                if not k[0] in number[i][j]:# if state k if not in dict number make it
                    number[i][j][k[0]] = int(k[2])# set number of injured to k state
                else:# if state k is in dict number count how many injured in that state
                    number[i][j][k[0]] += int(k[2])
    all_year = {}# this variable is for count number of injured each month and each year
    for i in number:# loop in number variable
        all_year[i] = {}# set dict year
        for j in number[i]:# loop in each state in "i" year
            for k in number[i][j]:# loop in each month in "j" state
                if not k in all_year[i]:# if sum of numberofinjured in "k" month in "i" year is not in variable make it
                    all_year[i][k] = number[i][j][k]
                else:# if sum is in dict plus it
                    all_year[i][k] += number[i][j][k]
    all_year['sum_year'] = 0# create key and values to keep sum of each year
    for i in all_year:# loop in sum of numberofinjured
        if i.isdigit():# check condition to fix some bug
            all_year[i]['one_year'] = 0# create key and values to keep sum of one year
            for j in all_year[i]:# loop in each month in "i" year
                if j.isdigit():# check condition to fix some bug
                    all_year['sum_year'] += all_year[i][j]# add numberofinjured in sum of all year
                    all_year[i]['one_year'] += all_year[i][j]# add numberofinjured in "i" year
    return number, all_year
    #number -> data contain how many injured happen each state and each month
    #all_year -> data contain how many injured happen each month each year and all

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
    return cut_data# this variable contain data from 2014 to 2016 and sort month data from jan to dec

def sort_sum(var):
    """sort data all_year and choose only sum of every year to save into variable"""
    cut_data = []
    temp3 = sorted(list(var.keys()))
    for i in temp3:
        if i.isdigit():
            cut_data.append(var[i]['one_year'])
    return cut_data

# def sort_state(var):

def graph_3year(data):
    """use data to plot graph 3 year with pygal module here"""
    line_chart = pygal.Line()
    line_chart.title = 'Gun crime for each month in 2014 - 2016'# change word later
    line_chart.x_labels = map(str, range(1, 13))# change x label here
    count = 0
    y_data = ['2014', '2015', '2016']
    for i in data:
        line_chart.add(y_data[count], data[count])
        count += 1
    line_chart.render_to_file('all_year.svg')

def graph_sum(data):
    line_chart = pygal.Line()
    line_chart.title = 'Gun crime for each year in 2014 - 2016'
    line_chart.x_labels = map(str, range(2014, 2017))# change x label here
    line_chart.add('numberofcrime death injured' , data)
    line_chart.render_to_file('sum_year.svg')

#def graph(data):

def main():
    """get input to choose what year to show here"""
    choose = input("2014, 2015, 2016, all or sum : ")
    data = collect_data()
    cal = []
    if choose.isdigit():
        cal.append(choose)
    elif choose == "all":
        cal = ["2014", "2015", "2016"]
    elif choose == "sum":
        cal = ["2014", "2015", "2016"]
    output_data = []
    output_data.append(numberofcrime(cal, choose, data))
    #output_data.append() add another function here
    if len(cal) > 1 and choose == "all":# if choose all year call function for 3 year
        graph_3year(output_data[0])
        #graph_3year(output_data[1])# make graph of dead
        #graph_3year(output_data[2])# make graph of injured
    elif len(cal) > 1 and choose == "sum":
        graph_sum(output_data[0])
    else:# if choose one year call function for 1 year
        for i in output_data:
            graph(i)

main()
