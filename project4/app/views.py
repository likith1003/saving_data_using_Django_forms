from django.shortcuts import render, HttpResponse
from app.forms import *
from app.models import *
# Create your views here.
def djform(request):
    SFO = StudentForm()
    d = {'SFO':SFO}
    if request.method == 'POST':
        sname=request.POST.get('sname')
        sage=request.POST.get('sage')
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        saddress=request.POST.get('saddress')
        cource=request.POST.get('cource')
        SO = Student(sname=sname, sage=sage, password=password, gender=gender, saddress=saddress,cource=cource)
        SO.save()
        return HttpResponse('Student Created Successfully')
    return render(request, 'djform.html', d)