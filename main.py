#modules
import random
import os
import qrcode
#---



#libraries
UPPER_ru_letters = ["А", "Б", "В", "Г", "Д", "Е",
					"Ё", "Ж", "З", "И", "Й", "К",
					"Л", "М", "Н", "О", "П", "Р",
					"С", "Т", "У", "Ф", "Х", "Ц",
					"Ч", "Ш", "Щ", "Ъ", "Ы", "Ь",
					"Э", "Ю", "Я"]

LOWER_ru_letters = ["а", "б", "в", "г", "д", "е",
					"ё", "ж", "з", "и", "й", "к",
					"л", "м", "н", "о", "п", "р",
					"с", "т", "у", "ф", "х", "ц",
					"ч", "ш", "щ", "ъ", "ы", "ь",
					"э", "ю", "я"]

UPPER_en_letters = ["A", "B", "C", "D", "E", "F",
					"G", "H", "I", "J", "K", "L",
					"M", "N", "O", "P", "Q", "R",
					"S", "T", "U", "V", "W", "X",
					"Y", "Z"]

LOWER_en_letters = ["a", "b", "c", "d", "e", "f",
					"g", "h", "i", "j", "k", "l",
					"m", "n", "o", "p", "q", "r",
					"s", "t", "u", "v", "w", "x",
					"y", "z"]

specify_sign = ["!", "@", "#", "$", "%", "^",
				"&", "*", "№", ";", "%", ":",
				"?", "*", "-", "_", "+", "=",
				"/", "\\", "|", "~", "`", ".",
				",", "<", ">", "\"", "'", "(",
				")"]

answers_for_ball = ["Бесспорно.", "Предрешено.", "Никаких сомнений.", "Определённо да.", "Можешь быть уверен в этом.",
					"Мне кажется — да.", "Вероятнее всего.", "Хорошие перспективы.", "Знаки говорят — да.", "Да.",
					"Пока не ясно, попробуй снова.", "Спроси позже.", "Лучше не рассказывать.", "Сейчас нельзя предсказать.", "Сконцентрируйся и спроси опять.",
					"Даже не думай.", "Мой ответ — нет.", "По моим данным — нет.", "Перспективы не очень хорошие.", "Весьма сомнительно."]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

all_library = UPPER_ru_letters + LOWER_ru_letters + UPPER_en_letters + LOWER_en_letters
ru_password_library = UPPER_ru_letters + LOWER_ru_letters + specify_sign + numbers
en_password_library = UPPER_en_letters + LOWER_en_letters + specify_sign + numbers
all_password_library = UPPER_ru_letters + LOWER_ru_letters + specify_sign + UPPER_en_letters + LOWER_en_letters + numbers
#---



#start-settings
version_program = "1.0.3"
os.system("mode con cols=80 lines=40")
os.system("cls")
#---



#start/back/quit texts
start_text = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[~] eeazegen - генератор разного!
┃
┃[~] Функции:
┃(1) генератор числа.
┃(2) генератор букв.
┃(3) генератор пароля.
┃(4) генератор STEAM-KEY.
┃(5) генератор UPLAY-KEY.
┃(6) генератор QR-CODE.
┃(7) генератор ответа на вопрос (волшебный шар восьмёрка).
┃
┃[~] Hot-Keys:
┃(CTRL+C) выход/возвращение назад.
┃
┃[~] Автор: https://vk.com/eeaze | 2024 | {version_program}
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""

back_text = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[back] Вы возвращены назад!
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""

quit_text = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[quit] Выход из программы успешен!
┃
┃[~] Автор: https://vk.com/eeaze | 2024 | {version_program}
┃[~] Дискорд-сервер: https://discord.gg/invite/wcKbu76jDS
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
#---



#texts for functions
type_text = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[~] Тип данных:
┃
┃(1) целое число.
┃(2) десятичное число.
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""

answer_ball_text = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[~] Этот генератор имеет в себе ответы "Шар восьмёрка".
┃[~] Этот шар считается волшебным и его ответы предсказывают
┃[~] ~б~у~д~у~щ~е~е~
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""

qr_code_text = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[~] Простой генератор QR-CODE.
┃[~] Имя файла можно изменить. А можно и не менять.
┃[~] Создай свой QR-CODE.
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
#---



#errors texts
error_text = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[X] Что-то пошло не так. Попробуйте заново.
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""

error_gen_text = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[X] Генератор не найден.
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""

error_library_text = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[X] Такой библиотеки нет.
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
#---



#make-text
def except_make(text):
	os.system("cls")
	print(text)
#---



