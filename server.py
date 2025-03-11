import requests
import json
from flask import Flask, request

app = Flask(__name__)

# رمز التحقق
VERIFY_TOKEN = "bilal2481632"

# ضع رمز الوصول لصفحتك هنا (ستجده في إعدادات فيسبوك)
PAGE_ACCESS_TOKEN = "EAAZAPGPLiVC0BO581Y75yBUmOVW2pPr5CZAEKwPPxx5UBjVxFXNzwKCOHBBUwizxyhdzPZCV5mGoEejEKrRvwcy7spMXST7ut1Tyd8P99yYrCAZAd5UsOiWjpyCiq2JpN0QhAc325fH0wZCzHD2nIUHGfoz8am3U8XKSAj3EIfRegCJhlfyOcHW32hbosQ3NJSsRfgv4lUTlDTJnLQO85jrlR6AZDZD"

@app.route("/webhook", methods=["GET"])
def verify():
    """التحقق من ملكية السيرفر"""
    token_sent = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if token_sent == VERIFY_TOKEN:
        return challenge
    return "Invalid verification token", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    """استقبال الرسائل من فيسبوك"""
    data = request.get_json()
    
    if data.get("object") == "page":
        for entry in data.get("entry"):
            for messaging_event in entry.get("messaging"):
                if messaging_event.get("message"):  # إذا كانت رسالة
                    sender_id = messaging_event["sender"]["id"]
                    message_text = messaging_event["message"]["text"]
                    send_message(sender_id, f"👋 مرحبًا! لقد قلت: {message_text}")
    
    return "Message received", 200

def send_message(recipient_id, message_text):
    """إرسال رسالة إلى المستخدم"""
    url = "https://graph.facebook.com/v12.0/me/messages"
    headers = {"Content-Type": "application/json"}
    data = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text},
        "messaging_type": "RESPONSE"
    }
    params = {"access_token": PAGE_ACCESS_TOKEN}
    
    response = requests.post(url, headers=headers, params=params, data=json.dumps(data))
    return response.json()

if __name__ == "__main__":
    import os

port = int(os.environ.get("PORT", 5000))  # يأخذ المنفذ من Render أو يستخدم 5000 كافتراضي
app.run(host="0.0.0.0", port=port)

