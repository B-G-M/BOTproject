#! /usr/bin/env python37
# -*- coding: utf-8 -*-

import vk_api
import vk
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

token = '37a55873060ed384d376a08d921213e296fcfaa82afbe78b165c8042cddce28ddd0614b73d3fe777cb48d'
vk_session = vk_api.VkApi(token=token)
ls_longpoll = VkLongPoll(vk_session)
ls_vk = vk_session.get_api()


def write_ls_msg(event, message):
	ls_vk.messages.send(user_id=event.user_id, message=message, random_id=get_random_id())
	return


def key_start():
	keyboard = vk_api.keyboard.VkKeyboard(one_time=False)
	keyboard.add_button("Узнать о процессе буста.", color=VkKeyboardColor.SECONDARY)
	keyboard.add_line()
	keyboard.add_button("Заказать буст Faceit.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Заказать буст MM.", color=VkKeyboardColor.PRIMARY)
	return keyboard.get_keyboard()


def key_rank_mm():
	keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
	keyboard.add_button("Silver I.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Silver II.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Silver III.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Silver VI.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Silver Elite.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Silver Master.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Gold Nova I.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Gold Nova II.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Gold Nova III.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("G.Nova Master.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Guardian I.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Guardian II.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Guardian Elite.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Big Star.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Eagle.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Eagle master.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Supreme.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Global Elite.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Назад.", color=VkKeyboardColor.NEGATIVE)
	return keyboard.get_keyboard()


def key_elo():
	keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
	keyboard.add_button("lvl 1.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("lvl 2.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("lvl 3.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("lvl 4.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("lvl 5.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("lvl 6.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("lvl 7.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("lvl 8.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("lvl 9.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("lvl 10.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Назад.", color=VkKeyboardColor.NEGATIVE)
	return keyboard.get_keyboard()


def key_end():
	keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
	keyboard.add_button("Перейти к оплате.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Вернуться в начало.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Назад.", color=VkKeyboardColor.NEGATIVE)
	return keyboard.get_keyboard()


def key_payment():
	keyboard = vk_api.keyboard.VkKeyboard(one_time=False)
	keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=203427725")
	keyboard.add_line()
	keyboard.add_button("Вернуться в начало.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Назад.", color=VkKeyboardColor.NEGATIVE)
	return keyboard.get_keyboard()


def price_elo(have_elo, want_elo):
	tir = 0
	tir2 = 0
	if have_elo == "lvl 1." or have_elo == "lvl 2." or have_elo == "lvl 3.":
		tir = 1
	if have_elo == "lvl 4." or have_elo == "lvl 5." or have_elo == "lvl 6." or have_elo == "lvl 7.":
		tir = 2
	if have_elo == "lvl 8." or have_elo == "lvl 9.":
		tir = 3
	if have_elo == "lvl 10.":
		tir = 4
	if want_elo == "lvl 1." or want_elo == "lvl 2." or want_elo == "lvl 3.":
		tir2 = 1
	if want_elo == "lvl 4." or want_elo == "lvl 5." or want_elo == "lvl 6." or want_elo == "lvl 7.":
		tir2 = 2
	if want_elo == "lvl 8." or want_elo == "lvl 9.":
		tir2 = 3
	if want_elo == "lvl 10.":
		tir2 = 4
	if tir2-tir == 0:
		return "Цена буста - 250 рублей"
	if tir2-tir == 1:
		return "Цена буста - 500 рублей"
	if tir2-tir == 2:
		return "Цена буста 1000 рублей"
	if tir2-tir == 3:
		return "2000 рублей"


def price_mm(have_rang, want_rang):
	tir = 0
	tir2 = 0
	if have_rang == "Silver I." or have_rang == "Silver II." or have_rang == "Silver III." or have_rang == "Silver VI." \
		or have_rang == "Silver Elite." or have_rang == "Silver Master.":
		tir = 1
	if have_rang == "Gold Nova I." or have_rang == "Gold Nova II." or have_rang == "Gold Nova III." \
		or have_rang == "G.Nova Master.":
		tir = 2
	if have_rang == "Guardian I." or have_rang == "Guardian II." or have_rang == "Guardian Elite." \
		or have_rang == "Big Star.":
		tir = 3
	if have_rang == "Eagle." or have_rang == "Eagle master.":
		tir = 4
	if have_rang == "Supreme.":
		tir = 5
	if want_rang == "Silver I." or want_rang == "Silver II." or want_rang == "Silver III." or want_rang == "Silver VI." \
		or want_rang == "Silver Elite." or want_rang == "Silver Master.":
		tir2 = 1
	if want_rang == "Gold Nova I." or want_rang == "Gold Nova II." or want_rang == "Gold Nova III." \
		or want_rang == "G.Nova Master.":
		tir2 = 2
	if want_rang == "Guardian I." or want_rang == "Guardian II." or want_rang == "Guardian Elite." \
		or want_rang == "Big Star.":
		tir2 = 3
	if want_rang == "Eagle." or want_rang == "Eagle master.":
		tir2 = 4
	if want_rang == "Supreme." or want_rang == "Global Elite.":
		tir2 = 5
	if tir2 - tir == 0:
		return "Цена буста - 250 рублей"
	if tir2 - tir == 1:
		return "Цена буста - 450 рублей"
	if tir2 - tir == 2:
		return "Цена буста 750 рублей"
	if tir2 - tir == 3:
		return "Цена буста 1500 рублей"
	if tir2 - tir == 4:
		return "2000 рублей"


def write_ls_keyboard(event, message, keyboard):
	ls_vk.messages.send(user_id=event.user_id, random_id=get_random_id(), keyboard=keyboard, message=message)


def main():
	message = "undefined"
	user_elo = "undefined"
	user_rank = "undefined"
	user_want_rank = "undefined"
	user_want_elo = "undefined"
	check_answer = "undefined"
	case = -1
	while True:
		for event in ls_longpoll.listen():
			if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
				if event.text == "Назад.":
					if case != 0:
						case = case - 1
					else:
						event.text = "undefined"
				else:
					case = case + 1
					
				if user_elo == "Какой у тебя lvl Faceit ?":
					user_elo = event.text
				if user_rank == "Какое у тебя звание ?":
					user_rank = event.text
				if user_want_elo == "Какой lvl ты хочешь ?":
					user_want_elo = event.text
				if user_want_rank == "Какое звание ты хочешь ?":
					user_want_rank = event.text
					
				if event.text == "Вернуться в начало.":
					case = 0
					message = "undefined"
				if event.text == "Узнать о процессе буста.":
					case = 0
					write_ls_msg(event, "Буст происходит с передачей аккаунта бустеру. \
										Сроки выполнения услуги зависят от сложности заказа.")
				if case == 0:
					write_ls_keyboard(event, '''Привет, я бот BoostCsGo. Здесь вы можете заказать буст и
											узнать цены на услуги.''', key_start())
					if event.text == "Заказать буст Faceit." or "Заказать буст MM.":
						continue
				if case == 1:
					if event.text == "Заказать буст Faceit." or message == "Заказать буст Faceit.":
						write_ls_keyboard(event, "Какой у тебя lvl Faceit ?", key_elo())
						check_answer = True
						user_elo = "Какой у тебя lvl Faceit ?"
						continue
					elif event.text == "Заказать буст MM." or message == "Заказать буст MM.":
						write_ls_keyboard(event, "Какое у тебя звание ?", key_rank_mm())
						check_answer = False
						user_rank = "Какое у тебя звание ?"
						continue
				if case == 2:
					if check_answer:
						write_ls_keyboard(event, "Какой lvl ты хочешь ?", key_elo())
						user_want_elo = "Какой lvl ты хочешь ?"
						message = "Заказать буст Faceit."
						continue
					elif not check_answer:
						write_ls_keyboard(event, "Какое звание ты хочешь ?", key_rank_mm())
						user_want_rank = "Какое звание ты хочешь ?"
						message = "Заказать буст MM."
						continue
				if case == 3:
					if check_answer:
						write_ls_keyboard(event, "Стоимость буста: ", key_end())
						write_ls_msg(event, price_elo(user_elo, user_want_elo))
						continue
					elif not check_answer:
						write_ls_keyboard(event, "Стоимость буста: ", key_end())
						write_ls_msg(event, price_mm(user_rank, user_want_rank))
						continue
				if case == 4:
					write_ls_keyboard(event, "Можно приступить к оплате или вернуться \
											обратно в меню для выбора другой услуги.", key_payment())
					continue
					
					
main()
