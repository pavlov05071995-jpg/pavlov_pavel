
#Задание 1
print("\nЗадание 1-1")
a= 8
b= 3
x= 2.5
y= -1.7
print("a",type(a))
print("b", type(b))
print("x", type(x))
print("y",type(y))
print()
#Задание 2
print("\nЗадание 1-2")
num1= 9
num2= -2
print("Сложение: ",num1 + num2)
print("Вычитание: ",num1 - num2)
print("Умножение: ",num1 * num2)
print("Деление: ",num1 / num2)
print("Целочисленое деление: ", num1 // num2)
print("Остаток от деления: ", num1 % num2)
print("Возведение в степень: ", num1 ** num2)
print()
#Задание 3
print("\nЗадание 1-3")
# Первый случай: a = 10, b = 3
a = 10
b = 3
print("Случай 1: a = 10, b = 3")
print(f"a / b = {a / b}")    # Деление с плавающей точкой
print(f"a // b = {a // b}")  # Целочисленное деление
print(f"a % b = {a % b}")    # Остаток от деления
print()

# Второй случай: a = -10, b = 3
a = -10
b = 3
print("Случай 2: a = -10, b = 3")
print(f"a / b = {a / b}")    # Деление с плавающей точкой
print(f"a // b = {a // b}")  # Целочисленное деление
print(f"a % b = {a % b}")    # Остаток от деления
print()

# Третий случай: a = 10, b = -3
a = 10
b = -3
print("Случай 3: a = 10, b = -3")
print(f"a / b = {a / b}")    # Деление с плавающей точкой
print(f"a // b = {a // b}")  # Целочисленное деление
print(f"a % b = {a % b}")    # Остаток от деления
print()

#Задание 4
print("\nЗадание 1-4")
a=5
b=3
c=2
calc1= a + b * c
calc2= (a + b) * c
calc3= (a + a) / c ** c
print(calc1)
print(calc2)
print(calc3)

#Задание 5
print("\nЗадание 1-5")
# Создаем начальную переменную
count = 10
print(f"Начальное значение: count = {count}")

# Увеличиваем на 5
count += 5
print(f"После += 5: count = {count}")

# Уменьшаем на 3
count -= 3
print(f"После -= 3: count = {count}")

# Умножаем на 2
count *= 2
print(f"После *= 2: count = {count}")

# Делим на 4
count /= 4
print(f"После /= 4: count = {count}")

# Итоговое значение
print(f"\nИтоговое значение count: {count}")

#Задание 1
print("\nЗадание 2-1")
s1="Python"
s2="Программирование"
print(s1 + " " + s2)
print("""
Python
programming
""")
empty = "    "
print("Длина строки empty:", len(empty))

#Задание 2
print("\nЗадание 2-2")
first_name = "Иван"
last_name = "Петров"
full_name= f"{first_name} {last_name}"
print(full_name)

#Задание 3
print("\nЗадание 2-3")
s="возраст"
age=25
print(s + ":" + str(age))

#Задание 4
print("\nЗадание 2-4")
x="xa "*5
print("смех:"+x)
#  "ха " * 2.5 - нельзя будет вывести так как str не может использоваться с дробными числами

#Задание 5
print("\nЗадание 2-5")
text = "Привет, мир!"
print ("Длина строки:",len(text))
text1=""
print("Длина пустой строки:", len(text1))

#Задание 6
print("\nЗадание 2-6")
sentence = "Я изучаю Python"
p="Python" in sentence
j="Java" in sentence
print("содержит ли слово Python переменная sentence?- ", p)
print("содержит ли слово Java переменная sentence?- ", j)

#Задание 7
print("\nЗадание 2-7")
a = "apple"
b = "banana"

print(f"a == b (равны ли строки?): {a == b}")
print(f"a != b (не равны ли строки?): {a != b}")
print(f"a < b (a меньше b?): {a < b}")
print(f"a > b (a больше b?): {a > b}")
print(f"a <= b (a меньше или равно b?): {a <= b}")
print(f"a >= b (a больше или равно b?): {a >= b}")

#Задание 8
print("\nЗадание 2-8")
code_A = ord('A')
code_a = ord('a')
code_Я = ord('Я')
print("код А:", code_A)
print("код а:", code_a)
print("код Я:", code_Я)