# Библиотеки
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as mb
import pickle
import os.path
#Переменные
login = ''
password = ''
cost_pick_1 = 15
cost_pick_2 = 500
cost_pick_3 = 3500
cost_pick_4 = 10000
cost_worker_1 = 100
cost_worker_2 = 2500
cost_worker_3 = 10000
cost_worker_4 = 30000
size_gold_click = 1
size_gold_real = 1
size_gold = 1
size_gold_dps = 0
a = True

#Игра
def game():
	global login,password,cost_pick_1,cost_pick_2,cost_pick_3,cost_pick_4,cost_worker_1,cost_worker_2,cost_worker_3,cost_worker_4,size_gold_click,size_gold_real,size_gold,size_gold_dps,a
	# Функции
	def exit_game():
		global login,password,cost_pick_1,cost_pick_2,cost_pick_3,cost_pick_4,cost_worker_1,cost_worker_2,cost_worker_3,cost_worker_4,size_gold_click,size_gold_real,size_gold,size_gold_dps,a
		answer = mb.askyesno(title = 'Сохранение.', message = 'Сохранить игру ?')
		if answer and login == '':
			def tu():
				login = e_login.get()
				password = e_password.get()
				if login != '' and password != '' and not(os.path.exists('saves/save_{}.txt'.format(login))):
					f = open('saves/save_{}.txt'.format(login), 'wb')
					login_password = {'login': login, 'password': password}
					pickle.dump(login_password, f)
					f.close()
					f = open('saves/game_{}.txt'.format(login), 'wb')
					game_m = {'cost_pick_1': cost_pick_1,
					'cost_pick_2': cost_pick_2,
					'cost_pick_3': cost_pick_3,
					'cost_pick_4': cost_pick_4,
					'cost_worker_1' : cost_worker_1,
					'cost_worker_2' : cost_worker_2,
					'cost_worker_3' : cost_worker_3,
					'cost_worker_4' : cost_worker_4,
					'size_gold_click' : size_gold_click,
					'size_gold_real' : size_gold_real,
					'size_gold' : size_gold_real,
					'size_gold_dps' : size_gold_dps,
					'a' : a}
					pickle.dump(game_m, f)
					f.close()
					mb.showinfo('Сохранение.', 'Ваши данные и результат были сохранены успешно.')
					root_save.destroy()
				elif not(os.path.exists('saves/save_{}.txt'.format(login))):
					mb.showerror('Ошибка.', 'Логин или пароль не может быть пустой.')
				else:
					mb.showerror('Ошибка.', 'Данный логин занят.')
			root.destroy()
			root_save = Tk()
			root_save.geometry('450x150')
			root_save.title('Регистрация.')
			lbl_avtoriz_login = Label(root_save, text = ' Логин : ', font = 'Arial 20')
			lbl_avtoriz_login.place(x = 15, y = 10)

			lbl_avtoriz_password = Label(root_save, text = 'Пароль: ', font = 'Arial 20')
			lbl_avtoriz_password.place(x = 10, y = 50)

			e_login = Entry(root_save, font = 20)
			e_password = Entry(root_save, font = 20)
			e_password.config(show="*")
			e_login.place(x = 130, y = 20)
			e_password.place(x = 130, y = 60)
			but_avtoriz_ok = Button(root_save, text = 'Потвердить', font = 'Arial 20', command = tu)
			but_avtoriz_ok.place(x = 160, y = 90)
			root_save.mainloop()
		elif answer and login != '':
			f = open('saves/game_{}.txt'.format(login), 'wb')
			game_m = {'cost_pick_1': cost_pick_1,
			'cost_pick_2': cost_pick_2,
			'cost_pick_3': cost_pick_3,
			'cost_pick_4': cost_pick_4,
			'cost_worker_1' : cost_worker_1,
			'cost_worker_2' : cost_worker_2,
			'cost_worker_3' : cost_worker_3,
			'cost_worker_4' : cost_worker_4,
			'size_gold_click' : size_gold_click,
			'size_gold_real' : size_gold_real,
			'size_gold' : size_gold_real,
			'size_gold_dps' : size_gold_dps,
			'a' : a}
			pickle.dump(game_m, f)
			root.destroy()
		elif not(answer):
			root.destroy()
	def pr_cost_pick_worker():
		global size_gold_real, size_gold_click, cost_pick_1, cost_pick_2, cost_pick_3, cost_pick_4, cost_worker_1, cost_worker_2, cost_worker_3, cost_worker_4
		if size_gold_real >= gstr(cost_pick_1):
			lbl_shop_gold_pick_1.configure(image = img_shop_gold_pick_1)
			lbl_shop_pick_1.configure(bg = '#007be9')
		else:
			lbl_shop_gold_pick_1.configure(image = img_shop_gold_pick_1_off)
			lbl_shop_pick_1.configure(bg = '#004284')
		if size_gold_real >= gstr(cost_pick_2):
			lbl_shop_gold_pick_2.configure(image = img_shop_gold_pick_2)
			lbl_shop_pick_2.configure(bg = '#007be9')
		else:
			lbl_shop_gold_pick_2.configure(image = img_shop_gold_pick_2_off)
			lbl_shop_pick_2.configure(bg = '#004284')
		if size_gold_real >= gstr(cost_pick_3):
			lbl_shop_gold_pick_3.configure(image = img_shop_gold_pick_3)
			lbl_shop_pick_3.configure(bg = '#007be9')
		else:
			lbl_shop_gold_pick_3.configure(image = img_shop_gold_pick_3_off)
			lbl_shop_pick_3.configure(bg = '#004284')
		if size_gold_real >= gstr(cost_pick_4):
			lbl_shop_gold_pick_4.configure(image = img_shop_gold_pick_4)
			lbl_shop_pick_4.configure(bg = '#007be9')
		else:
			lbl_shop_gold_pick_4.configure(image = img_shop_gold_pick_4_off)
			lbl_shop_pick_4.configure(bg = '#004284')
		if size_gold_real >= gstr(cost_worker_1):
			lbl_shop_gold_worker_1.configure(image = img_shop_gold_worker_1)
			lbl_shop_worker_1.configure(bg = '#e7b200')
		else:
			lbl_shop_gold_worker_1.configure(image = img_shop_gold_worker_1_off)
			lbl_shop_worker_1.configure(bg = '#816500')
		if size_gold_real >= gstr(cost_worker_2):
			lbl_shop_gold_worker_2.configure(image = img_shop_gold_worker_2)
			lbl_shop_worker_2.configure(bg = '#e7b200')
		else:
			lbl_shop_gold_worker_2.configure(image = img_shop_gold_worker_2_off)
			lbl_shop_worker_2.configure(bg = '#816500')
		if size_gold_real >= gstr(cost_worker_3):
			lbl_shop_gold_worker_3.configure(image = img_shop_gold_worker_3)
			lbl_shop_worker_3.configure(bg = '#e7b200')
		else:
			lbl_shop_gold_worker_3.configure(image = img_shop_gold_worker_3_off)
			lbl_shop_worker_3.configure(bg = '#816500')
		if size_gold_real >= gstr(cost_worker_4):
			lbl_shop_gold_worker_4.configure(image = img_shop_gold_worker_4)
			lbl_shop_worker_4.configure(bg = '#e7b200')
		else:
			lbl_shop_gold_worker_4.configure(image = img_shop_gold_worker_4_off)
			lbl_shop_worker_4.configure(bg = '#816500')
	def dps():
		global size_gold, size_gold_real, size_gold_dps, a
		size_gold = gint(size_gold_real)
		lbl_size_gold.configure(text = '{}'.format(size_gold))
		lbl_shop_gold_size_int.configure(text = '{}'.format(size_gold))
		pr_cost_pick_worker()
		if size_gold_dps != 0 and size_gold_dps <= 100:
			root.after(int(1000/size_gold_dps), dps)
			size_gold_real += 1
			a = False
		elif size_gold_dps > 100:
			root.after(50, dps)
			size_gold_real += size_gold_dps/50
	def gstr(x):
		try:
			if x[-1] == 'K':
				return float(x[:len(x)-1]) * 10**3
			if x[-1] == 'M':
				return float(x[:len(x)-1]) * 10**6
		except:
			return x
	def gint(x):
		if x >= 10**3 and x < 10**6:
			x = str((x//100)/10) + 'K'
			return x
		if x >=10**6 and x < 10**9:
			x = str((x//(10**5))/10) + 'M'
			return x
		else:
			return int(x)
	def open_fullscreen(event = '<Button-1>'):
		root.attributes('-fullscreen', True)
		but_exit_fs.place(x = 0, y = 0)
		but_open_fs.place_forget()
	def exit_fullscreen(event = '<Button-1>'):
		root.attributes('-fullscreen', False)
		but_exit_fs.place_forget()
		but_open_fs.place(x = 0, y = 0)
	def click(event):
		global size_gold_real, size_gold, size_gold_click
		size_gold_real += size_gold_click
		size_gold = gint(size_gold_real)
		lbl_size_gold.configure(text = '{}'.format(size_gold))
	def shop():
		fr_game_mine.pack_forget()
		fr_game_shop_gold.pack()
		pick()
	def pick():
		global size_gold_real, size_gold_click, cost_pick_1, cost_pick_2, cost_pick_3, cost_pick_4
		if size_gold_real >= gstr(cost_pick_1):
			lbl_shop_gold_pick_1.configure(image = img_shop_gold_pick_1)
			lbl_shop_pick_1.configure(bg = '#007be9')
		else:
			lbl_shop_gold_pick_1.configure(image = img_shop_gold_pick_1_off)
			lbl_shop_pick_1.configure(bg = '#004284')
		if size_gold_real >= gstr(cost_pick_2):
			lbl_shop_gold_pick_2.configure(image = img_shop_gold_pick_2)
			lbl_shop_pick_2.configure(bg = '#007be9')
		else:
			lbl_shop_gold_pick_2.configure(image = img_shop_gold_pick_2_off)
			lbl_shop_pick_2.configure(bg = '#004284')
		if size_gold_real >= gstr(cost_pick_3):
			lbl_shop_gold_pick_3.configure(image = img_shop_gold_pick_3)
			lbl_shop_pick_3.configure(bg = '#007be9')
		else:
			lbl_shop_gold_pick_3.configure(image = img_shop_gold_pick_3_off)
			lbl_shop_pick_3.configure(bg = '#004284')
		if size_gold_real >= gstr(cost_pick_4):
			lbl_shop_gold_pick_4.configure(image = img_shop_gold_pick_4)
			lbl_shop_pick_4.configure(bg = '#007be9')
		else:
			lbl_shop_gold_pick_4.configure(image = img_shop_gold_pick_4_off)
			lbl_shop_pick_4.configure(bg = '#004284')
		but_shop_gold_pick['state'] = 'disabled'
		but_shop_gold_worker['state'] = 'normal'
		lbl_shop_gold_pick_1.place(x = int(0.05*w), y = int(0.33*h))
		lbl_shop_gold_pick_2.place(x = int(0.05*w), y = int(0.33*h) + int(0.15*h))
		lbl_shop_gold_pick_3.place(x = int(0.05*w), y = int(0.33*h) + int(0.15*h)*2)
		lbl_shop_gold_pick_4.place(x = int(0.05*w), y = int(0.33*h) + int(0.15*h)*3)
		lbl_shop_pick_1.place(x = int(0.38*w), y = int(0.54 * h) - int(0.15*h))
		lbl_shop_pick_2.place(x = int(0.38*w), y = int(0.54 * h))
		lbl_shop_pick_3.place(x = int(0.38*w), y = int(0.54 * h) + int(0.15*h))
		lbl_shop_pick_4.place(x = int(0.38*w), y = int(0.54 * h) + int(0.15*h)*2)
		lbl_shop_gold_worker_1.place_forget()
		lbl_shop_gold_worker_2.place_forget()
		lbl_shop_gold_worker_3.place_forget()
		lbl_shop_gold_worker_4.place_forget()
		lbl_shop_worker_1.place_forget()
		lbl_shop_worker_2.place_forget()
		lbl_shop_worker_3.place_forget()
		lbl_shop_worker_4.place_forget()
		lbl_shop_gold_size_int.configure(text = '{}'.format(size_gold))
	def worker():
		global size_gold_real, cost_worker_1, cost_worker_2, cost_worker_3, cost_worker_4
		if size_gold_real >= gstr(cost_worker_1):
			lbl_shop_gold_worker_1.configure(image = img_shop_gold_worker_1)
			lbl_shop_worker_1.configure(bg = '#e7b200')
		else:
			lbl_shop_gold_worker_1.configure(image = img_shop_gold_worker_1_off)
			lbl_shop_worker_1.configure(bg = '#816500')
		if size_gold_real >= gstr(cost_worker_2):
			lbl_shop_gold_worker_2.configure(image = img_shop_gold_worker_2)
			lbl_shop_worker_2.configure(bg = '#e7b200')
		else:
			lbl_shop_gold_worker_2.configure(image = img_shop_gold_worker_2_off)
			lbl_shop_worker_2.configure(bg = '#816500')
		if size_gold_real >= gstr(cost_worker_3):
			lbl_shop_gold_worker_3.configure(image = img_shop_gold_worker_3)
			lbl_shop_worker_3.configure(bg = '#e7b200')
		else:
			lbl_shop_gold_worker_3.configure(image = img_shop_gold_worker_3_off)
			lbl_shop_worker_3.configure(bg = '#816500')
		if size_gold_real >= gstr(cost_worker_4):
			lbl_shop_gold_worker_4.configure(image = img_shop_gold_worker_4)
			lbl_shop_worker_4.configure(bg = '#e7b200')
		else:
			lbl_shop_gold_worker_4.configure(image = img_shop_gold_worker_4_off)
			lbl_shop_worker_4.configure(bg = '#816500')
		but_shop_gold_pick['state'] = 'normal'
		but_shop_gold_worker['state'] = 'disabled'
		lbl_shop_gold_pick_1.place_forget()
		lbl_shop_gold_pick_2.place_forget()
		lbl_shop_gold_pick_3.place_forget()
		lbl_shop_gold_pick_4.place_forget()
		lbl_shop_pick_1.place_forget()
		lbl_shop_pick_2.place_forget()
		lbl_shop_pick_3.place_forget()
		lbl_shop_pick_4.place_forget()
		lbl_shop_gold_worker_1.place(x = int(0.05*w), y = int(0.33*h))
		lbl_shop_gold_worker_2.place(x = int(0.05*w), y = int(0.33*h) + int(0.15*h))
		lbl_shop_gold_worker_3.place(x = int(0.05*w), y = int(0.33*h) + int(0.15*h)*2)
		lbl_shop_gold_worker_4.place(x = int(0.05*w), y = int(0.33*h) + int(0.15*h)*3)
		lbl_shop_worker_1.place(x = int(0.38*w), y = int(0.54 * h) - int(0.15*h))
		lbl_shop_worker_2.place(x = int(0.38*w), y = int(0.54 * h))
		lbl_shop_worker_3.place(x = int(0.38*w), y = int(0.54 * h) + int(0.15*h))
		lbl_shop_worker_4.place(x = int(0.38*w), y = int(0.54 * h) + int(0.15*h)*2)
		lbl_shop_gold_size_int.configure(text = '{}'.format(size_gold))
	def exit_shop_gold():
		global size_gold, size_gold_click
		fr_game_mine.pack()
		fr_game_shop_gold.pack_forget()
		size_gold = gint(size_gold_real)
		lbl_size_gold.configure(text = '{}'.format(size_gold))
		lbl_mine_size_click.configure(text = 'Золота за 1 клик: {}'.format(gint(size_gold_click)))
		lbl_mine_size_dps.configure(text = 'Золота в секунду: {}'.format(gint(size_gold_dps)))
	def pick_1(event):
		global size_gold_real, cost_pick_1, size_gold_click, size_gold
		if size_gold_real >= cost_pick_1:
			size_gold_real -= cost_pick_1
			cost_pick_1 *= 1.15
			cost_pick_1 //= 1
			size_gold_click += 1
			size_gold = gint(size_gold_real)
			lbl_shop_gold_size_click.configure(text = 'Золота за 1 клик: {}'.format(gint(size_gold_click)))
			lbl_shop_gold_size_int.configure(text = '{}'.format(size_gold))
			lbl_shop_pick_1.configure(text = '{}'.format(gint(cost_pick_1)))
		pick()
	def pick_2(event):
		global size_gold_real, cost_pick_2, size_gold_click, size_gold
		if size_gold_real >= cost_pick_2:
			size_gold_real -= cost_pick_2
			cost_pick_2 *= 1.15
			cost_pick_2 //= 1
			size_gold_click += 10
			size_gold = gint(size_gold_real)
			lbl_shop_gold_size_click.configure(text = 'Золота за 1 клик: {}'.format(gint(size_gold_click)))
			lbl_shop_gold_size_int.configure(text = '{}'.format(size_gold))
			lbl_shop_pick_2.configure(text = '{}'.format(gint(cost_pick_2)))
		pick()
	def pick_3(event):
		global size_gold_real, cost_pick_3, size_gold_click, size_gold
		if size_gold_real >= cost_pick_3:
			size_gold_real -= cost_pick_3
			cost_pick_3 *= 1.15
			cost_pick_3 //= 1
			size_gold_click += 25
			size_gold = gint(size_gold_real)
			lbl_shop_gold_size_click.configure(text = 'Золота за 1 клик: {}'.format(gint(size_gold_click)))
			lbl_shop_gold_size_int.configure(text = '{}'.format(size_gold))
			lbl_shop_pick_3.configure(text = '{}'.format(gint(cost_pick_3)))
		pick()
	def pick_4(event):
		global size_gold_real, cost_pick_4, size_gold_click, size_gold
		if size_gold_real >= cost_pick_4:
			size_gold_real -= cost_pick_4
			cost_pick_4 *= 1.15
			cost_pick_4 //= 1
			size_gold_click += 50
			size_gold = gint(size_gold_real)
			lbl_shop_gold_size_click.configure(text = 'Золота за 1 клик: {}'.format(gint(size_gold_click)))
			lbl_shop_gold_size_int.configure(text = '{}'.format(size_gold))
			lbl_shop_pick_4.configure(text = '{}'.format(gint(cost_pick_4)))
		pick()
	def worker_1(event):
		global size_gold_real, cost_worker_1, size_gold_dps, size_gold
		if size_gold_real >= cost_worker_1:
			size_gold_real -= cost_worker_1
			cost_worker_1 *= 1.15
			cost_worker_1 //= 1
			size_gold_dps += 1
			size_gold = gint(size_gold_real)
			lbl_shop_gold_size_dps.configure(text = 'Золота в секунду: {}'.format(gint(size_gold_dps)))
			lbl_shop_gold_size_int.configure(text = '{}'.format(size_gold))
			lbl_shop_worker_1.configure(text = '{}'.format(gint(cost_worker_1)))
			if a == True:
				dps()
		worker()
	def worker_2(event):
		global size_gold_real, cost_worker_2, size_gold_dps, size_gold
		if size_gold_real >= cost_worker_2:
			size_gold_real -= cost_worker_2
			cost_worker_2 *= 1.15
			cost_worker_2 //= 1
			size_gold_dps += 10
			size_gold = gint(size_gold_real)
			lbl_shop_gold_size_dps.configure(text = 'Золота в секунду: {}'.format(gint(size_gold_dps)))
			lbl_shop_gold_size_int.configure(text = '{}'.format(size_gold))
			lbl_shop_worker_2.configure(text = '{}'.format(gint(cost_worker_2)))
			if a == True:
				dps()
		worker()
	def worker_3(event):
		global size_gold_real, cost_worker_3, size_gold_dps, size_gold
		if size_gold_real >= cost_worker_3:
			size_gold_real -= cost_worker_3
			cost_worker_3 *= 1.15
			cost_worker_3 //= 1
			size_gold_dps += 25
			size_gold = gint(size_gold_real)
			lbl_shop_gold_size_dps.configure(text = 'Золота в секунду: {}'.format(gint(size_gold_dps)))
			lbl_shop_gold_size_int.configure(text = '{}'.format(size_gold))
			lbl_shop_worker_3.configure(text = '{}'.format(gint(cost_worker_3)))
			if a == True:
				dps()
		worker()
	def worker_4(event):
		global size_gold_real, cost_worker_4, size_gold_dps, size_gold
		if size_gold_real >= cost_worker_4:
			size_gold_real -= cost_worker_4
			cost_worker_4 *= 1.15
			cost_worker_4 //= 1
			size_gold_dps += 50
			size_gold = gint(size_gold_real)
			lbl_shop_gold_size_dps.configure(text = 'Золота в секунду: {}'.format(gint(size_gold_dps)))
			lbl_shop_gold_size_int.configure(text = '{}'.format(size_gold))
			lbl_shop_worker_4.configure(text = '{}'.format(gint(cost_worker_4)))
			if a == True:
				dps()
		worker()



	# Настройка корневого окна
	root = Tk()
	root.resizable(False, False)
	root['bg'] = '#ffb61b'
	w = root.winfo_screenwidth()
	h = root.winfo_screenheight()
	size = str(w)+'x'+str(h)
	root.geometry(size)
	root.attributes('-fullscreen', True)
	root.bind('<Escape>', exit_fullscreen)

	#dps для старого пользователя
	if a == False:
		root.after(int(1000/size_gold_dps), dps)
		size_gold_real += 1
		a = False

	# Создание игры.
	fr_game_mine = Frame(root, width = w, height = h, bg = '#ffb61b')

	# Создание шахты
	img_box = Image.open('images/box.png')
	img_box = img_box.resize((int(0.4*w),int(0.4*h)), Image.ANTIALIAS)
	img_photo_box = ImageTk.PhotoImage(img_box)
	lbl_mine = Label(fr_game_mine, image = img_photo_box, bg = '#ffb61b')
	lbl_mine.place(x = int(0.3*w), y = int(0.3*h))
	lbl_mine.bind('<Button-1>', click)

	# Отображение золота
	img_gold = Image.open('images/gold.png')
	img_gold = img_gold.resize((int(0.2*w),int(0.2*h)), Image.ANTIALIAS)
	img_photo_gold = ImageTk.PhotoImage(img_gold)
	lbl_gold = Label(fr_game_mine, image = img_photo_gold, bg = '#ffb61b')
	lbl_gold.place(x = int(0.4*w), y = int(0.05*h))

	lbl_size_gold = Label(fr_game_mine, text = '{}'.format(size_gold), font = 'Arial 25', fg = 'yellow', bg = '#850E02')
	lbl_size_gold.place(x = int(0.51*w),y = int(0.135*h))

	#Созданеи кнопки магазина шахты
	img_shop_gold = Image.open('images/shop.png')
	img_shop_gold = img_shop_gold.resize((int(0.1*w),int(0.1*w)), Image.ANTIALIAS)
	img_shop_gold = ImageTk.PhotoImage(img_shop_gold)
	but_shop_gold = Button(fr_game_mine, command = shop, image = img_shop_gold, activebackground = '#ffb61b', bg = '#ffb61b', relief = 'flat')
	but_shop_gold.place(x = 0, y = int((1-0.1*w/h)*h))
	fr_game_mine.pack()

	#Создание магазина шахты
	fr_game_shop_gold = Frame(root, width = w, height = h, bg = '#ffb61b')

	img_shop_gold_pick = Image.open('images/pick.png')
	img_shop_gold_pick = img_shop_gold_pick.resize((int(0.25*w),int(0.25*h)), Image.ANTIALIAS)
	img_shop_gold_pick = ImageTk.PhotoImage(img_shop_gold_pick)
	but_shop_gold_pick = Button(fr_game_shop_gold, command = pick, image = img_shop_gold_pick, activebackground = '#ffb61b', bg = '#ffb61b', relief = 'groove')
	but_shop_gold_pick.place(x = (0.05*w), y = int(0.05*h))

	img_shop_gold_worker = Image.open('images/workers.png')
	img_shop_gold_worker = img_shop_gold_worker.resize((int(0.25*w),int(0.25*h)), Image.ANTIALIAS)
	img_shop_gold_worker = ImageTk.PhotoImage(img_shop_gold_worker)
	but_shop_gold_worker = Button(fr_game_shop_gold, command = worker, image = img_shop_gold_worker, activebackground = '#ffb61b', bg = '#ffb61b', relief = 'groove')
	but_shop_gold_worker.place(x = int(0.3*w), y = int(0.05*h))

	img_shop_gold_exit = Image.open('images/exit_shop_gold.png')
	img_shop_gold_exit = img_shop_gold_exit.resize((int(0.1*w),int(0.1*h)), Image.ANTIALIAS)
	img_shop_gold_exit = ImageTk.PhotoImage(img_shop_gold_exit)
	but_shop_gold_exit = Button(fr_game_shop_gold, command = exit_shop_gold, image = img_shop_gold_exit, activebackground = '#ffb61b', bg = '#ffb61b', relief = 'flat')
	but_shop_gold_exit.place(x = int(0.9*w), y = 0)
	#Новый дизайн
	img_shop_gold_pick_1 = Image.open('images/button_pick_1_on.png')
	img_shop_gold_pick_1 = img_shop_gold_pick_1.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_pick_1 = ImageTk.PhotoImage(img_shop_gold_pick_1)

	img_shop_gold_pick_1_off = Image.open('images/button_pick_1_off.png')
	img_shop_gold_pick_1_off = img_shop_gold_pick_1_off.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_pick_1_off = ImageTk.PhotoImage(img_shop_gold_pick_1_off)

	img_shop_gold_pick_2 = Image.open('images/button_pick_2_on.png')
	img_shop_gold_pick_2 = img_shop_gold_pick_2.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_pick_2 = ImageTk.PhotoImage(img_shop_gold_pick_2)

	img_shop_gold_pick_2_off = Image.open('images/button_pick_2_off.png')
	img_shop_gold_pick_2_off = img_shop_gold_pick_2_off.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_pick_2_off = ImageTk.PhotoImage(img_shop_gold_pick_2_off)

	img_shop_gold_pick_3 = Image.open('images/button_pick_3_on.png')
	img_shop_gold_pick_3 = img_shop_gold_pick_3.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_pick_3 = ImageTk.PhotoImage(img_shop_gold_pick_3)

	img_shop_gold_pick_3_off = Image.open('images/button_pick_3_off.png')
	img_shop_gold_pick_3_off = img_shop_gold_pick_3_off.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_pick_3_off = ImageTk.PhotoImage(img_shop_gold_pick_3_off)

	img_shop_gold_pick_4 = Image.open('images/button_pick_4_on.png')
	img_shop_gold_pick_4 = img_shop_gold_pick_4.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_pick_4 = ImageTk.PhotoImage(img_shop_gold_pick_4)

	img_shop_gold_pick_4_off = Image.open('images/button_pick_4_off.png')
	img_shop_gold_pick_4_off = img_shop_gold_pick_4_off.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_pick_4_off = ImageTk.PhotoImage(img_shop_gold_pick_4_off)

	lbl_shop_gold_pick_1 = Label(fr_game_shop_gold, image = img_shop_gold_pick_1, borderwidth =0)
	lbl_shop_gold_pick_1.bind('<Button-1>', pick_1)

	img_shop_gold_pick_2 = Image.open('images/button_pick_2_on.png')
	img_shop_gold_pick_2 = img_shop_gold_pick_2.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_pick_2 = ImageTk.PhotoImage(img_shop_gold_pick_2)
	lbl_shop_gold_pick_2 = Label(fr_game_shop_gold, image = img_shop_gold_pick_2, borderwidth =0)
	lbl_shop_gold_pick_2.bind('<Button-1>', pick_2)

	img_shop_gold_pick_3 = Image.open('images/button_pick_3_on.png')
	img_shop_gold_pick_3 = img_shop_gold_pick_3.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_pick_3 = ImageTk.PhotoImage(img_shop_gold_pick_3)
	lbl_shop_gold_pick_3 = Label(fr_game_shop_gold, image = img_shop_gold_pick_3, borderwidth =0)
	lbl_shop_gold_pick_3.bind('<Button-1>', pick_3)

	img_shop_gold_pick_4 = Image.open('images/button_pick_4_on.png')
	img_shop_gold_pick_4 = img_shop_gold_pick_4.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_pick_4 = ImageTk.PhotoImage(img_shop_gold_pick_4)
	lbl_shop_gold_pick_4 = Label(fr_game_shop_gold, image = img_shop_gold_pick_4, borderwidth =0)
	lbl_shop_gold_pick_4.bind('<Button-1>', pick_4)

	lbl_shop_pick_1 = Label(fr_game_shop_gold, text = '{}'.format(gint(cost_pick_1)), font = 'Arial 25', bg = '#007be9', fg = '#e87223')
	lbl_shop_pick_1.place(x = int(0.38*w), y = int(0.54 * h) - int(0.15*h))
	lbl_shop_pick_2 = Label(fr_game_shop_gold, text = '{}'.format(gint(cost_pick_2)), font = 'Arial 25', bg = '#007be9', fg = '#e87223')
	lbl_shop_pick_2.place(x = int(0.38*w), y = int(0.54 * h))
	lbl_shop_pick_3 = Label(fr_game_shop_gold, text = '{}'.format(gint(cost_pick_3)), font = 'Arial 25', bg = '#007be9', fg = '#e87223')
	lbl_shop_pick_3.place(x = int(0.38*w), y = int(0.54 * h) + int(0.15*h))
	lbl_shop_pick_4 = Label(fr_game_shop_gold, text = '{}'.format(gint(cost_pick_4)), font = 'Arial 25', bg = '#007be9', fg = '#e87223')
	lbl_shop_pick_4.place(x = int(0.38*w), y = int(0.54 * h) + int(0.15*h)*2)

	lbl_shop_pick_1.bind('<Button-1>', pick_1)
	lbl_shop_pick_2.bind('<Button-1>', pick_2)
	lbl_shop_pick_3.bind('<Button-1>', pick_3)
	lbl_shop_pick_4.bind('<Button-1>', pick_4)

	img_shop_gold_worker_1 = Image.open('images/button_worker_1_on.png')
	img_shop_gold_worker_1 = img_shop_gold_worker_1.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_worker_1 = ImageTk.PhotoImage(img_shop_gold_worker_1)

	img_shop_gold_worker_1_off = Image.open('images/button_worker_1_off.png')
	img_shop_gold_worker_1_off = img_shop_gold_worker_1_off.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_worker_1_off = ImageTk.PhotoImage(img_shop_gold_worker_1_off)
	lbl_shop_gold_worker_1 = Label(fr_game_shop_gold, image = img_shop_gold_worker_1, borderwidth =0)
	lbl_shop_gold_worker_1.bind('<Button-1>', worker_1)
	lbl_shop_worker_1 = Label(fr_game_shop_gold, text = '{}'.format(gint(cost_worker_1)), font = 'Arial 25', bg = '#007be9', fg = '#e87223')

	img_shop_gold_worker_2 = Image.open('images/button_worker_2_on.png')
	img_shop_gold_worker_2 = img_shop_gold_worker_2.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_worker_2 = ImageTk.PhotoImage(img_shop_gold_worker_2)

	img_shop_gold_worker_2_off = Image.open('images/button_worker_2_off.png')
	img_shop_gold_worker_2_off = img_shop_gold_worker_2_off.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_worker_2_off = ImageTk.PhotoImage(img_shop_gold_worker_2_off)
	lbl_shop_gold_worker_2 = Label(fr_game_shop_gold, image = img_shop_gold_worker_2, borderwidth =0)
	lbl_shop_gold_worker_2.bind('<Button-1>', worker_2)
	lbl_shop_worker_2 = Label(fr_game_shop_gold, text = '{}'.format(gint(cost_worker_2)), font = 'Arial 25', bg = '#007be9', fg = '#e87223')

	img_shop_gold_worker_3 = Image.open('images/button_worker_3_on.png')
	img_shop_gold_worker_3 = img_shop_gold_worker_3.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_worker_3 = ImageTk.PhotoImage(img_shop_gold_worker_3)

	img_shop_gold_worker_3_off = Image.open('images/button_worker_3_off.png')
	img_shop_gold_worker_3_off = img_shop_gold_worker_3_off.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_worker_3_off = ImageTk.PhotoImage(img_shop_gold_worker_3_off)
	lbl_shop_gold_worker_3 = Label(fr_game_shop_gold, image = img_shop_gold_worker_3, borderwidth =0)
	lbl_shop_gold_worker_3.bind('<Button-1>', worker_3)
	lbl_shop_worker_3 = Label(fr_game_shop_gold, text = '{}'.format(gint(cost_worker_3)), font = 'Arial 25', bg = '#007be9', fg = '#e87223')

	img_shop_gold_worker_4 = Image.open('images/button_worker_4_on.png')
	img_shop_gold_worker_4 = img_shop_gold_worker_4.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_worker_4 = ImageTk.PhotoImage(img_shop_gold_worker_4)

	img_shop_gold_worker_4_off = Image.open('images/button_worker_4_off.png')
	img_shop_gold_worker_4_off = img_shop_gold_worker_4_off.resize((int(0.5*w)+5,int(0.15*h)), Image.ANTIALIAS)
	img_shop_gold_worker_4_off = ImageTk.PhotoImage(img_shop_gold_worker_4_off)
	lbl_shop_gold_worker_4 = Label(fr_game_shop_gold, image = img_shop_gold_worker_4, borderwidth =0)

	lbl_shop_gold_worker_1.bind('<Button-1>', worker_1)
	lbl_shop_worker_1 = Label(fr_game_shop_gold, text = '{}'.format(gint(cost_worker_1)), font = 'Arial 25', bg = '#e7b200', fg = '#007be9')
	lbl_shop_gold_worker_2.bind('<Button-1>', worker_2)
	lbl_shop_worker_2 = Label(fr_game_shop_gold, text = '{}'.format(gint(cost_worker_2)), font = 'Arial 25', bg = '#e7b200', fg = '#007be9')
	lbl_shop_gold_worker_3.bind('<Button-1>', worker_3)
	lbl_shop_worker_3 = Label(fr_game_shop_gold, text = '{}'.format(gint(cost_worker_3)), font = 'Arial 25', bg = '#e7b200', fg = '#007be9')
	lbl_shop_gold_worker_4.bind('<Button-1>', worker_4)
	lbl_shop_worker_4 = Label(fr_game_shop_gold, text = '{}'.format(gint(cost_worker_4)), font = 'Arial 25', bg = '#e7b200', fg = '#007be9')

	lbl_shop_worker_1.bind('<Button-1>', worker_1)
	lbl_shop_worker_2.bind('<Button-1>', worker_2)
	lbl_shop_worker_3.bind('<Button-1>', worker_3)
	lbl_shop_worker_4.bind('<Button-1>', worker_4)
	#Создание кнопки выхода из полноэкранного режима
	img_exit_fs = Image.open('images/exit_fs.png')
	img_exit_fs = img_exit_fs.resize((int(0.1*h),int(0.1*h)), Image.ANTIALIAS)
	img_exit_fs = ImageTk.PhotoImage(img_exit_fs)
	but_exit_fs = Button(fr_game_mine, command = exit_fullscreen, image = img_exit_fs, activebackground = '#ffb61b', bg = '#ffb61b', relief = 'groove')
	but_exit_fs.place(x = 0, y = 0)

	img_open_fs = Image.open('images/open_fs.png')
	img_open_fs = img_open_fs.resize((int(0.1*h),int(0.1*h)), Image.ANTIALIAS)
	img_open_fs = ImageTk.PhotoImage(img_open_fs)
	but_open_fs = Button(fr_game_mine, command = open_fullscreen, image = img_open_fs, activebackground = '#ffb61b', bg = '#ffb61b', relief = 'groove')

	#сила клика и dps отображение
	lbl_mine_size_click = Label(fr_game_mine, text = 'Золота за 1 клик: {}'.format(gint(size_gold_click)), font = 'Arial 20', bg = '#ffb61b',fg = '#1025ce')
	lbl_mine_size_click.place(x = int(0.3*w), y = int(0.71*h))
	lbl_mine_size_dps = Label(fr_game_mine, text = 'Золота в секунду: {}'.format(gint(size_gold_dps)), font = 'Arial 20', bg = '#ffb61b',fg = '#1025ce')
	lbl_mine_size_dps.place(x = int(0.3*w), y = int(0.75*h))

	lbl_shop_gold_size_click = Label(fr_game_shop_gold, text = 'Золота за 1 клик: {}'.format(gint(size_gold_click)), font = 'Arial 30', bg = '#ffb61b',fg = '#1025ce')
	lbl_shop_gold_size_click.place(x = int(0.61*w), y = int(0.02*h))
	lbl_shop_gold_size_dps = Label(fr_game_shop_gold, text = 'Золота в секунду: {}'.format(gint(size_gold_dps)), font = 'Arial 30', bg = '#ffb61b',fg = '#1025ce')
	lbl_shop_gold_size_dps.place(x = int(0.61*w), y = int(0.09*h))

	lbl_shop_gold_size = Label(fr_game_shop_gold, image = img_photo_gold, bg = '#ffb61b')
	lbl_shop_gold_size.place(x = int(0.61*w), y = int(0.15*h))
	lbl_shop_gold_size_int = Label(fr_game_shop_gold, text = '1', font = 'Arial 25', fg = 'yellow', bg = '#850E02')
	lbl_shop_gold_size_int.place(x = int(0.72*w), y = int(0.23*h))

	#Кнопка выхода из игры
	img_exit_game = Image.open('images/exit_game.png')
	img_exit_game = img_exit_game.resize((int(0.1*h),int(0.1*h)), Image.ANTIALIAS)
	img_exit_game = ImageTk.PhotoImage(img_exit_game)
	but_exit_game = Button(fr_game_mine, command = exit_game, image = img_exit_game, activebackground = '#ffb61b', bg = '#ffb61b', relief = 'groove')
	but_exit_game.place(x = w-0.1*h, y = 0)

	root.mainloop()

#Функции приветсвенного окна или функции до игры.
def f_1():
	def answer_1():
		fr_avtoriz.pack_forget()
		fr_answer_1.pack()
	def answer_2():
		global login,password,cost_pick_1,cost_pick_2,cost_pick_3,cost_pick_4,cost_worker_1,cost_worker_2,cost_worker_3,cost_worker_4,size_gold_click,size_gold_real,size_gold,size_gold_dps,a
		login = e_login.get()
		password = e_password.get()
		if login != '' and password != '' and os.path.exists('saves/save_{}.txt'.format(login)):
			f = open('saves/save_{}.txt'.format(login), 'rb')
			login_password = pickle.load(f)
			f.close()
			if login_password['password'] == password:
				root_answer_1.destroy()
				f = open('saves/game_{}.txt'.format(login), 'rb')
				game_m = pickle.load(f)
				login = login_password['login']
				password = login_password['password']
				cost_pick_1 = game_m['cost_pick_1']
				cost_pick_2 = game_m['cost_pick_2']
				cost_pick_3 = game_m['cost_pick_3']
				cost_pick_4 = game_m['cost_pick_4']
				cost_worker_1 = game_m['cost_worker_1']
				cost_worker_2 = game_m['cost_worker_2']
				cost_worker_3 = game_m['cost_worker_3']
				cost_worker_4 = game_m['cost_worker_4']
				size_gold_click = game_m['size_gold_click']
				size_gold_real = game_m['size_gold_real']
				size_gold = game_m['size_gold']
				size_gold_dps = game_m['size_gold_dps']
				a = game_m['a']
				game()
			else:
				mb.showerror('Ошибка.', 'Введен неверный пароль.')
		elif login == '' or password == '':
			mb.showerror('Ошибка.', 'Логин или пароль не может быть пустым.')
		else:
			mb.showerror('Ошибка.', 'Такого пользователя не существует')
	fr_answer_1.pack_forget()
	fr_avtoriz = Frame(root_answer_1, width = 450, height = 150)
	root_answer_1.title('Авторизация.')

	lbl_avtoriz_login = Label(fr_avtoriz, text = ' Логин : ', font = 'Arial 20')
	lbl_avtoriz_login.place(x = 15, y = 10)

	lbl_avtoriz_password = Label(fr_avtoriz, text = 'Пароль: ', font = 'Arial 20')
	lbl_avtoriz_password.place(x = 10, y = 50)

	e_login = Entry(fr_avtoriz, font = 20)
	e_password = Entry(fr_avtoriz, font = 20)
	e_password.config(show="*")
	e_login.place(x = 130, y = 20)
	e_password.place(x = 130, y = 60)

	but_avtoriz_exit = Button(fr_avtoriz, text = 'Назад', font = 'Arial 20', command = answer_1)
	but_avtoriz_ok = Button(fr_avtoriz, text = 'Потвердить', font = 'Arial 20', command = answer_2)
	but_avtoriz_exit.place(x = 10, y = 90)
	but_avtoriz_ok.place(x = 160, y = 90)
	fr_avtoriz.pack()
def f_2():
	root_answer_1.destroy()
	game()
#Приветсвенное окно
root_answer_1 = Tk()
root_answer_1.geometry('450x150')
root_answer_1.resizable(False, False)
root_answer_1.title('Приветсвенное окно.')

fr_answer_1 = Frame(root_answer_1, width = 450, height = 150)
lbl_answer_1 = Label(fr_answer_1, text = 'Выберите, что хотите сделать:', font = 'Arial 20')
lbl_answer_1.place(x = 25, y = 25)

but_continue = Button(fr_answer_1, text = 'Продолжить игру', font = 'Arial 18', command = f_1)
but_continue.place(x = 10, y = 70)

but_new_game = Button(fr_answer_1, text = 'Начать сначала', font = 'Arial 18', command = f_2)
but_new_game.place(x = 240, y = 70)
fr_answer_1.pack()
root_answer_1.mainloop()

