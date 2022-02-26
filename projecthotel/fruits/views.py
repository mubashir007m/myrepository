from django.shortcuts import render
from.models import fruits
# Create your views here.
def first(request):
    return render(request, 'html1.html')
def second(request):
    a = request.POST['idv']
    b = request.POST['names']
    c = request.POST['prices']
    d = request.POST['quant']
    m = request.FILES['img']
    data = fruits(id1=a, name=b, price=c, quantity=d, image=m)
    data.save()
    return render(request, 'html2.html')
def display(request):
    data = fruits.objects.all()
    return render(request, 'html4.html',{'r':data})
