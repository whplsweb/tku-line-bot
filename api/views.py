from urllib.parse import parse_qsl

from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, PostbackEvent
from api import func
from api.models import User
from api.mod import getUserName

import traceback

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden
        except LineBotApiError:
            return HttpResponseBadRequest

        for event in events:
            if isinstance(event, MessageEvent):
                # # 傳過來的訊息是文字訊息（2022/07/23測 不可用）
                # if isinstance(event.message, TextSendMessage):

                # 獲取 user 的 uid
                uid = event.source.user_id
                name = getUserName(uid)

                # 若不存在 則存入user
                if not (User.objects.filter(uid=uid).exists()):
                    print('該用戶尚未註冊本系統')
                    user = User.objects.create(uid=uid, name=name)
                    user.save()
                else:
                    user = User.objects.get(uid=uid)
                    if (user.name != name):
                        user.name = name
                        user.save()

                # 接受user的文字訊息
                umes = event.message.text

                jobs_word = ['@短期打工', '@長期打工']

                if umes == "@美食優惠":
                    func.sendMulti(event, 'food')
                elif umes == "@旅遊優惠":
                    func.sendMulti(event, 'travel')
                elif jobs_word[0] in umes or jobs_word[1] in umes:
                    type = umes.split(':')
                    main_type = type[0]
                    try:
                        pos = type[1]
                        try:
                            city = type[2]
                        except:
                            traceback.print_exc()
                            city = None
                    except:
                        traceback.print_exc()
                        pos = None

                    if not pos:
                        func.select(event, main_type, mod='pos')
                    else:
                        if not city:
                            func.select(event, main_type, mod='city', pos=pos)
                        else:
                            if main_type == '@短期打工':
                                func.sendMulti(event, 'short', city)
                            elif main_type == '@長期打工':
                                func.sendMulti(event, 'long',city)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def auto_send_message(request):
    key = request.POST.get('key', '')
    if key != 'RrpxZ@YEUS6rhthkP3VCvN8GkWBxtMv@':
        return HttpResponseBadRequest()
    try:
        func.pushMsg()
        return JsonResponse({
            'msg': '訊息發送成功'
        })
    except:
        traceback.print_exc()
        return HttpResponseBadRequest()