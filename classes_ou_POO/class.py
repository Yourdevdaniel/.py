class Ficha: # Convenção é usar a primeira letra maiúscula para classes
    def __init__(self, name, age, Marital_Status, sexuality, phone_number, country, city, sex):
        self.name = name
        self.age = age
        self.Marital_Status_ = Marital_Status
        self.sexuality = sexuality
        self.phone_number = phone_number
        self.country = country
        self.city = city
        self.sex = sex

    def exibir_ficha(self):
        print("--------------------------")
        print("Personal Details")
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"sex: {self.sex}")
        print(f"Marital Status: {self.Marital_Status}")
        print(f"sexuality: {self.sexuality}")
        print(f"phone_number: {self.phone_number}")
        print(f"País: {self.country}")
        print(f"city: {self.city}")
        print("The end.")
        print("--------------------------")

def new_record():
    print("Enter yours details")
    name_input = input("name: ")
    age_input = int(input("age: ")) # Converte para int
    Marital_Status_input = input("Marital_Status: ")
    sexuality_input = input("sexuality: ")
    sex_input = input("sex: ")
    phone_number_input = input("phone_number: ")
    country_input = input("País: ")
    city_input = input("city: ")
    return name_input, age_input, Marital_Status_input, sexuality_input, \
           phone_number_input, country_input, city_input, sex_input


colected_data = new_record()

name_final, age_final, Marital_Status_final, sexuality_final, \
phone_number_final, country_final, city_final, sex_final = colected_data


new_record = Ficha(name_final, age_final, Marital_Status_final,
                   sexuality_final, phone_number_final, country_final, city_final, sex_final)

new_record.exibir_ficha()