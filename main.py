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
import time
import json
from pprint import pprint
from yadrive import YaDrive
from vkapi import VkClient
import logging
import sys


def transport_from_vk_to_clud(vk_token, owner_id, album_id, clud_token):
    logging.info('Start vk to cloud process')  
    vk_clien = VkClient(vk_token)
    logging.info('Connection to vk')
    photo_base = vk_clien.get_photos(owner_id, album_id)
    logging.info(f'{len(photo_base)} photos found')
    # pprint(photo_base)
    logging.info('Connection to YaDrive')
    disck = YaDrive(clud_token, '/test_app/')
    logging.info('Getting folder list')
    folder_list = disck.get_files_list()
    if 'status.json' in folder_list:
        disck.download_from_cloud('status.json')
        with open('status.json') as f:
            files_data = json.load(f)  
        logging.info('Folder list obtained from clud')
    else:    
        files_data = {
        'last_update' : 0,
        'items' : []
        }
        logging.info('Creating new Folder list')

    for entry in reversed(photo_base):
        if entry['date'] > files_data['last_update']:
            photo_name = f"{entry['likes']['count']}" + '.jpg'
            if photo_name in folder_list:
                date = datetime.datetime.utcfromtimestamp(entry['date']).strftime('-%d-%m-%Y')
                photo_name = f"{entry['likes']['count']}" + date + '.jpg'       
            
            up_code = disck.upload_from_url(entry['photo_2560'], photo_name)
            logging.info(f'{photo_name} uploading to cloud')
            if up_code == 200:
                files_data['items'].append({"file_name": photo_name, "size": f"{entry['height']} x {entry['width']} " })
        else: 
            logging.info('Remaining files have already been written to disk')
            break

    files_data['last_update'] = int(time.time())
    logging.info('Uploading to cloud status file')
    with open('status.json', 'w', encoding='utf-8') as f:
        json.dump(files_data, f, indent=2)
    disck.upload_from_drive('status.json')
    logging.info('Uploading is sucsessfull')



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='log: %(name)s - %(message)s')
    test_token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
    ya_token = ''
    id = ''
    album_id = 'profile'
    transport_from_vk_to_clud(test_token, id, album_id, ya_token)
