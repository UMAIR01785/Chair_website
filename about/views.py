from django.shortcuts import render
from . models import TeamMange
# Create your views here.
def about(request):
    team=TeamMange.objects.all()
    context={
        'team':team,
    }
    return render(request,'about/fullabout.html',context)