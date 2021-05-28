import datetime
import time
import os
import json
from yadrive import YaDrive
from vkapi import VkClient
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

    def get_status_data(self, path, text_log):
        folder_list = self.disck.get_files_list(path)['files']
        if 'status.json' in folder_list:
            self.disck.download_from_cloud('status.json', path)
            with open('status.json') as f:
                files_data = json.load(f)  

            text_log.setText('Folder list obtained from clud')
        else:    
            files_data = {
            'last_update' : 0,
            'items' : []
            }
            text_log.setText('Creating new Folder list')
        return files_data


    def transport_from_vk_to_cloud(self, vk_token, owner_id, album_id, clud_token, 
                                    cloud_path, qty=None, text_log=None, p_bar=None):
        '''
        vk_token - vk access token,
        owner_id - id vk user
        albun_id - type of album - profile, wall, saved
        cloud_token - access token for yandex drive
        cloud path - path to folder in yandex disck
        qty - naumber of photo for uplading to cloud
        text_log - qTexr oject for dysplaing current startus in windows form
        p_bar - qProgressBar object  for dysplaing startus bar in windows form
        '''
        #  VK:
        text_log.setText('Start vk to cloud process')
        vk_clien = VkClient(vk_token)
        text_log.setText('Connection to vk')
        photo_base = vk_clien.get_photos(owner_id, album_id)
        progress = 10
        p_bar.setProperty("value", progress)
        
        if 'response' in photo_base:
            photo_base = photo_base['response']['items']
            total_photo = len(photo_base)
            text_log.setText(f'{total_photo} photos found')
            # satusbar step:
            p_quant = 90/qty - 1 if qty is not None else 90/total_photo - 1   
           
            text_log.setText('Connection to YaDrive')
            # YaDrive:
            self.disck = YaDrive(clud_token)
            cp = self.disck.get_files_list(cloud_path)
           
            if cp['code'] == 404:
                # creating path to folder if it doesn't exist
                self.disck.create_path_to_folder(cloud_path)
            text_log.setText('Getting folder list')
            # creating or downloading information about folder:
            files_data = self.get_status_data(cloud_path, text_log)
            files_count = len(files_data['items'])
            # file name list for control the same file names
            tmp_photo_list = [file['file_name'] for file in files_data['items']]
            # file name list for control the uniqueness of the copied images
            id_list = [file['id'] for file in files_data['items']]

            # uploading process:
            for entry in reversed(photo_base):
                if entry['id'] not in id_list:
                    photo_name = f"{entry['likes']['count']}" + '.jpg'
                    if photo_name in tmp_photo_list:
                        date = datetime.datetime.utcfromtimestamp(entry['date']).strftime('-%d-%m-%Y-%H-%M-%S')
                        photo_name = f"{entry['likes']['count']}" + date + '.jpg'       
                    tmp_photo_list.append(photo_name)
                    up_code = self.disck.upload_from_url(entry[self.get_max_res(entry)], photo_name, cloud_path)
                    
                    text_log.setText(f'{photo_name} uploading to cloud')
                    progress += p_quant
                    p_bar.setProperty("value", progress)

                    if up_code == 200:
                        # change staus file
                        files_data['items'].append({"file_name": photo_name, "id" : entry['id'],
                          "size": f"{entry['height']} x {entry['width']} " })
                        if qty is not None and len(tmp_photo_list) - files_count == qty:
                            break
                    else:
                        text_log.setText(f"can't file {photo_name} uploading to cloud")
                else: 
                    text_log.setText('This files already been written to disk')
        
            # uplading status file:
            files_data['last_update'] = int(time.time())
            text_log.setText('Uploading to cloud status file')
            with open('status.json', 'w', encoding='utf-8') as f:
                json.dump(files_data, f, indent=2)
            self.disck.upload_from_drive('status.json', cloud_path)
           
            text_log.setText('Uploading is sucsessfull')
            p_bar.setProperty("value", 100)
        elif 'error' in photo_base:
            text_log.setText(f"error - {photo_base['error']['error_msg']}")
        else:
            text_log.setText('error - undefined error')



class WindowsForms(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.__preset()
        self.pushButton.clicked.connect(self.but_action)
        self.checkBox.clicked.connect(self.check_box_action)
        self.l_layуr = LogicalLair()
    
    # listWidget get items; default item == profile
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
        self.progressBar.setProperty("value", 0)

        if self.checkBox.isChecked():
            numbe_of_photo = self.spinBox.value()
        else:
            numbe_of_photo = None

        self.l_layуr.transport_from_vk_to_cloud(vk_token, vk_id, vk_album, yd_token, 
                            yd_path, numbe_of_photo, self.label_3, self.progressBar)

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
    main()
