from django.shortcuts import render

def index(request):
#    return render(request, 'pybo/sun_work/index.html')
    return render(request, 'pybo/sun_work/test.html')

def test(request):
    return render(request, 'pybo/sun_work/test.html')