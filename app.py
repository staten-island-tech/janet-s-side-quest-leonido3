## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)
    return data_list


file_path = "SalesData.csv"  
data = csv_to_list(file_path)
def avgcalc():
    global full_data, avgdata
    avgdata = []
    sumrow = 0
    for i in range(10):
        for x in range(30):
            sumrow += data[i+1][x+1]
        sumrow = sumrow/30
        avgdata.append(round(sumrow))
    full_data = []
    for index, item in enumerate(avgdata):
        full_data.append((f"{data[index+1][0]}", item))
    print(full_data)
avgcalc()
def sort_data():
    sorted_data = []
    numsort = sorted(avgdata)
    for i in range(len(numsort)):
        for x in range(len(full_data)):
            if numsort[i] == full_data[x][1]:
                sorted_data.append((full_data[x][0], numsort[i]))
    print(sorted_data)
sort_data()
def allavg():
    avgdatasum = sum(avgdata)
    fullavg = avgdatasum/len(avgdata)
    print(f"Full average: {fullavg}")
allavg()
def underperf():