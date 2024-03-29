import vk_api
from time import sleep

# Авторизация
login, password = '', ''
vk_session = vk_api.VkApi(login, password)
vk_session.auth()
vk = vk_session.get_api()

def check_last_comment(post):
    lst = ''
    while not lst:
        lst = vk_session.method('wall.getComments',
                                {'owner_id': -193376219, 'post_id': post, 'count': 1, 'sort': 'desc', 'extended': 1})
    return lst['profiles'][0]['id'] != 353313939


def get_last_post_id():
    all_wall = (vk_session.method('wall.get', {'owner_id': -193376219, 'count': 2})).values()
    last_post_id = (list(list(all_wall)[1])[1])['id']
    return last_post_id

def check_like(post_id):
    a = vk_session.method('likes.isLiked',
                          {'user_id': 353313939, 'type': 'post', 'owner_id': -193376219, 'item_id': post_id})
    return a['liked']
