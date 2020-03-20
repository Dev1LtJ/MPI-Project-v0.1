# Подгружаем модуль Time
import time
# Подгружаем модуль Math
import math
# Подгружаем модуль Scipy SciPy.stats (нужен для расчета коэффициента Стьдента)
import scipy.stats
# Подгружаем модуль Colorama
from colorama import init # нужно для того, чтобы цвета работали в консоли винды
from colorama import Fore, Back, Style # Fore - цвет текста, Back - цвет фона, Style - хз
init(autoreset=True) # Инициализируем

# Приветствие
__version__ = Fore.YELLOW + Style.BRIGHT + 'v0.1'
print(Fore.GREEN + Style.BRIGHT + "Программа для расчета МПИ", __version__,'\n')
time.sleep (0.75)
print(Fore.BLUE + Style.BRIGHT + "By Alexander Razumny")
time.sleep (0.75)

# Функция: проведение расчетов
def iteration ():
# Функция проверки, является ли введенное значение целым неотрицательным числом и без символов
	def isint (arg):
		try:
			if arg.isdecimal():
				return True
		except:
			return False

# Функция проверки, является ли введенное значение неотрицательным числом и без символов
	def isfloat (arg):
		try:
			if arg.isdecimal():
				return True
			elif float(arg):
				return True
		except:
			return False

# Вводим переменные, которые не нужно обрабатывать:
	print(Fore. CYAN + Style.BRIGHT +"\nВведите исходные данные:")
	time.sleep (0.75)
	while True:
		Tn = input("Введите нормируемое значение наработки на отказ, ч: " + Fore.YELLOW + Style.BRIGHT)
		if isint (Tn) != True:
			print(Fore.RED + Style.BRIGHT +"Строка не должна содержать букв, +, -, ' ', и т.д. и быть целочисленной")
			continue
		Delta = input(Style.RESET_ALL + "Введите нормируемую погрешность СИ, %: " + Fore.YELLOW + Style.BRIGHT)
		if isfloat (Delta) != True:
			print(Fore.RED + Style.BRIGHT +"Строка не должна содержать букв, +, -, ' ', и т.д.")
			continue
		else:
			Tn = int(Tn)
			Delta = float(Delta)
			DeltaE = Delta	
			break
# Функция проверки, является ли введенное значение целым неотрицательным числом и без символов
# Отличие от функции isint в том, что в данном случае enter как исключение возвращает прописанное дефолтное значение
	def isint_2 (arg):
		try:
			if arg.isdecimal() or not P_perc:
				return True
		except:
			return False

# Ввод доверительной вероятности и расчет квантиля

	while True:
		P_list = list(range(1, 100)) # Задачем диапазон возможных значений
		P_perc = input(Style.RESET_ALL + "Введите доверительную вероятность [1 ... 99 %]: "+ Fore.YELLOW + Style.BRIGHT)
		if isint_2 (P_perc) != True:
			print(Fore.RED + Style.BRIGHT + "Строка не должна содержать букв, +, -, ' ', '.' и т.д. [нажатие enter установит стандартное значением для СЗМ]")
			continue
		elif not P_perc: # Реализуем возврат дефолтного при отсутствии введенного значения
			P = 0.95
			lmbd = scipy.stats.t.ppf ((1 + P)/2, 999 - 1)
			print(Fore.RED + Style.BRIGHT + "Если доверительная вероятность не указана, то принимается как 95 %")
			print("Квантиль при P = " + Fore.GREEN + Style.BRIGHT + "95 " + Style.RESET_ALL + "будет: " + Fore.GREEN + Style.BRIGHT + str(lmbd))
			break
		P_perc = int(P_perc)
		if P_perc in P_list:
			P = int(P_perc)/100 # Приводим к значению 0.P_perc (нужно для выполнения формулы расчеты)
			lmbd = scipy.stats.t.ppf ((1 + P)/2, 999 - 1)
			print(Style.RESET_ALL + "Квантиль при P = " + Fore.GREEN + Style.BRIGHT + str(P_perc) + Style.RESET_ALL + " будет: " + Fore.GREEN + Style.BRIGHT + str(lmbd))
			break
		else:
			print(Fore.RED + Style.BRIGHT + "Значение доверительной вероятности должно быть в диапазоне от 1 до 99 %!")

