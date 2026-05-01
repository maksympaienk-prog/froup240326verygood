# main.py
import poems
import sign

# Ім'я автора
author_name = "Олександр Іванов"

# Вивід підпису через .format
print(sign.SIGN_TEMPLATE.format(name=author_name))

# Побажання одним рядком з \n
wishes = "Більше практичних завдань\nЦікавих розборів коду"
print(wishes)

# Розділювач
stars = "**************************************************************************"

# Вивід віршів
print(stars)
print(poems.ZAPOVIT)
print(stars)
print(poems.MENI_ODNAKO)
print(stars)
