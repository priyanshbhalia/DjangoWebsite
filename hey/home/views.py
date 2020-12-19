from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable':'beast is on'
    }
   # return HttpResponse("this is homepage")
    return render(request,'index.html',context)
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")
def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is services page")
def contacts(request):
    return render(request, 'contact.html')
    #return HttpResponse("this is contacts page")
