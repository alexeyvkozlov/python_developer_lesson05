#~ USAGE
# cd c:\python_developer
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd c:\python_developer\lesson_05
# cd d:\python_developer\lesson_05
#~~~~~~~~~~~~~~~~~~~~~~~~
# python console_file_manager.py
#~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import platform
import getpass
import random

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 9. Играть в викторину
famous_people = [
  ("Александр Сергеевич Пушкин", "06.06.1799"),
  ("Альберт Эйнштейн", "14.03.1879"),
  ("Махатма Ганди", "02.10.1869"),
  ("Мартин Лютер Кинг", "15.01.1929"),
  ("Стив Джобс", "24.02.1955"),
  ("Леонардо да Винчи", "15.04.1452"),
  ("Мэри Кюри", "07.11.1867"),
  ("Нельсон Мандела", "18.07.1918"),
  ("Вольфганг Амадей Моцарт", "27.01.1756"),
  ("Майя Анжелу", "04.04.1928")
]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def format_date(date):
  day, month, year = date.split('.')
  months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
  return f"{int(day)} {months[int(month) - 1]} {year} года"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def play_quiz():
  selected_people = random.sample(famous_people, 5)
  correct_answers = 0
  incorrect_answers = 0

  for famous_person, birth_date in selected_people:
    answer = input(f"Введите дату рождения {famous_person} (в формате 'dd.mm.yyyy'): ")
    if answer == birth_date:
      correct_answers += 1
    else:
      incorrect_answers += 1
      print(f"Неверно! Правильный ответ: {format_date(birth_date)}")

  print("\nРезультаты:")
  print(f"Количество правильных ответов: {correct_answers}")
  print(f"Количество ошибок: {incorrect_answers}")

  restart = input("Хотите начать заново? (да/нет): ")
  if restart.lower() == "да":
    play_quiz()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 10. Мой банковский счет
balance = 0
purchase_history = []

def deposit_money():
  global balance
  amount = float(input('Введите сумму для пополнения счета: '))
  balance += amount
  print('Счет пополнен на', amount, 'рублей')
  show_bank_menu()

def make_purchase():
  global balance
  global purchase_history
  amount = float(input('Введите сумму покупки: '))
  if amount > balance:
    print('У вас недостаточно средств на счете')
  else:
    item = input('Введите название покупки: ')
    balance -= amount
    purchase_history.append((item, amount))
    print('Покупка совершена')
  show_bank_menu()

def show_purchase_history():
  print('История покупок:')
  for item, amount in purchase_history:
    print(item, '-', amount, 'рублей')
  show_bank_menu()

def show_bank_menu():
  print('1. пополнение счета')
  print('2. покупка')
  print('3. история покупок')
  print('4. выход')

  choice = input('Выберите пункт меню: ')
  if choice == '1':
    deposit_money()
  elif choice == '2':
    make_purchase()
  elif choice == '3':
    show_purchase_history()
  elif choice == '4':
    exit()
  else:
    print('Неверный пункт меню')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 1. Создать папку
def create_folder():
  folder_name = input("Введите название папки для создания: ")
  try:
    os.mkdir(folder_name)
    print("Папка", folder_name, "создана")
  except FileExistsError:
    print("Папка", folder_name, "уже существует")
  show_main_menu()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 2. Удалить файл/папку
def delete_file_or_folder():
  item_name = input("Введите название файла или папки для удаления: ")
  try:
    os.remove(item_name) if os.path.isfile(item_name) else os.rmdir(item_name)
    print(item_name, "удален(а)")
  except FileNotFoundError:
    print("Файл или папка не найдены")
  show_main_menu()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 3. Копировать файл/папку
def copy_file_or_folder():
  source = input("Введите название файла или папки для копирования: ")
  destination = input("Введите путь для копирования: ")
  try:
    if os.path.isfile(source):
      os.system(f'copy {source} {destination}')
    else:
      os.system(f'xcopy {source} {destination} /E /I')
    print(source, "скопирован(а) в", destination)
  except FileNotFoundError:
    print("Файл или папка не найдены")
  show_main_menu()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 4. Просмотр содержимого рабочей директории
def list_directory_contents():
  print("Содержимое рабочей директории:")
  for item in os.listdir():
    print(item)
  show_main_menu()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 5. Посмотреть только папки
def list_only_folders():
  print("Папки в рабочей директории:")
  for item in os.listdir():
    if os.path.isdir(item):
      print(item)
  show_main_menu()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 6. Посмотреть только файлы
def list_only_files():
  print("Файлы в рабочей директории:")
  for item in os.listdir():
    if os.path.isfile(item):
      print(item)
  show_main_menu()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 7. Просмотр информации об операционной системе
def display_system_info():
  print("Информация об операционной системе:")
  print(f"Операционная система: {platform.system()} {platform.release()}")
  print(f"Имя пользователя: {getpass.getuser()}")
  show_main_menu()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ 8. Создатель программы
def display_creator_info():
  print("Создатель программы: Алексей Козлов")
  show_main_menu()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def show_main_menu():
  print("""
Меню:
1. Создать папку
2. Удалить файл/папку
3. Копировать файл/папку
4. Просмотр содержимого рабочей директории
5. Посмотреть только папки
6. Посмотреть только файлы
7. Просмотр информации об операционной системе
8. Создатель программы
9. Играть в викторину
10. Мой банковский счет
11. Выход
""")
  choice = input("Выберите пункт меню: ")
  
  if choice == '1':
    create_folder()
  elif choice == '2':
    delete_file_or_folder()
  elif choice == '3':
    copy_file_or_folder()
  elif choice == '4':
    list_directory_contents()
  elif choice == '5':
    list_only_folders()
  elif choice == '6':
    list_only_files()
  elif choice == '7':
    display_system_info()
  elif choice == '8':
    display_creator_info()
  elif choice == '9':
    play_quiz()
  elif choice == '10':
    show_bank_menu()
  elif choice == '11':
    exit()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
show_main_menu()
