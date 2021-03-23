product_list = []

print("Заполняем список товаров, для выхода введите 'exit'")
count = 1
while True:
    description_product = {}
    description_product.update({'Название': input("Название: ")})
    description_product.update({'Цена': input("Цена: ")})
    description_product.update({'Количество': input("Количество: ")})
    description_product.update({'eд': input("Еденицы: ")})
    product_list.append((count, description_product))
    count = count + 1
    if input("Для выхода введите 'exit' ") == "exit":
        break

analysis_dic = {'Название': [], 'Цена': [], 'Количество': [], 'eд': []}

for number, order in product_list:
    analysis_dic.get("Название").append(order.get("Название"))
    analysis_dic.get("Цена").append(order.get("Цена"))
    analysis_dic.get("Количество").append(order.get("Количество"))
    analysis_dic.get("eд").append(order.get("eд"))

print(analysis_dic)
