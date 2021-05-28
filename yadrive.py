import requests
from pprint import pprint
  
class YaDrive:

    def __init__(self, token, default_cloud_path=None):
          self.token = token
          if default_cloud_path is None:
              default_cloud_path = '/'
          self.default_cloud_path = default_cloud_path
    
    def get_headers(self):
        return {
            'Accept' : 'application/json',
            'Authorization' : f'OAuth {self.token}'
        }

    def get_files_list(self, path_to_cloud=None):
        if path_to_cloud is None:
            path_to_cloud = self.default_cloud_path    
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = self.get_headers()
        parametrs = {
            'path' : path_to_cloud,
            'limit' : 1000000
        }
        response = requests.get(files_url, headers=headers, params=parametrs)
        if response.status_code == 200:
            return {
                'code' : 200,
                'files' : [file['name'] for file in response.json()['_embedded']['items']]
            }
        elif response.status_code == 404:
            return {
                'code' : 404,
                'messege' : "The specified directory does not exist."
                }

    def upload_from_drive(self, filename, path_to_cloud=None, path_to_folder=''):
        if '\\' in filename:
            filename = filename[filename.rfind('\\') :]    
        if path_to_cloud is None:
            path_to_cloud = self.default_cloud_path          
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path_to_cloud + filename, "overwrite": "true"}
        link =  requests.get(url, headers=headers, params=params).json().get('href', None)
        if link is None:
            return 'Unable to get upload link'
        else:  
            response = requests.put(link, data=open(path_to_folder + filename, 'rb'))
            return response.status_code

    def upload_from_url(self, upload_url, filename, path_to_cloud=None ):
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
        return upload.status_code
    
    def download_from_cloud(self, filename, path_to_cloud=None):
        if path_to_cloud is None:
           path_to_cloud = self.default_cloud_path   
        url = 'https://cloud-api.yandex.net/v1/disk/resources/download'
        params = {
        'path': path_to_cloud + filename, 
        }
        response = requests.get(url, headers=self.get_headers(), params=params)
        download_link = response.json()['href']
        req = requests.get(download_link)
        with open(filename, 'wb') as f:
            f.write(req.content)
    
    def create_folder(self, folder_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {
            'path' : folder_name
        }
        req = requests.put(url, headers=self.get_headers(), params=params)
        return req.json()    
    
    def create_path_to_folder(self, path):
        if path[0] == '/':
            path = path[1 :]
        cloud_path = '/'  
        folder_root = self.get_files_list(cloud_path)  
        for folder in path.split('/'):
            if folder in folder_root:
                cloud_path += folder
                folder_root = self.get_files_list(cloud_path)
                cloud_path += '/'
            else:
                self.create_folder(cloud_path + folder)
                cloud_path += folder
                folder_root = self.get_files_list(cloud_path)
                cloud_path += '/'


if __name__ == '__main__':
    pass















