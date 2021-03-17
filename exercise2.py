time = int(input("Введите количество секунд: "))

second = time % 60
minute = time // 60 % 60
hour = time // 60 // 60

print(f"{hour}:{minute}:{second}")
