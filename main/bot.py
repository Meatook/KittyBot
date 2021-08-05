# -*- coding: utf-8 -*-
import vk_api, codecs, group_captcha_method as gcm, tr
import get_post_id as gpi
from time import sleep
from random import randint

# Авторизация
login, password = '', ''
vk_session = vk_api.VkApi(login, password)
vk_session.auth()
vk = vk_session.get_api()

# Загрзка файла и работа с ним
with codecs.open('ЕГ.txt', encoding='utf-8') as text:
    def get_liked(post_id):
        if not gpi.check_like(post_id):
            sleep(4)
            vk_session.method('likes.add',
                              {'user_id': , 'type': 'post', 'owner_id': , 'item_id': post_id})


    # Функция отправки коментария
    def send_comment(post, comment_text, group=):
            # Отправка при обычных условиях и при капче
        try:
            vk_session.method('wall.createComment', {'owner_id': group, 'post_id': post, 'message': comment_text, 'random_id': 0}, captcha_sid=None, captcha_key=None)
        except vk_api.exceptions.Captcha as err:
            print('Отправлен запрос на получение ключа от капчи.')
            key = gcm.send_captcha(err.get_url())
            print('Получен ключ:', key)

            # Обработка неверности ключа капчи
            try:
                vk_session.method('wall.createComment',
                                {'owner_id': group, 'post_id': post, 'message': comment_text, 'random_id': 0},
                                captcha_sid=((err.get_url().split('=')[1])[:-2]), captcha_key=key)
                print('Ключ успешно отправлен.\n' + '-'*100 + '\n')
#                gcm.send_message('Успешно.')
            except:
                print('Произошла ошибка при отправке капчи.\nПерезагрузка.')
#                gcm.send_message('Произошла ошибка при отправке капчи.\nПерезагрузка.')
    for _ in range(3):
        for i in text:
            # Нахождение последнего поста
            try:
                last_post_id = gpi.get_last_post_id()
            except:
                all_wall = (vk_session.method('wall.get', {'owner_id': , 'count': 2})).values()
                last_post_id = (list(list(all_wall)[1])[1])['id']

#            get_liked(last_post_id)
            k = i[::]

            if k.count(' ') < 5:
                k = i[::] + i[::] + i[::]
            try:
                x = gpi.check_last_comment(last_post_id)
                while not x:
                    x = gpi.check_last_comment(last_post_id)
            except:
                print('Не запустилась программа автолайка')

            send_comment(last_post_id, k)
            sleep(1 + (randint(1, 23) / 10))

gcm.send_message('Достигнут конец файла')
print('Достигнут конец файла')



