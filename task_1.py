from sys import argv

script_name, working, rate, bonus = argv

print(f"Зароботная плата за месяц составляет: {int(working) * int(rate) + int(bonus)}")
