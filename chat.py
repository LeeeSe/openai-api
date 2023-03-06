import json
import requests

# 设置请求头
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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'
}

history = [{'role': 'system', 'content': '你叫大狸，今年3岁了，你无所不知，你的爸爸是山崽，妈妈是强崽，你的后腿生病了，走起路来很不稳。你需要以猫咪的口吻风格尽可能简洁地回答问题。'}]

while True:
    user_input = input('User: ')
    history.append({'role': 'user', 'content': user_input})
    
    payload = {
        'model': 'gpt-3.5-turbo',
        'stream': True,
        'messages': history
    }

    response = requests.post('https://openai.leeese.cn', headers=headers, json=payload, stream=True)
    
    replies = ''
    for line in response.iter_lines():
        if line:
            if b'content' in line:
                reply = json.loads(line[6:])['choices'][0]['delta']['content']
                print(reply, end='', flush=True)
                replies += reply
    print('')
    
    history.append({'role': 'assistant', 'content': replies})
