from django.conf import settings
from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, \
    QuickReplyButton, MessageAction, CarouselColumn
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    ConfirmTemplate,
    CarouselTemplate,
    MessageTemplateAction,
    URITemplateAction,
    PostbackTemplateAction,
    DatetimePickerTemplateAction
)
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
imgurl = 'https://cc.tvbs.com.tw/img/upload/2022/05/20/20220520170357-1298d211.jpg'
# 傳送文字
def sendText(event):
    try:
        message = TextSendMessage(
            text = "我是口袋電商小助手您好"
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))

# 傳送圖片
def sendImage(event):
    try:
        message = ImageSendMessage(
            original_content_url = 'https://cc.tvbs.com.tw/img/upload/2022/05/20/20220520170357-1298d211.jpg',
            preview_image_url = 'https://cc.tvbs.com.tw/img/upload/2022/05/20/20220520170357-1298d211.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))

# 傳送貼圖
def sendStick(event):
    try:
        message = StickerSendMessage(
            package_id='1',
            sticker_id='2'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))

# 傳送多項
def sendMulti(event):
    try:
        message = [
            TextSendMessage(
                text="我是口袋電商小助手您好"
            ),
            ImageSendMessage(
                original_content_url='https://cc.tvbs.com.tw/img/upload/2022/05/20/20220520170357-1298d211.jpg',
                preview_image_url='https://cc.tvbs.com.tw/img/upload/2022/05/20/20220520170357-1298d211.jpg'
            ),
            StickerSendMessage(
                package_id='1',
                sticker_id='2'
            )
        ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))

def sendPostion(event):
    try:
        message = LocationSendMessage(
            title='101大樓',
            address='台北市信義路',
            latitude=25.034207,
            longitude=121.564560
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))

def sendQuickReply(event):
    try:
        message = TextSendMessage(
            text='選擇最喜歡',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label='Python', text='Python')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='C++', text='C++')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))

def sendButtonTemplate(event):
    # try:
    message = TemplateSendMessage(
        alt_text = '取代文字',
        template=ButtonsTemplate(
            thumbnail_image_url='https://cc.tvbs.com.tw/img/upload/2022/05/20/20220520170357-1298d211.jpg',
            title='大標題',
            text='內文',
            actions=[
                MessageTemplateAction(
                    label='文字測試',
                    text='@文測'
                ),
                URITemplateAction(
                    label='連結測試',
                    uri='https://google.com'
                ),
                # 不用發送文字 就可以跟後台互動
                PostbackTemplateAction(
                    label='回傳訊息',
                    data='action=buy'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    # except:
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))

def sendConfirmTemplate(event):
    try:
        message = TemplateSendMessage(
            alt_text='確認',
            template=ConfirmTemplate(
                text='您確認要預約嗎',
                actions=[
                    MessageTemplateAction(
                        label='是',
                        text='@yes'
                    ),
                    MessageTemplateAction(
                        label='否',
                        text='@no'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))

def sendCarouselTemplate(event):
    try:
        message = TemplateSendMessage(
            alt_text='確認',
            template=CarouselTemplate(
                columns = [
                    CarouselColumn(
                        thumbnail_image_url=imgurl,
                        title='樣板一號',
                        text='pizza',
                        actions=[
                            MessageTemplateAction(
                                label='文字測試',
                                text='@文測'
                            ),
                            URITemplateAction(
                                label='連結測試',
                                uri='https://google.com'
                            ),
                            # 不用發送文字 就可以跟後台互動
                            PostbackTemplateAction(
                                label='回傳訊息',
                                data='action=buy'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=imgurl,
                        title='樣板二號',
                        text='pizza',
                        actions=[
                            MessageTemplateAction(
                                label='文字測試',
                                text='@文測'
                            ),
                            URITemplateAction(
                                label='連結測試',
                                uri='https://google.com'
                            ),
                            # 不用發送文字 就可以跟後台互動
                            PostbackTemplateAction(
                                label='回傳訊息',
                                data='action=buy'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))

def sendDateTime(event):
    try:
        message = TemplateSendMessage(
            alt_text='日期時間',
            template=ButtonsTemplate(
                thumbnail_image_url=imgurl,
                title='範例',
                text='請選擇：',
                actions=[
                    DatetimePickerTemplateAction(
                        label = '選取日期',
                        data="action=sell&mode=date",
                        mode="date",
                        initial="2019-01-01",
                        min="2019-01-01",
                        max="2020-12-31"
                    ),
                    DatetimePickerTemplateAction(
                        label='選取時間',
                        data="action=sell&mode=time",
                        mode="time",
                        initial="10:00",
                        min="00:00",
                        max="23:59"
                    ),
                    DatetimePickerTemplateAction(
                        label='選取日期時間',
                        data="action=sell&mode=datetime",
                        mode="datetime",
                        initial="2019-01-01T10:00",
                        min="2019-01-01T00:00",
                        max="2020-12-31T23:59"
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))

def manageForm(event, umes):
    try:
        flist = umes[3:].split('/')
        text1 = '姓名：' + flist[0] + '\n'
        text1 += '日期：' + flist[1] + '\n'
        text1 += '房型：' + flist[2]
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))
