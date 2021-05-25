import requests
from pprint import pprint


class VkClient():

    def __init__(self, token):
        self.access_token = token

    def get_photos(self, owner_id, album_id, extended=1, version=5.52):
        parametrs ={
        'access_token' :  self.access_token,
        'owner_id' : owner_id,
        'album_id' : album_id,
        'extended' : extended,
        'v' : version
        }
        url = 'https://api.vk.com/method/photos.get'
        req = requests.get(url, params=parametrs)
        return req.json()['response']['items']
    

if __name__ == '__main__':
    test_token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
    id = ''
    album_id = 'wall'
    vk_user = VkClient(test_token)
    items = vk_user.get_photos(id, album_id)
                
    pprint(vk_user.get_photos(id, album_id))
