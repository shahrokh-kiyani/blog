from django.shortcuts import render


def home_view(request):
    return render(request, 'pages/home.html')

def error404(request, exception):
    return render(request, '404.html')

def error500(request):
    return render(request, '404.html')
    