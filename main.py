# class API VK
# class YaDrive
# class gui - QT ? (status bar, VK id, VK token, YaDrive token)
# class logger

# class Logger():

#     def __init__(self):
#         self.status_code = {
#             '01' : 'Connection',
#             '02' : 'Autentifaction',
#             '03' : 'Downloading from server',
#             '04' : 'Uploading to cloud'
#         }
#         self.process_code = {
#             '01' : 'stating',
#             '02' : 'in process',
#             '03' : 'is finish',
#             '04' : 'is falled',
#             '05' : 'is canceled'          
#         }


import datetime
import requests 
from pprint import pprint
from yadrive import YaDrive

token = ''
disck = YaDrive(token, '/test_app/')


test_token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
parametrs ={
    'access_token' : test_token,
    'owner_id' : '1388348',
    'album_id' : 'profile',
    'extended' : 1

}
# url = 'https://api.vk.com/method/users.get?user_id=210700286&v=5.52'
# photos.get
purl = 'https://api.vk.com/method/photos.get?user_id=210700286&v=5.52'

req = requests.get(purl, params=parametrs)
# pprint(req.json())

photo_base = req.json()['response']['items']
for entry in photo_base:
  
    date = datetime.datetime.utcfromtimestamp(entry['date']).strftime('%Y-%m-%d %H:%M:%S')
    print(date)
    disck.upload_from_url(entry['photo_2560'],f"{entry['likes']['count']}" + '.jpg')

