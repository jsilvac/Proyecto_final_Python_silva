from django.shortcuts import render
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages as messages_module
from .models import *
from .forms import *

# Create your views here.
@login_required
def messagesFunc(request):
    form=messagesForm()
    allMessages=Messages.objects.filter(sendTo=request.user) 
    if request.method == 'POST':
        form=messagesForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            print(info)
            msg=Messages(author=request.user,sendTo=info['toUser'],message=info['message'])
            msg.save()
            messages_module.success(request,"Message Sended")
            form= messagesForm()
            return render (request,'messages.html',{'form':form,'allMessages':allMessages})
        else:
            messages_module.success(request,"Messagge Not Sended")
            return render (request,'messages.html',{'form':form,'allMessages':allMessages})  
    return render (request,'messages.html',{'form':form,'allMessages':allMessages,  })

@login_required
def delMsg(request,id):
    form=messagesForm()
    allMessages=Messages.objects.filter(sendTo=request.user) 
    msg=Messages.objects.get(id=id)
    msg.delete()
    messages_module.success(request,"Message Deleted")
    return render(request,'messages.html',{'form':form,'allMessages':allMessages})

@login_required
def viewMsg(request,id):
     msg=Messages.objects.get(id=id)
     if request.method == 'POST' and msg:
        msg.delete()
        messages_module.success(request,"Message Deleted")
        return render(request,'messages.html')
     else:
          return render(request,'viewMsg.html',{'msg':msg})