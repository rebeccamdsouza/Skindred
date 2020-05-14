from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
import string


@csrf_exempt
def bot_reply(request):
    print(request.GET['usermessage'])
    # save patient reply in db
    # generate bot reply
    bot_reply = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    # save bot reply in db
    return JsonResponse({'botreply':bot_reply})


def export_chat(request):
    # export chat
    return None

