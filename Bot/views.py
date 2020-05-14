from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
import random
import string
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["skindred"]


@csrf_exempt
def bot_reply(request):
    col = db[str(request.user)]
    print(request.user)
    message = request.GET['usermessage']
    print(message)
    # save patient reply in db
    chat = {
        "speaker": "user",
        "timestamp": datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"),
        "message": message,
    }
    col.insert_one(chat)

    # generate bot reply
    bot_reply = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

    # save bot reply in db
    chat = {
        "speaker": "bot",
        "timestamp": datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"),
        "message": bot_reply,
    }
    col.insert_one(chat)
    return JsonResponse({'botreply': bot_reply})


def export_chat(request):
    # export chat
    return None

