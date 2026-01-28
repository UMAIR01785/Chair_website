from django.shortcuts import render

from .forms import ContactForm
# Create your views here.
def contact(request):
    if request.method == "POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            contact=form.save()

            

    return render(request,'contact/conatct.html')