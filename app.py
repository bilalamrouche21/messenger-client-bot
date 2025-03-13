from flask import Flask, request, jsonify
import requests
import config
from message_handler import handle_message

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # تحقق من التوكن للتحقق من صحة الـ Webhook
    if request.args.get('hub.verify_token') == config.VERIFY_TOKEN:
        return request.args.get('hub.challenge')
    return 'Verification token mismatch', 403

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                if messaging_event.get('message'):
                    sender_id = messaging_event['sender']['id']
                    message_text = messaging_event['message'].get('text')
                    response = handle_message(sender_id, message_text)
                    send_message(sender_id, response)
    return 'Message Processed', 200

# إرسال الرسائل إلى Facebook Messenger

def send_message(recipient_id, message_text):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'recipient': {'id': recipient_id},
        'message': {
            'text': message_text,
            'quick_replies': config.QUICK_REPLIES['main_menu']
        }
    }
    params = {
        'access_token': config.PAGE_ACCESS_TOKEN
    }
    response = requests.post(
        'https://graph.facebook.com/v11.0/me/messages',
        params=params,
        headers=headers,
        json=data
    )
    if response.status_code != 200:
        print(f'Error sending message: {response.status_code} - {response.text}')

if __name__ == '__main__':
    app.run(port=5000, debug=True) 