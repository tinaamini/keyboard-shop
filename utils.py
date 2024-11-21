# utils.py
def format_price(value):
    return "{:,}".format(value)


import requests


def send_otp_code(phone_number, code):
    data = {'from': '50002710017796', 'to': phone_number, 'text': f'{code}'}
    response = requests.post('https://console.melipayamak.com/api/receive/balance/e97f2fd3453d4717bd528e07a8210f0d', json=data)
