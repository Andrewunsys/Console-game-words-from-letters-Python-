import random 

""" Консольна игра - составить слова из слова или набора букв """

def create_word_and_guess_to_play_1(all_word_list):
	""" Формирование набора букв и на его основе списка слов для угадывания """

	# a='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
	abc=['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
	
	again=True
	while again:
		letters_count=random.randint(6, 11)
		counter=0
		abc_out=[]
		while counter<letters_count:
			aux_letter_tuple=random.choices(abc)
			aux_letter_str = ''.join(aux_letter_tuple)
			abc.remove(aux_letter_str)
			abc_out.append(aux_letter_str)
			counter+=1
		abc_out.sort() # Получен и отсортирован список букв из которых будем составлять слово
		abc_out_str=''.join(abc_out)

		# Проверяем, сколько из него можно составить слов. Если более 4, то выдаем этот список дальше
		out_list=[]
		for item_word in all_word_list:
			item_word_list=list(item_word)
			item_word_list.sort()
			item_word_list= list( dict.fromkeys(item_word_list) ) # Удаление дубликатов

			include=True

			for letter in item_word_list:
				if letter not in abc_out:
					include=False

			if include:
				out_list.append(item_word)

		if len(out_list)>4:
			again=False
			# print(abc_out_str, out_list)

			out_data=[abc_out_str, out_list]
			# print(out_data)

	return out_data


def create_word_and_guess_to_play_2(all_word_list):
	""" Формирование слова и на его основе списка слов для угадывания """
	
	# Составляем список из слов, длина которых не менее 11 символов	
	list_of_word=[]
	for i in all_word_list:
		if len(i)>=11:
			list_of_word.append(i)

	again=True
	while again:
		word_out = random.choices(list_of_word)

		word_out_str  = ''.join(word_out)	# Переводим в сроку
		word_out_list = list(word_out_str) 
		word_out_list.sort()
		word_out_list= list( dict.fromkeys(word_out_list) ) # Удаление дубликатов

		# Проверяем, сколько из него можно составить слов. Если более 4, то выдаем этот список дальше
		out_list=[]
		for item_word in all_word_list:
			item_word_list=list(item_word)
			item_word_list.sort()
			item_word_list= list( dict.fromkeys(item_word_list) ) # Удаление дубликатов

			include=True

			for letter in item_word_list:
				if letter not in word_out_list:
					include=False

			if include:
				out_list.append(item_word)
				# print(out_list)

		if len(out_list)>4:
			again=False
			# print('Успешная поверка на 4 и более вхождений',word_out_str, len(out_list), out_list)
		out_data=[word_out_str,out_list]
		# print(out_data)

	return out_data


def create_word_and_guess_to_play_3(all_word_list):
	""" Формирование слова и на его основе списка слов для угадывания """
	
	# Составляем список из слов, длина которых не менее 11 символов	
	list_of_word=[]
	for i in all_word_list:
		if len(i)>=11:
			list_of_word.append(i)

	again=True
	while again:
		word_out = random.choices(list_of_word)
		word_out_str  = ''.join(word_out)	# Переводим в сроку
		out_list=[]
		for i in all_word_list:
			i_str= ''.join(i)
			if i_str in word_out_str  and i_str!=word_out_str :
				out_list.append(i_str)
		# print(word_out_str, len(out_list), out_list)
		if len(out_list)>4:
			again=False
			out_data=[word_out_str,out_list]
			# print(out_data)

	return out_data


def print_guess_mask_list(mask_list, count_success, count_all):
	""" Функция вывода на экран информации о прогрессе и маскованного списка в четыре столбца.
	Для красоты ширина столбцов - единая и равна 25 символов. """

	counter=0
	msg='\t'
	lenght_colum=25
	for i in mask_list:
		counter+=1
		lenght_word=len(i)
		lenght_free_space = lenght_colum - lenght_word - 3
		msg_free_space = ' '* int(lenght_free_space)

		if counter%4==0:
			msg=f"{msg}{i}\n\t"
		else:
			msg=f"{msg}{i}{msg_free_space}"

	print(f"Угадано {count_success} слов из {count_all}. Прогресс {int(100 * count_success/count_all)} %")
	print(f"{msg}")


def play_round(all_word_list, number_of_game):
	""" Функция раунда игры """

	# Преобразование полного списка слов (возможно, из списка из одного элемента) в список строк
	word_list=[]
	for i in all_word_list:
		aux=''.join(i)
		word_list.append(aux)

	# Определение сетов в записимости от выбранной игры
	# Получаем список их двух элементов:
	# 	1. Слово или список букв из которых надо составить слова
	# 	2. на основаниее п.1 - список слов, которые надо угадать.
	# После создается маскированный список для угадываемых слов

	if number_of_game == 1:
		aux=create_word_and_guess_to_play_1(word_list)
		word_or_letter_to_play = aux[0]
		guess_list=aux[1]
		letter_str=''
		for i in word_or_letter_to_play:
			letter_str+= f"{i} "
		main_msg=f"\nСоставте слова из следующего набора букв: {letter_str}:"

	elif number_of_game == 2:
		aux=create_word_and_guess_to_play_2(word_list)
		word_or_letter_to_play = aux[0]
		guess_list=aux[1]
		main_msg=f"\nСоставте слова из слова: '{word_or_letter_to_play}' :"

	elif number_of_game == 3:
		aux=create_word_and_guess_to_play_3(word_list)
		word_or_letter_to_play = aux[0]
		guess_list=aux[1]
		main_msg=f"\nНайдите слова в следующем слове: '{word_or_letter_to_play}' :"

	# Создание маскированного списка. Маскированный представляет копию списка слов,
	# скоторые надо угадать. Но здесь все элементы списка заменены на звездочки *,
	# Количество звездочек соответствует длине слова. По мере угадывания слов 
	# элементы маскированного списка меняются со звездочек на угаданные слова.
	guess_mask_list=[]
	for i in guess_list:
		guess_mask_list.append('*'*len(i))

	# Основной цикл раунда
	again=True
	count_success=0

	while True:
		print(main_msg)
		print_guess_mask_list(guess_mask_list, count_success, len(guess_list))
		in_word = input("\n Введите ваш вариант:  ")
		print(f"\n")
		in_word.lower()
		if in_word == 'q' or in_word == 'Q':
			print("\nРаунд завершен досрочно. Ответы:\n")
			print_guess_mask_list(guess_list, count_success, len(guess_list))
			again=False
			break
		elif in_word == 'h' or in_word == 'H':
			print(main_msg)
			print("\n Раунд завершен досрочно. Правильные ответы и вариант пользователя\n")
			guess_list_length=len(guess_list)
			for i_guess_list in range(0,guess_list_length):
				print(f" - {guess_list[i_guess_list]}	- {guess_mask_list[i_guess_list]}")
			again=False
			break
		elif in_word in guess_list and in_word in guess_mask_list:
			print(f"Слово '{in_word}', вы уже вводили. Составте другое слово.")
		elif in_word not in guess_list and in_word not in guess_mask_list:
			print(f"Слово '{in_word}' не подходит. Составте другое слово.")
		elif in_word in guess_list and in_word not in guess_mask_list:
			print(f"Угадали! Слово '{in_word}' - подходит. Составте следующее слово.")
			index_in_word = guess_list.index(in_word)
			guess_mask_list[index_in_word]=in_word
			count_success += 1
		if count_success >= len(guess_list):
			print("\n!!! УРА !!! Вы угадали все слова !!! Поздравляем !!!\n")
			print_guess_mask_list(guess_mask_list, count_success, len(guess_list))
			again=False
			break


def prepare_all_word_list():
	""" Возвращает список из всех (почти) слов словаря.
	При обработке файла слова длиной менее трех символов игнорируются. Дубликаты удаляются"""

	word_list=[]	
	file_name='russian_popular_words-10_000.txt'
	file=open(file_name,'r')
	for i in file.readlines():
		aux=i.lower()
		aux1=aux.strip()
		if len(aux1)>=3:
			aux2=''.join(aux1)
			word_list.append(aux2)
	file.close()

	word_list.sort()
	word_list= list( dict.fromkeys(word_list) ) # Удаление дубликатов
	return word_list


def play_ruls():
	""" Правила игры """

	msg="\nПравила Игры:"
	msg+="\nНа экран выводится последовательность букв (Игра 1) или слово (Игра 2) из букв которых необходимо"
	msg+="\nсоставить все возможные слова. Длина угадываемого слова не менее трех символов."
	msg+="\nВ (Игре 3) необходимо найти возможные слова в составе слова (без перестановок букв)."
	msg+="\nПояснения и особенности:"
	msg+="\n - Слова должны быть из русского языка, существительные, не имена."
	msg+="\n - Слова используются из списка 10000 самых распространненных сществительных русского языка."
	msg+="\n - Словарь используется 'as is' и имеет некоторые неточности (отвутствуют некоторые известные слова, ...)."
	msg+="\n  - При игре выводятся маскированные ответы и угаданные слова."
	msg+="\n  - Для игры необходим файл со словарем с именем 'russian_popular_words-10_000.txt'."
	msg+="\n  - Для выхода из Игры нажмите 'q'."
	msg+="\n  - Для вывода всех ответов в Игры нажмите 'h'.\n"
	print(msg)	


def main():
	""" Основное меню игры и выхода из нее. Получение полного списка слов словаря из файла """

	# Получение полного списка слов словаря из файла
	all_word_list = prepare_all_word_list()

	# Основное меню игры и выхода из нее
	again=True
	while True:
		msg="\nМеню пунктов игры:"
		msg+="\n1) Игра: Составь слова из набора букв"
		msg+="\n2) Игра: Составь слова из букв слова"
		msg+="\n3) Игра: Составь слова из слова"
		msg+="\n4) Описание игры"
		msg+="\n5) Выход\n"
		print(msg)

		in_coose=input("Выберите пункт: ")
		print()
		if in_coose=='1':
			play_round(all_word_list, 1)
		elif in_coose=='2':
			play_round(all_word_list, 2)
		elif in_coose=='3':
			play_round(all_word_list, 3)
		elif in_coose=='4':
			play_ruls()
		elif in_coose=='5':
			print("Всего хорошего. До новой игры;)")	# "Have a nice time. Bye ;)"
			break
		else:
			print(f"Введено недопустимое значение: {in_coose}. Повторите выбор еще раз") # "Not correct choose! Please repeat input."
	

main()