from multiprocessing import Pool
from requests import get

DOMAIN = 'http://ec2-52-91-14-62.compute-1.amazonaws.com/'

def send_request(val):
        while True:
                response = get(f'{DOMAIN}')
                data = response.json()
                print('Sent request')
                print(data)
if __name__ == '__main__':
        with Pool(150) as p:
                p.map(send_request, range(150))