from django.shortcuts import render


def index(request):
    # TEMPLATE설정에 app/templates폴더 추가
    # templates폴더에 'index.html'추가

    # STATICFILES_DIRS에 app/static 폴더 추가
    # static 폴더에 Bootstrap CSS파일(css/bootstrap.css)추가

    # index.html에서 {% static %}태그를 사용해서
    # head태그 내의 link태그에 css/bootstrap.css를 불러오기

    # url '/'이 이 view와 연결되도록 urls.py실
    return render(request, 'index.html')