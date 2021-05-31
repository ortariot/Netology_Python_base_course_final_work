import datetime
import time
import os
import json
from yadrive import YaDrive
from vkapi import VkClient
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import designtwo
import threading


class LogicalLair(QtWidgets.QDialog):
    # q signals:
    changed_value = pyqtSignal(int)
    changed_log = pyqtSignal(str)

    def get_max_res(self, item):
        out = 0
        for sl in item:
            if 'photo' in sl:
                value = int(sl[6:])
                if value > out:
                    out = value
        return f"photo_{out}"

    def get_status_data(self, path):
        folder_list = self.disck.get_files_list(path)['files']
        if 'status.json' in folder_list:
            self.disck.download_from_cloud('status.json', path)
            with open('status.json') as f:
                files_data = json.load(f)
            self.changed_log.emit('Folder list obtained from clud')
        else:
            files_data = {'last_update': 0,
                          'items': []
                          }
            self.changed_log.emit('Creating new Folder list')
        return files_data

    def transport_from_vk_to_cloud(self, vk_token, owner_id,
                                   album_id, clud_token,
                                   cloud_path, qty=None
                                   ):
        '''
        vk_token - vk access token,
        owner_id - id vk user
        albun_id - type of album - profile, wall, saved
        cloud_token - access token for yandex drive
        cloud path - path to folder in yandex disck
        qty - naumber of photo for uplading to cloud
        text_log - qTexr oject for dysplaing current startus in windows form
        '''
        #  VK:
        self.changed_log.emit('Start vk to cloud process')
        vk_clien = VkClient(vk_token)
        self.changed_log.emit('Connection to vk')
        photo_base = vk_clien.get_photos(owner_id, album_id)
        progress = 10
        self.changed_value.emit(progress)

        if 'response' in photo_base:
            photo_base = photo_base['response']['items']
            total_photo = len(photo_base)
            self.changed_log.emit(f'{total_photo} photos found')
            # satusbar step:
            p_quant = 90/qty - 1 if qty is not None else 90/total_photo - 1

            self.changed_log.emit('Connection to YaDrive')
            # YaDrive:
            self.disck = YaDrive(clud_token)
            cp = self.disck.get_files_list(cloud_path)

            if cp['code'] == 404:
                # creating path to folder if it doesn't exist
                self.disck.create_path_to_folder(cloud_path)
            self.changed_log.emit('Getting folder list')
            # creating or downloading information about folder:
            files_data = self.get_status_data(cloud_path)
            files_count = len(files_data['items'])
            # file name list for control the same file names
            tmp_photo_list = [file['file_name']
                              for file in files_data['items']]
            # file name list for control the uniqueness of the copied images
            id_list = [file['id'] for file in files_data['items']]

            # uploading process:
            for entry in reversed(photo_base):
                if entry['id'] not in id_list:
                    photo_name = f"{entry['likes']['count']}" + '.jpg'
                    if photo_name in tmp_photo_list:
                        date = datetime.datetime.\
                            utcfromtimestamp(entry['date']).\
                            strftime('-%d-%m-%Y-%H-%M-%S')
                        photo_name = f"{entry['likes']['count']}"\
                            + date + '.jpg'
                    tmp_photo_list.append(photo_name)
                    up_code = self.disck.\
                        upload_from_url(entry[self.get_max_res(entry)],
                                        photo_name, cloud_path)

                    self.changed_log.emit(f'{photo_name} uploading to cloud')
                    progress += p_quant
                    self.changed_value.emit(int(progress))

                    if up_code == 200:
                        # change staus file
                        files_data['items'].append(
                            {"file_name": photo_name,
                             "id": entry['id'],
                             "size": f"{entry['height']} x {entry['width']}"}
                                                   )
                        if qty is not None and\
                                len(tmp_photo_list) - files_count == qty:
                            break
                    else:
                        self.changed_log.\
                            emit(f"can't file {photo_name} uploading to cloud")
                else:
                    self.changed_log.\
                        emit('This files already been written to disk')

            # uplading status file:
            files_data['last_update'] = int(time.time())
            self.changed_log.emit('Uploading to cloud status file')
            with open('status.json', 'w', encoding='utf-8') as f:
                json.dump(files_data, f, indent=2)
            self.disck.upload_from_drive('status.json', cloud_path)

            self.changed_log.emit('Uploading is sucsessfull')
            self.changed_value.emit(100)
            time.sleep(5)
            self.changed_log.emit('ready')
            self.changed_value.emit(0)

        elif 'error' in photo_base:
            self.changed_log.\
                emit(f"error - {photo_base['error']['error_msg']}")
        else:
            self.changed_log.emit('error - undefined error')


