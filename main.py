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
import os
import json
from pprint import pprint
from yadrive import YaDrive
from vkapi import VkClient
import logging
import sys
from PyQt5 import QtWidgets
import design


class LogicalLair():

    
    def get_max_res(self, item):
        out = 0
        for sl in item:
            if 'photo' in sl:
                value = int(sl[6 :])
                if value > out:
                    out = value
        return f"photo_{out}"

    def get_status_data(self):
        folder_list = self.disck.get_files_list()
        if 'status.json' in folder_list:
            self.disck.download_from_cloud('status.json')
            with open('status.json') as f:
                files_data = json.load(f)  
            logging.info('Folder list obtained from clud')
        else:    
            files_data = {
            'last_update' : 0,
            'items' : []
            }
            logging.info('Creating new Folder list')
        return files_data


    def transport_from_vk_to_clud(self, vk_token, owner_id, album_id, clud_token, qty=None):
        logging.info('Start vk to cloud process')  
        vk_clien = VkClient(vk_token)
        logging.info('Connection to vk')
        photo_base = vk_clien.get_photos(owner_id, album_id)
        if 'response' in photo_base:
            logging.info(f'{len(photo_base)} photos found')
            logging.info('Connection to YaDrive')
            self.disck = YaDrive(clud_token, '/test_app2/')
            logging.info('Getting folder list')
            files_data = self.get_status_data()
            files_count = len(files_data['items'])
            tmp_photo_list = [file['file_name'] for file in files_data['items']]
            id_list = [file['id'] for file in files_data['items']]
            
            for entry in reversed(photo_base):
                if entry['id'] not in id_list:
                    photo_name = f"{entry['likes']['count']}" + '.jpg'
                    if photo_name in tmp_photo_list:
                        date = datetime.datetime.utcfromtimestamp(entry['date']).strftime('-%d-%m-%Y-%H-%M-%S')
                        photo_name = f"{entry['likes']['count']}" + date + '.jpg'       
                    tmp_photo_list.append(photo_name)
                    up_code = self.disck.upload_from_url(entry[self.get_max_res(entry)], photo_name)
                    logging.info(f'{photo_name} uploading to cloud')
                    if up_code == 200:
                        files_data['items'].append({"file_name": photo_name, "id" : entry['id'],  "size": f"{entry['height']} x {entry['width']} " })
                        if qty is not None and len(tmp_photo_list) - files_count == qty:
                            print(tmp_photo_list)
                            break
                else: 
                    logging.info('This files already been written to disk')
        

            files_data['last_update'] = int(time.time())
            logging.info('Uploading to cloud status file')
            with open('status.json', 'w', encoding='utf-8') as f:
                json.dump(files_data, f, indent=2)
            self.disck.upload_from_drive('status.json')
            logging.info('Uploading is sucsessfull')
        elif 'error' in photo_base:
            print(f"error - {photo_base['error']['error_msg']}")
        else:
            print('error - undefined error')



class WindowsForms(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.__preset()
        self.pushButton.clicked.connect(self.but_action)
        self.checkBox.clicked.connect(self.check_box_action)
        self.l_layуr = LogicalLair()
    
    # listWidget get items; fedault item == profile
    def __listWidget_get_item(self):
        if self.listWidget.selectedItems():
            if self.listWidget.selectedItems()[0] == self.listWidget.item(1):
                return self.listWidget.item(1).text()
            elif self.listWidget.selectedItems()[0] == self.listWidget.item(2):
                return self.listWidget.item(2).text()
            else:
                return self.listWidget.item(0).text()
        else:
            return self.listWidget.item(0).text()

    def __preset(self):
        dir_list = os.listdir()
        if 'settings.json' in dir_list:
            with open('settings.json', 'r', encoding='utf-8') as f:
                settings = json.load(f)
            self.textEdit.setText(settings['vk_token']) 
            self.textEdit_4.setText(settings['vk_id']) 
            self.textEdit_2.setText(settings['yd_token']) 
            self.textEdit_5.setText(settings['yd_path']) 
    
    def __set_settings(self, vk_token, vk_id, vk_album, yd_token, yd_path):
        settings = {
            'vk_token' : vk_token,
            'vk_id' : vk_id,
            'vk_album' : vk_album,
            'yd_token' : yd_token,
            'yd_path' : yd_path
        }
        with open('settings.json', 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=2)

    def but_action(self):
        vk_token = self.textEdit.toPlainText()
        vk_id = self.textEdit_4.toPlainText()
        vk_album = self.__listWidget_get_item()
        yd_token = self.textEdit_2.toPlainText()
        yd_path = self.textEdit_5.toPlainText()       
        self.__set_settings(vk_token, vk_id, vk_album, yd_token, yd_path)
    
        if self.checkBox.isChecked():
            numbe_of_photo = self.spinBox.value()
        else:
            numbe_of_photo = None

        # self.l_layуr.transport_from_vk_to_clud(vk_token, vk_id, vk_album, yd_token, numbe_of_photo)

        # print(numbe_of_photo)
        self.label_3.setText(vk_album)
        # print(self.listWidget.item(0))


    def check_box_action(self):
        if self.checkBox.isChecked():
            self.spinBox.setEnabled(True)
        else:
            self.spinBox.setEnabled(False)


def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = WindowsForms()  
    window.show()  
    app.exec_() 


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='log: %(name)s - %(message)s')
    test_token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
    ya_token = ''
    id = ''
    album_id = 'wall'
    ll = LogicalLair()
    ll.transport_from_vk_to_clud(test_token, id, album_id, ya_token, 10)


    # main()
