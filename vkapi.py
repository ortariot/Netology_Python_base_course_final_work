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
        return req.json()

    

if __name__ == '__main__':
    pass
                
