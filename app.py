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
    global avgdata
    avgdata = []
    sumrow = 0
    for i in range(10):
        for x in range(30):
            sumrow += data[i+1][x+1]
        sumrow = sumrow/30
        avgdata.append(sumrow)
    for index, item in enumerate(avgdata):
        print(data[index][0], ": $", round(item))
def avgsort():
    sorted_data = avgdata.sort()