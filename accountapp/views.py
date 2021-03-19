from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        # db에 데이터를 저장

        #list에 objects를 담아서 보내줄 예정임

        return HttpResponseRedirect(reverse('accountapp:hello_world')) # reverse는 함수형 view에서 사용한다.
    else:
        hello_world_list = HelloWorld.objects.all()
        #get에서도 보내줄 예정임
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})



class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #reverse_lazy는 class형 view에서 사용한다
    template_name = 'accountapp/create.html'