# Функция проверки, является ли введенное значение неотрицательным числом и без символов
	def isnumeric (arg):
		try:
			if arg.isnumeric():
				return True
			elif not arg: # Проверяем введено ли значение вообще, иначе возвращает дефолтное значение
				return True
			elif float (arg): # Проверяем является ли это числом с плавающей точкой, т.к. как оказалось isnumeric() не пропускает такие числа.
				return True
		except:
			return False
# Ввод и условие для выбора значения СКО:
	while True:
		Upper_limit = Delta/3
		SKO = input("Введите СКО (0..." + str(Upper_limit) + ' (Delta/3)]: ' + Fore.YELLOW + Style.BRIGHT)
		if isnumeric (SKO) != True:
			print(Fore.RED + Style.BRIGHT + "Строка не должна содержать букв, +, -, ' ', и т.д.")
			continue
		elif not SKO: # Реализуем возврат дефолтного при отсутствии введенного значения
			SKO = Delta/3
			print(Style.RESET_ALL + "Если СКО не введено, то принимается как Delta/3: " + Fore.GREEN + Style.BRIGHT + str(SKO))
			break
		SKO = float(SKO)
		if SKO == 0:
			print(Fore.RED + Style.BRIGHT + "СКО не может быть равно 0")
			continue
		elif SKO > Delta/3:
			print(Fore.RED + Style.BRIGHT + "СКО не может быть больше 1/3 погрешности СИ (больше запаса по точности при поверке)")
			continue
		else:
			break

# Рассчитываем значения:

	time.sleep (0.75)
	print(Fore.CYAN + Style.BRIGHT + "\nРезультаты расчетов:")
	T1 = abs(Tn*(math.log((DeltaE/lmbd)*SKO)/math.log((Delta/SKO)+0.635)))
	T1_c = math.ceil (T1)
	print("T1 будет равно:", T1_c)
	T2 = abs(Tn*((DeltaE-(lmbd*SKO))/Delta))
	T2_c = math.ceil(T2)
	print("T2 будет равно:", T2_c)

# Проверяем условия:
	if T1 > T2:
		T = math.floor(T2/24/365)
		T_2 = math.floor(T2/24/30)
		time.sleep (0.75)
		if T == 1:
			print("\nМПИ: " + Fore.GREEN + Style.BRIGHT + str(T2_c) + Style.RESET_ALL +  " часов или " + Fore.GREEN + Style.BRIGHT + str(T) + Style.RESET_ALL + " год")
		elif T > 1 and T <= 4:
			print("\nМПИ: " + Fore.GREEN + Style.BRIGHT + str(T2_c) + Style.RESET_ALL +  " часов или " + Fore.GREEN + Style.BRIGHT + str(T) + Style.RESET_ALL + " года")
		elif T > 4:
			print("\nМПИ: " + Fore.GREEN + Style.BRIGHT + str(T2_c) + Style.RESET_ALL +  " часов или " + Fore.GREEN + Style.BRIGHT + str(T) + Style.RESET_ALL + " лет")
		else:
			print("\nМПИ: " + Fore.GREEN + Style.BRIGHT + str(T2_c) + Style.RESET_ALL +  " часов или " + Fore.GREEN + Style.BRIGHT + str(T_2) + Style.RESET_ALL + " мес")
	if T2 > T1:
		T = math.floor(T1/24/365)
		T_2 = math.floor(T1/24/30)
		time.sleep (0.75)
		if T == 1:
			print("\nМПИ: " + Fore.GREEN + Style.BRIGHT + str(T1_c) + Style.RESET_ALL +  " часов или " + Fore.GREEN + Style.BRIGHT + str(T) + Style.RESET_ALL + " год")
		elif T > 1 and T <= 4:
			print("\nМПИ: " + Fore.GREEN + Style.BRIGHT + str(T1_c) + Style.RESET_ALL +  " часов или " + Fore.GREEN + Style.BRIGHT + str(T) + Style.RESET_ALL + " года")
		elif T > 4:
			print("\nМПИ: " + Fore.GREEN + Style.BRIGHT + str(T1_c) + Style.RESET_ALL +  " часов или " + Fore.GREEN + Style.BRIGHT + str(T) + Style.RESET_ALL + " лет")
		else:
			print("\nМПИ: " + Fore.GREEN + Style.BRIGHT + str(T1_c) + Style.RESET_ALL +  " часов или " + Fore.GREEN + Style.BRIGHT + str(T_2) + Style.RESET_ALL + " мес")
	
iteration ()
while True:
	flag = input(Fore.MAGENTA + "\nНажмите Enter для повтора расчетов") 
	if not flag:
		iteration()
	else:
		break