import json

profit_middle = 0
count = 1
list_result = []
dic_result = {}

with open("task_7.txt") as file:
    content = file.readlines()
    for el in content:
        list_content = el.split()
        name = list_content[0]
        profit = int(list_content[2]) - int(list_content[3])
        if profit >= 0:
            profit_middle += profit / count
            count += 1
        dic_result.update({name: profit})

list_result.append(dic_result)
list_result.append({"average_profit": profit_middle})

with open("task_7.json", "w") as file:
    json.dump(list_result, file)

