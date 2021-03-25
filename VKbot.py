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


def write_ls_msg(user_id, message):
	ls_vk.messages.send(user_id=user_id, message=message, random_id=get_random_id())


def create_empty_keyboard():
	keyboard = vk_api.keyboard.VkKeyboard.get_empty_keyboard()
	return keyboard


def key_start():
	keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
	keyboard.add_button("Узнать о процессе буста.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Заказать буст Faceit.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Заказать буст MM.", color=VkKeyboardColor.PRIMARY)
	return keyboard.get_keyboard()


def key_rank_mm():
	keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
	keyboard.add_button("Silver I", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Silver II", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Silver III.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Silver VI.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Silver Elite.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Silver Elite Master.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Gold Nova I.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Gold Nova II.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Gold Nova III.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Gold Nova Master.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Master Guardian I.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Master Guardian II.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Master Guardian Elite.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Distinguished master guardian.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Legendary eagle.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Legendary eagle master.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_button("Supreme master first class.", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("Назад.", color=VkKeyboardColor.NEGATIVE)
	return keyboard.get_keyboard()


def key_elo():
	keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
	keyboard.add_button("lvl 0.", color=VkKeyboardColor.PRIMARY)
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
	keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
	keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=203427725")
	return keyboard.get_keyboard()


def price_elo(have_elo, want_elo):
	return "Цена Faceit"


def price_mm(have_rang, want_rang):
	return "Цена ММ"


def write_ls_keyboard(event, message, keyboard):
	ls_vk.messages.send(user_id=event.user_id, random_id=get_random_id(), keyboard=keyboard, message=message)


def lvl_1():
	for event in ls_longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
			write_ls_keyboard(event, '''Привет, я бот BoostCsGo. Здесь вы можете заказать буст и
									узнать цены на услуги.''', key_start())
			if event.text == "Узнать о процессе буста.":
				write_ls_msg(event.user_id, "Текст с инфой.")
			if event.text == "Заказать буст Faceit." or "Заказать буст MM.":
				lvl_2()
				continue


def lvl_2():
	for event in ls_longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
			user_elo = "undefined"
			user_rank = "undefined"
			if event.text == "Заказать буст Faceit.":
				write_ls_keyboard(event, "Какой у тебя lvl Faceit ?", key_elo())
				if event.text == "Назад.":
					return
				elif event.text == "lvl 0.":
					check_answer = True
					user_elo = event.text
					lvl_3(check_answer, user_elo, user_rank)
					continue
			elif event.text == "Заказать буст MM.":
				write_ls_keyboard(event, "Какое у тебя звание ?", key_rank_mm())
				if event.text == "Назад.":
					return
				elif event.text != "Назад.":
					check_answer = False
					user_rank = event.text
					lvl_3(check_answer, user_elo, user_rank)
					continue


def lvl_3(check_answer, user_elo, user_rank):
	for event in ls_longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
			user_want_rank = "undefined"
			user_want_elo = "undefined"
			if check_answer:
				write_ls_keyboard(event, "Какой lvl ты хочешь ?", key_elo())
				if event.text == "Назад.":
					event.text = "Заказать буст Faceit."
					return
				user_want_elo = event.text
				lvl_4(check_answer, user_elo, user_rank, user_want_rank, user_want_elo)
			elif not check_answer:
				write_ls_keyboard(event, "Какое звание ты хочешь ?", key_rank_mm())
				if event.text == "Назад.":
					event.text = "Заказать буст MM."
					return
				user_want_rank = event.text
				lvl_4(check_answer, user_elo, user_rank, user_want_rank, user_want_elo)


def lvl_4(check_answer, user_elo, user_rank, user_want_rank, user_want_elo):
	for event in ls_longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
			if check_answer:
				write_ls_keyboard(event, "Стоимость буста: ", key_end())
				write_ls_msg(event.user_id, price_elo(user_elo, user_want_elo))
			elif not check_answer:
				write_ls_keyboard(event, "Стоимость буста: ", key_end())
				write_ls_msg(event.user_id, price_mm(user_rank, user_want_rank))
			if event.text == "Назад.":
				lvl_3(check_answer, user_elo, user_rank)
			if event.text == "Перейти к оплате.":
				lvl_5(check_answer, user_elo, user_rank, user_want_rank, user_want_elo)


def lvl_5(check_answer, user_elo, user_rank, user_want_rank, user_want_elo):
	for event in ls_longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
			write_ls_keyboard(event, "{Хз че тут писать.", key_payment())
			if event.text == "Назад.":
				lvl_4(check_answer, user_elo, user_rank, user_want_rank, user_want_elo)
			elif event.text == "Вернуться в начало.":
				lvl_1()


for event in ls_longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
		write_ls_keyboard(event, '''Привет, я бот BoostCsGo. Здесь вы можете заказать буст и
								узнать цены на услуги.''', key_start())
		if event.text == "Узнать о процессе буста.":
			write_ls_msg(event.user_id, "Текст с инфой.")
			continue
		if event.text == "Заказать буст Faceit." or "Заказать буст MM.":
			lvl_2()
			continue
		else:
			continue


