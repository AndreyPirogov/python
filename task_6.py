file = open("task_6.txt")

content = file.readlines()
dic_content = {}
file.close()

for el in content:
    sum_hour = 0
    name = ""
    el_sp = el.split()
    for i in el_sp:
        if i.endswith(":"):
            name = i[:len(i) - 1]
        if i.find("(л)") != -1 or i.find("(пр)") != -1 or i.find("(лаб)") != -1:
            num = ""
            for a in i:
                if a.isdigit():
                    num += a
            sum_hour += int(num)
    dic_content.update({name: sum_hour})


print(dic_content)
