import requests
from pprint import pprint
  
class YaDrive:

    def __init__(self, token, default_cloud_path):
          self.token = token
          self.default_cloud_path = default_cloud_path
    
    def get_headers(self):
        return {
            'Accept' : 'application/json',
            'Authorization' : f'OAuth {self.token}'
        }

    def get_files_list(self, path):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = self.get_headers()
        parametrs = {
            'path' : path,
            'limit' : 1000
        }
        response = requests.get(files_url, headers=headers, params=parametrs)
        files = [file['name'] for file in response.json()['_embedded']['items']]
        print(files)

    def upload_from_drive(self, filename, path_to_cloud = None, path_to_folder = ''):
        if '\\' in filename:
            filename = filename[filename.rfind('\\') :]    
        if path_to_cloud is None:
            path_to_cloud = self.default_cloud_path          
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path_to_cloud + filename[1 : ], "overwrite": "true"}
        link =  requests.get(url, headers=headers, params=params).json().get('href', None)
        if link is None:
            print('Unable to get upload link')
        else:  
            response = requests.put(link, data=open(path_to_folder + filename, 'rb'))
            if response.status_code == 201:
                print('Upload is Success')
            else:
                print('Upload is falled')

    def upload_from_url(self, upload_url, filename, path_to_cloud = None ):
        if path_to_cloud is None:
           path_to_cloud = self.default_cloud_path   
        req_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {
            'path': path_to_cloud + filename, 
            'overwrite': 'true',
            'url' : upload_url
            }
        response = requests.post(req_url, headers=self.get_headers(), params=params)
        upload_link = response.json()['href']
        upload = requests.get(upload_link, headers=self.get_headers())
        print(upload)





if __name__ == '__main__':
    token = ''
    disck = YaDrive(token, '/test_app/')
    upload_url = 'https://sun9-12.userapi.com/impf/c621705/v621705348/2701/4T6pKaCSUtA.jpg?size=1280x960&quality=96&sign=aa9a2f011b23ba4acf40d82f342dd06d&c_uniq_tag=1aeiBaV9by9I9rlblesgaLgErFist0_UfUu8PVXbPrc&type=album'
    disck.upload_from_url(upload_url, 'test_photo.jpg')













