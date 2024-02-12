import random
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from app.models import UrlModel


def ads(request): return render(request, 'ads.txt')

def admin(request):
    urls = UrlModel.objects.all()
    return render(request, 'admin.html', {'urls': urls})

CHARACTERS = 'ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz234567890'
@csrf_exempt
def index(request):

    """Создание коротких ссылок"""
    if request.method == 'POST':
        if '.' not in request.POST['user_url'] or len(request.POST['user_url']) < 4 or 'kiin.fun' in request.POST['user_url']:
            return render(request, 'index.html', {'short_url': 'Неверная ссылка'})
        short_url = ''
        data = UrlModel.objects.all()
        for i in data:
            if i.user_url == request.POST['user_url']:
                short_url = 'Эта ссылка уже была сокращена!'
                return render(request, 'index.html', {'short_url': short_url})

        for i in range(5): short_url += CHARACTERS[random.randint(0, len(CHARACTERS)-1)]
        model = UrlModel()
        model.user_url = request.POST['user_url']
        model.short_url = short_url
        model.save()
        return render(request, 'index.html', {'short_url': 'kiin.fun/'+short_url})
    return render(request, 'index.html')


def get_full_url(short_url):
    """Получаем ссылку пользователя"""
    data = UrlModel.objects.all()
    for i in data:
        if i.short_url == short_url:
            return i.user_url

def redirection(request, short_url):

    """Перенаправляем пользователя по ссылке"""
    try:
        user_url = get_full_url(short_url)  # получает полный адрес по короткой ссылке
        if 'http' not in user_url:
            return redirect('https://'+user_url)
        return redirect(user_url)  # перенаправляем пользователя по ссылке
    except Exception as e:
        return render(request, 'index.html', {'short_url': 'Данный URL не существует!'})
