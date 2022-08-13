from django.shortcuts import render


# All handlers views in here

def handler403(request, exception):
    return render(request, 'pages/403.html')

def handler404(request, exception):
    return render(request, 'pages/404.html', status=404)

def handler500(request):
    return render(request, 'pages/500.html')
    