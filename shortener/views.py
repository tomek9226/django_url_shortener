from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import ShortURL

def index(request):
    if request.method == 'POST':
        url = request.POST['url']
        short = ShortURL.objects.create(original_url=url)
        return render(request, 'index.html', {'short': f"http://127.0.0.1:8000/{short.short_code}"})
    return render(request, 'index.html')

def redirect_view(request, code):
    try:
        short = ShortURL.objects.get(short_code=code)
        return redirect(short.original_url)
    except:
        return HttpResponse('Not found', status=404)