class WindowsForms(QtWidgets.QMainWindow, designtwo.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__preset()
        self.start_pushButton.clicked.connect(self.but_action)
        self.checkBox.clicked.connect(self.check_box_action)
        self.l_layуr = LogicalLair()

    def make_connection_progress_bar(self, logicalLayer=None):
        if logicalLayer is None:
            logicalLayer = self.l_layуr
        logicalLayer.changed_value.connect(self.get_slider_value)

    def make_connection_log(self, logicalLayer=None):
        if logicalLayer is None:
            logicalLayer = self.l_layуr
        logicalLayer.changed_log.connect(self.get_log_text)

    @pyqtSlot(int)
    def get_slider_value(self, val):
        self.progressBar.setValue(val)

    @pyqtSlot(str)
    def get_log_text(self, text):
        self.label_9.setText(text)

# listWidget get items; default item == profile
    def __listWidget_get_item(self):
        if self.vk_album_listWidget.selectedItems():
            if self.vk_album_listWidget.selectedItems()[0] ==\
                    self.vk_album_listWidget.item(1):
                return self.vk_album_listWidget.item(1).text()
            elif self.vk_album_listWidget.selectedItems()[0] ==\
                    self.vk_album_listWidget.item(2):
                return self.vk_album_listWidget.item(2).text()
            else:
                return self.vk_album_listWidget.item(0).text()
        else:
            return self.vk_album_listWidget.item(0).text()

    def __preset(self):
        dir_list = os.listdir()
        if 'settings.json' in dir_list:
            with open('settings.json', 'r', encoding='utf-8') as f:
                settings = json.load(f)
            self.vk_token_textEdit.setText(settings['vk_token'])
            self.vk_usr_id_textEdit.setText(settings['vk_id'])
            self.yd_token_textEdit.setText(settings['yd_token'])
            self.yd_path_textEdit.setText(settings['yd_path'])

    def __set_settings(self, vk_token, vk_id, vk_album, yd_token, yd_path):
        settings = {'vk_token': vk_token,
                    'vk_id': vk_id,
                    'vk_album': vk_album,
                    'yd_token': yd_token,
                    'yd_path': yd_path
                    }
        with open('settings.json', 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=2)

    def but_action(self):
        vk_token = self.vk_token_textEdit.toPlainText()
        vk_id = self.vk_usr_id_textEdit.toPlainText()
        vk_album = self.__listWidget_get_item()
        yd_token = self.yd_token_textEdit.toPlainText()
        yd_path = self.yd_path_textEdit.toPlainText()

        self.__set_settings(vk_token, vk_id, vk_album, yd_token, yd_path)
        self.progressBar.setProperty("value", 0)
        self.make_connection_progress_bar()
        self.make_connection_log()

        if self.checkBox.isChecked():
            numbe_of_photo = self.spinBox.value()
        else:
            numbe_of_photo = None

        upload_process_thread = \
            threading.Thread(target=self.l_layуr.transport_from_vk_to_cloud,
                             args=(vk_token, vk_id, vk_album,
                                   yd_token, yd_path, numbe_of_photo)
                             )

        upload_process_thread.start()

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
    # main_thread = threading.Thread(target=main)
    # main_thread.start()
    main()
