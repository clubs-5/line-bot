from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('KH0oUZctJ5HEkTaJ8LsDewWB3efij6CtAJa1Sr6Nrp+LtzREzjZS43aUZJxkWdxary0Yhkyyq0hkmmx/m/GeBmD4qJZqCZWQ9oNFyD/yQDoU2unJKaXNYdmUVYrgnFM0VPlct1UtmfRo9TjiaBxcKAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e5d41aa80b555092dcc2b140fff4c99c')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

#處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text 
    if '我想看影集' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextMessage(text=msg)
        line_bot_api.reply_message(reply_token,message)


if __name__ == "__main__":
    app.run()