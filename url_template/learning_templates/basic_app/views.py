from django.shortcuts import render

# Create your views here.

def index(request):
    text1 = {'text_here':'Hello World','number':'100','message':'Status 200'}
    return render(request, 'index.html',context=text1)

def other(request):
        return render(request, 'other.html')

def relative_url_template(request):
    return render(request, 'relative_url_template.html')

