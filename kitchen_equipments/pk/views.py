from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request,"front.html")

def spec(request):
    return render(request,"aboutus.html")
def kick(request):
    return render(request,"gallary.html")
def run(request):
    return render(request,"ourclient.html")
def pic(request):
    return render(request,"contact.html")
def dev(request):
    return render(request,"product.html")



