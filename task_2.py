def person_date(first_name, second_name, dbo, city, email, tel):
    print(f"{second_name} {first_name} дата рождения:{dbo} город проживания:{city} email:{email} телфон:{tel}")


person_date(first_name=input("Имя: "), second_name=input("Фамилия: "), dbo=input("Дата рождения: "),
            city=input("Город проживания: "), email=input("email: "), tel=input("Телефон: "))