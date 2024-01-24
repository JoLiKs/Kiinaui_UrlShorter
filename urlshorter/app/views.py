import random

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

CHARACTERS = 'ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz234567890'
@csrf_exempt
def index(request):
    if request.method == 'POST':
        short_url = 'kiin.fun/'
        for i in range(5): short_url += CHARACTERS[random.randint(0, len(CHARACTERS)-1)]

        return render(request, 'index.html', {'short_url': short_url})
    return render(request, 'index.html')