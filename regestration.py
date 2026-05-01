import massages

# 1. Ім'я
name_input = input(massages.MSG_INPUT_NAME).strip()
if name_input.isalpha():
    formatted_name = name_input.title()
    print(massages.MSG_NAME_OK.format(name=formatted_name))
else:
    print("Помилка: Ім'я має містити лише літери.")

# 2. Вік
age_input = input(massages.MSG_INPUT_AGE).strip().lstrip('0')
if age_input.isdigit():
    print(massages.MSG_AGE_OK.format(age=age_input))
else:
    print("Помилка: Вік має бути цілим числом.")

# 3. Номер телефону
phone_input = input(massages.MSG_INPUT_PHONE).replace(" ", "")
if phone_input.isdigit():
    print(massages.MSG_PHONE_OK.format(phone=phone_input))
else:
    print("Помилка: Номер телефону має містити лише цифри.")

# 4. Завершення
print(massages.MSG_FINISH)
