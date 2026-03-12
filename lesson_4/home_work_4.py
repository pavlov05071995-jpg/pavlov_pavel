print("\n Методы строк")
print("\n 1. Работа с регистром")
s = "Python для автоматизации"
print(f"Вверхний регистр строки s= {s.upper()}")
print(f"Нижний регистр строки s= {s.lower()}")

print("\n 2. Подсчет вхождений подстроки")
msg = "абракадабра"
print(f"Cколько раз встречается подстрока \"ра\" в строке msg? Ответ:{msg.count("ра")}")
print(f"количество \"а\", начиная с 3-го символа: {msg.count('а',3)}")

print("\n 3. Поиск подстроки")
print(f"Индекс первого вхождения 'ка': {msg.find("ка")}")
print(f"Индекс последнего вхождения 'а': {msg.rfind("a")}")
print(f"Поиск 'xyz' вернет: {msg.find("xyz")}")
try:
    index_error = msg.index("xyz")
except ValueError as e:
    print(f"Метод index() для 'xyz' выбросил исключение: {e}")

print("\n 4. Замена подстроки")
text = "Я изучаю Java"
print(f"Замени \"Java\" на \"Python\": {text.replace('Java', 'Python')}")
print(f"Удали все пробелы из строки: {text.replace(' ', '')}")

print("\n 5. Проверка содержимого строки")
print(f"Строка 'Python' состоит только из букв: {'Python'.isalpha()}")
print(f"состоит ли строка \"12345\" только из цифр: {"12345".isdigit()}")
print(f"строка \"123abc\" не состоит только из цифр: {not'123abc'.isdigit()}")

print("\n 6. Дополнение строк")
code="42"
print(code.rjust(8,"0"))
print("text".ljust(10,"*"))

print("\n 7. Разбиение строк")
frut="яблоко, груша, банан"
print(frut.split(", "))
languages = "Python;Java;C++"
languages_list = languages.split(";")
print("2. Разбиение строки с языками программирования:")
print(f"   Исходная строка: '{languages}'")
print(f"   Результат: {languages_list}")
print(f"   Тип результата: {type(languages_list)}")
print(f"   Количество элементов: {len(languages_list)}")

print("\n 8. Объединение списка в строку")
print(' '.join(["Привет", "мир", "!"]))
print(', '.join(["apple", "banana", "cherry"]))

print("\n 9. Удаление пробелов")
print("     Python".lstrip())
print("Python    ".rstrip())
print("     Python     ".strip())

print("\n 10. Дополнительное задание")
text = "программирование"
print(text.replace("п", "П"))
print(f"кол-во букв \"р\" в строке text: {text.count("р")}")
print(f"индекс первой буквы \"и\"= {text.find("а")}")
print(f"Развернутая строка {text[::-1]}")

print("\n Спецсимволы")
print("\n 1. Перевод строки")
text = "Hello\nPython"
print(text)
print(r"Строка содержит специальный символ \n -он интерпретирует его как команду перейти на новую строку")

print("\n 2. Горизонтальная табуляция")
t = "Python\tAutomation"
print(t)
print(r"""\t (backslash-t) — это escape-последовательность,
 которая обозначает символ горизонтальной табуляции (tab). 
 При выводе на экран он перемещает курсор к следующей позиции табуляции (обычно к колонке, кратной 8 пробелам)""")


print("\n 3. Экранирование символов")
path = "C:\\new\\test.txt"
print(path)
print("Марка вина \"Ягодка\"")

print("\n 4. Сырые (raw) строки")
print(r"C:\new\test.txt" )
print(r"""# - Обычная строка интерпретирует \n, \t как спецсимволы
# - Сырая строка сохраняет обратные слеши как обычные символы
# - Сырые строки идеальны для путей Windows и регулярных выражений""")


print("\n 5. Использование разных спецсимволов")
s = "Hello\b World"
print(s)
print(r"\b - удаляет предыдущий символ")
s = "Hello\fPython"
print(s)
print(r"\f - символ перевода страницы, в современных терминалах отображается как спецсимвол")

print("\n Форматирование строк")
print("\n 1. Формирование строк через конкатенацию")
name=('pavel')
age=20
result = "Меня зовут " + name + ", мне " + str(age) + " лет."
print(result)
try:
    error_result = "Меня зовут " + name + ", мне " + age + " года."
    print(error_result)
except TypeError as e:
    print(f"Ошибка при попытке сложить строку и число без преобразования: {e}")

print("\n 2. Форматирование строк с .format()")
msg="Привет, меня зовут {0}, мне {1} лет.".format("Pavel","20")
print(msg)
msg_1="Привет, меня зовут {имя}, мне {возраст} лет.".format(имя=name,возраст=age)
print(msg_1)
msg_2="Привет, меня зовут {1}, мне {0} лет.".format("Pavel","20")
print(msg_2)

print("\n 3. Использование F-строк")
city='Новокузнецк'
year=2026
print(f"Сегодня {city} год, и я живу в {year}.")
print(f"Через 5 лет будет {year + 5} год.")

print("\n 4. Операции внутри F-строк")
print(f"Дважды мой возраст: {age * 2}")
print(f"Дважды мой возраст: {age}{age}")
print(f"Меня зовут {name.upper()}")

print("\n 5. Дополнительное задание")
usd=1
rub=92.5
msg_3="Курс валют: {0} доллар = {1} рубля.".format(usd, rub)
print(msg_3)
print(f"Квадрат числа 7 равен {7**2}.")

