#ЗАДАНИЕ 1
name="Pavel"
age=30
height=1.80
print("ИМЯ:",name)
print("ВОЗРАСТ:",age)
print("РОСТ:",height)
# Не совсем понял что подразумевалось под "Поясняющими подписями"-надеюсь правильно понял

#ЗАДАНИЕ 2
x = 10
print("Значение x:", x)
print("Тип переменной x:", type(x))
x = 25.5
print("\nНовое значение x:", x)
print("Тип переменной x:", type(x))
x = "Python"
print("\nНовое значение x:", x)
print("Тип переменной x:", type(x))
print("\nФинальное значение x:", x)

#ЗАДАНИЕ 3

a=7
b=a
print(a,b)
a=10
print(b)
#Это происходит потому, что числа в Python являются неизменяемыми объектами. Когда мы присваиваем новое значение числовой переменной, создается новый объект, а не изменяется существующий

#Задание 4

x=y=z=100
print(id(x),id(y),id(z)) #в данном случае выведет одинаковые идентификаторы

x,y,z=10,20,30
print(id(x),id(y),id(z)) # в данном случае выведет разные идентификаторы

#Задание 5
a=5
b=10
a,b=b,a
print("b:",b, "a:",a)

#Задание 6
import keyword
print(keyword.kwlist)

#Задание 7
var1 = 42
var2 = 3.14
var3 = "Hello"
print("Значение_1:",type(var1),"Значение_2:",type(var2),"Значение_3:",type(var3))
var1="Любое значение"
print("Значение_1 после изменений:",type(var1))

#Задание 8
firstName="Pavel"
myFingersHand=10
humanTemperature=36.6
student=True
print("Значения и типы переменных:")
print(f"Имя = {firstName}, тип: {type(firstName)}")
print(f"Пальцы на руке = {myFingersHand}, тип: {type(myFingersHand)}")
print(f"Температура человека = {humanTemperature}, тип: {type(humanTemperature)}")
print(f"студент? = {student}, тип: {type(student)}")
#8.2 - вообще можно называть переменые кирилицей , но лучше так не делать 
переменная=10
print(переменная)
