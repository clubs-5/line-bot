from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ButtonsTemplate,
)

#組圖面訊息
def imagemap_message():
    message = ImagemapSendMessage(
        base_url='https://example.com/base',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=1040, width=1040),
        video=Video(
            original_content_url='https://example.com/video.mp4',
            preview_image_url='https://example.com/video_preview.jpg',
            area=ImagemapArea(
                x=0, y=0, width=1040, height=585
            ),
            external_link=ExternalLink(
                link_uri='https://example.com/see_more.html',
                label='See More',
            ),
        ),
        actions=[
            URIImagemapAction(
                link_uri='https://example.com/',
                area=ImagemapArea(
                    x=0, y=0, width=520, height=1040
                )
            ),
            MessageImagemapAction(
                text='hello',
                area=ImagemapArea(
                    x=520, y=0, width=520, height=1040
                )
            )
        ]
    )
    return message