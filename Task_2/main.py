import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": 'Temp/'+ path_to_file, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json()['href']
        response = requests.put(href, data=open(path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'test.txt'
    token = input('Введите токен: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)