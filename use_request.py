import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200 :
        print(f'success! Response = {response.status_code}')
        print(f'content{response.text}')
    else:
        print(f'ada kesalahan request {response.status_code}')
except Exception as e:
    print(f'ada error {e}')
print('program ended')
