total_sum = 0
user_input = input("შეიყვანეთ დადებითი რიცხვი (ჩაწერეთ 'sum' ჯამის მისაღებად): ")

while not user_input == "sum":
    if user_input.isdigit() and int(user_input) > 0:
        total_sum += int(user_input)
    user_input = input("შეიყვანეთ დადებითი რიცხვი (ჩაწერეთ 'sum' ჯამის მისაღებად): ")
else:
    print(f"თქვენ მიერ შეყვანილი რიცხვების ჯამია: {total_sum}")
