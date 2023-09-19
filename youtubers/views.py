from django.shortcuts import render

# Create your views here.
def youtubers(request):
    return render(request, 'youtubers/youtubers.html')

def youtubers_detail(request, id):
    pass

def search(request):
    pass
