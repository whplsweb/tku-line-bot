import traceback

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
from api.models import User
import web_crawler.func

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def select(event, type, mod=None, pos=None):
    try:
        if mod == 'pos':
            items = quickTemplate(type, layer=1)
            text = '請選擇地區'
        elif mod == 'city':
            items = quickTemplate(type, layer=2, pos=pos)
            text = '請選擇城市'
        message = TextSendMessage(
            text=text,
            quick_reply=QuickReply(
                items=items
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        traceback.print_exc()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))


def sendMulti(event, type, city=None):

    columns = []

    if type == 'food':
        data_list = web_crawler.func.food()
    elif type == 'travel':
        data_list = web_crawler.func.travel()
    elif type == 'short' or type == 'long':
        if type == 'short':
            data_list = web_crawler.func.short(city)
        elif type == 'long':
            data_list = web_crawler.func.long(city)


    for data in data_list:
        title = data['title']
        a_href = data['a_href']
        sub_text = data['sub_text']
        img_src = data['img_src']
        t = columnTemplate(title, sub_text, img_src, a_href)
        columns.append(t)

    try:
        message = TemplateSendMessage(
            alt_text='確認',
            template=CarouselTemplate(
                columns = columns
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        traceback.print_exc()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))


def pushMsg():
    users = User.objects.all()
    for user in users:
        uid = user.uid
        data = web_crawler.func.gvm()[0]
        title = data['title']
        a_href = data['a_href']
        sub_text = data['sub_text']
        img_src = data['img_src']
        msg = buttonTemplate(title, sub_text, img_src, a_href)
        line_bot_api.push_message(uid, [
            TextSendMessage(
                text='"本週理財文章分享"'
            )
            ,msg]
        )

def buttonTemplate(title, text, imgurl, url):
    title = text[0:39]
    text = text[0:59]
    t = TemplateSendMessage(
        alt_text='取代文字',
        template=ButtonsTemplate(
            thumbnail_image_url=imgurl,
            title=title,
            text=text,
            actions=[
                URITemplateAction(
                    label='查看更多',
                    uri=url
                )
            ]
        )
    )
    return t

def quickTemplate(type, layer, pos=None):
    citys = {
        '北部': ['基隆', '台北', '新北' ,'桃園' ,'新竹'],
        '中部': ['苗栗' ,'台中', '彰化', '南投', '雲林' ,'嘉義'],
        '南部': ['台南', '高雄', '屏東'],
        '東部': ['宜蘭', '花蓮', '台東']
    }
    qs = []
    if layer == 1:
        for pos in citys.keys():
            q = QuickReplyButton(
                action = MessageAction(label=pos, text=f'{type}:{pos}')
            )
            qs.append(q)
    else:
        citys_pos = citys[pos]
        for city in citys_pos:
            q = QuickReplyButton(
                action=MessageAction(label=city, text=f'{type}:{pos}:{city}')
            )
            qs.append(q)
    return qs

def columnTemplate(title, text, imgurl, url):
    title = text[0:39]
    text = text[0:59]
    c = CarouselColumn(
        thumbnail_image_url=imgurl,
        title=title,
        text=text,
        actions=[
            URITemplateAction(
                label='查看更多',
                uri=url
            )
        ]
    )
    return c
