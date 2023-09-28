from django.shortcuts import render
from .models import Youtuber

# Create your views here.
def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'tubers': tubers,
    }
    return render(request, 'youtubers/youtubers.html', data)


from django.shortcuts import get_object_or_404

def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'tuber': tuber,
    }
    return render(request, 'youtubers/youtuber_detail.html', data)
    

def search(request):
    return render(request, 'youtubers/search.html')