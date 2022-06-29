import requests

URL = 'https://www.amazon.com.br/Beyond-Good-Friedrich-Wilhelm-Nietzsche/dp/014044923X/ref=sr_1_1?keywords=beyond+good+and+evil&qid=1656545851&sprefix=beyond%2Caps%2C194&sr=8-1'

response = requests.get(url=URL)
if 'src="https://images-na.ssl-images-amazon.com/captcha/' in response.text:
    print('detected bot')
else:
    print('Bot not detected')


response = requests.get(url='http://localhost:8050/render.html', params={'url': URL, 'wait': 2})
if 'src="https://images-na.ssl-images-amazon.com/captcha/' in response.text:
    print('detected bot')
else:
    print('Bot not detected')
