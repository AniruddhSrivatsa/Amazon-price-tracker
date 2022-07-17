from django.shortcuts import get_object_or_404, render,redirect
from .forms import amazeform
from .models import amaze
from django.urls import reverse_lazy
from django.views.generic import DeleteView,UpdateView
import requests
# Create your views here.

def home(request):
    no_discounts=0
    error=None 
    form=amazeform(request.POST or None)

    if request.method =='POST':
        try:
            if form.is_valid():
                form.save()
                form.save()
              
        except:
            error="Sorry! Something is wrong"
        
    form=amazeform()
    lists=amaze.objects.all()
    item_no=lists.count()
    count_disc=0
    if item_no>0:
        disc_liss=[]
        for item in lists:
            if item.exp_val>item.curr_val:
                disc_liss.append(item)
            count_disc=len(disc_liss)


    context={"lists":lists,
    "item_no":item_no,
    "count_disc":count_disc,
    "form":form,
    "error":error
    }

    return render(request,'track/main.html',context)


class LinkDeleteView(DeleteView):
    model=amaze
    template_name="track/delete.html"
    success_url=reverse_lazy('track:home')
    
def updating(request):
    qs=amaze.objects.all()
    for link in qs:
        link.save()
    return redirect("track:home")

'''def changed(request,amaze_id):
    chan=request.POST.get('c', False)
    obj=get_object_or_404(amaze,id=amaze_id)
    obj.old_val=chan
    obj.save()
    return render(request,'track/main.html',context)


class changed(UpdateView):
    model=amaze
    fields=['old_val']
    template_name="track/change.html"
    success_url=reverse_lazy('track:home')'''

        


    
    







