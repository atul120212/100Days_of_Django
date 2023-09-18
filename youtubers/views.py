from django.shortcuts import render

# Create your views here.
def youtubers(request):
    return render(request, 'youtubers/youtubers.html')

def youtubers_details(request, id):
    pass