#global-code
def choose_func(choose):
	try:
		#random-number
		if int(choose) == 1:
			try:
				os.system("cls")
				print(type_text)

				choose_type = int(input("\n[>>>] Какой тип чисел вам нужен: "))
				number = int(input("[>>>] Введите до какого числа нужен рандом: "))

				if choose_type == 1:
					os.system("cls")
					print(f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[+] Рандомное число: {random.randrange(0, number+1)}
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")

				elif choose_type == 2:
					os.system("cls")
					print(f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[+] Рандомное число: {random.random() * number}
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")

				else:
					except_make(error_text)
				
			except KeyboardInterrupt:
				except_make(back_text)
				
			except:
				except_make(error_text)
#---



#generation-letter
		elif int(choose) == 2:
			try:
				os.system("cls")
				print(f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[~] Словари для генерации:
┃
┃(1) Заглавные русские буквы. (А,Б,...)
┃(2) Строчные русские буквы. (а,б,...)
┃(3) Заглавные английские буквы. (A,B,...)
┃(4) Строчные английские буквы. (a,b,...)
┃(5) Все библиотеки.
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")

				choose_library = input("\n[>>>] Введите номер библиотеки: ")
				length_str = input("[>>>] Введите длину текста: ")

				def complete_def(complete):
					result = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[+] Рандомные буквы: {"".join(complete)}
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
					return result

				if int(choose_library) == 1:
					os.system("cls")
					print(complete_def(random.choices(UPPER_ru_letters, k=int(length_str))))

				elif int(choose_library) == 2:
					os.system("cls")
					print(complete_def(random.choices(LOWER_ru_letters, k=int(length_str))))

				elif int(choose_library) == 3:
					os.system("cls")
					print(complete_def(random.choices(UPPER_en_letters, k=int(length_str))))

				elif int(choose_library) == 4:
					os.system("cls")
					print(complete_def(random.choices(LOWER_en_letters, k=int(length_str))))

				elif int(choose_library) == 5:
					os.system("cls")
					print(complete_def(random.choices(all_library, k=int(length_str))))

				else:
					except_make(error_library_text)
				
			except KeyboardInterrupt:
				except_make(back_text)
				
			except:
				except_make(error_text)
#---



#password
		elif int(choose) == 3:
			try:
				os.system("cls")
				print(f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[~] Словари для генерации:
┃
┃(1) Русские буквы, знаки и цифры. (А,б,!,5,...)
┃(2) Английские буквы, знаки и цифры. (A,b,!,5,...)
┃(3) Все библиотеки.
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")

				choose_library = input("\n[>>>] Введите номер библиотеки: ")
				length_password = input("[>>>] Введите длину пароля: ")

				def gen_password_def(generated):
					result = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 
┃[+] Рандомный пароль: {"".join(generated)}
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
					return result

				if int(choose_library) == 1:
					os.system("cls")
					print(gen_password_def(random.choices(ru_password_library, k=int(length_password))))

				elif int(choose_library) == 2:
					os.system("cls")
					print(gen_password_def(random.choices(en_password_library, k=int(length_password))))

				elif int(choose_library) == 3:
					os.system("cls")
					print(gen_password_def(random.choices(all_password_library, k=int(length_password))))

				else:
					except_make(error_library_text)
				
			except KeyboardInterrupt:
				except_make(back_text)
				
			except:
				except_make(error_text)
#---



#steam-key
		elif int(choose) == 4:
			try:
				os.system("cls")
				one = random.choices(UPPER_en_letters + numbers, k=5)
				two = random.choices(UPPER_en_letters + numbers, k=5)
				three = random.choices(UPPER_en_letters + numbers, k=5)
				four = random.choices(UPPER_en_letters + numbers, k=5)
				five = random.choices(UPPER_en_letters + numbers, k=5)

				def steam_key(one, two, three, four, five):
					key = "".join(one) + "-" + "".join(two) + "-" + "".join(three) + "-" + "".join(four) + "-" + "".join(five)
					result = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[+] Рандомный STEAM-KEY: {key}
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
					return result

				print(steam_key(one, two, three, four, five))
				
			except KeyboardInterrupt:
				except_make(back_text)
				
			except:
				except_make(error_text)
#---



#uplay-key
		elif int(choose) == 5:
			try:
				os.system("cls")
				one = random.choices(UPPER_en_letters + numbers, k=4)
				two = random.choices(UPPER_en_letters + numbers, k=4)
				three = random.choices(UPPER_en_letters + numbers, k=4)
				four = random.choices(UPPER_en_letters + numbers, k=4)

				def uplay_key(one, two, three, four):
					key = "".join(one) + "-" + "".join(two) + "-" + "".join(three) + "-" + "".join(four)
					result = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[+] Рандомный UPLAY-KEY: {key}
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
					return result

				print(uplay_key(one, two, three, four))

			except KeyboardInterrupt:
				except_make(back_text)
				
			except:
				except_make(error_text)
#---



#qr-code
		elif int(choose) == 6:
			try:
				os.system("cls")
				print(qr_code_text)

				def qrcode_make(data, name):
					name = f"{name}.png"
					os.system("cls")

					img = qrcode.make(data)
					type(img)

					if name != ".png":
						img.save(name)

					else:
						name = "qr_code.png"
						img.save(name)

					result = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[+] QR-CODE создан. Имя файла: "{name}".
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
					return result

				data = input("\n[>>>] Введите URL/TEXT: ")
				name = input("[>>>] Введите имя файла: ")
				print(qrcode_make(data, name))

			except KeyboardInterrupt:
				except_make(back_text)

			except:
				except_make(error_text)
#---



#magic ball
		elif int(choose) == 7:
			try:
				os.system("cls")
				print(answer_ball_text)

				def gen_answers(ask):
					os.system("cls")
					result = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃
┃[+] Ответ на ваш вопрос: {''.join(random.choices(answers_for_ball, k=1))}
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
					return result

				ask = input("\n[>>>] Введите ваш вопрос: ")
				print(gen_answers(ask))

			except KeyboardInterrupt:
				except_make(back_text)

			except:
				except_make(error_text)



		else:
			except_make(error_gen_text)

	except KeyboardInterrupt:
		except_make(back_text)
			
	except:
		except_make(error_gen_text)
#---
#---



#repeat-code
while True:
	try:
		print(start_text)
		choose = input("\n[>>>] Введите запрос: ")
		choose_func(choose)
		
	except KeyboardInterrupt:
		os.system("cls")
		print(quit_text)
		try:
			input("\n[(^-^)] Нажмите Enter для выхода.")
			quit()
		except:
			quit()
#---