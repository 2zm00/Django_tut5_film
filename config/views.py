from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
class HomeView(generic.TemplateView):
    template_name='home.html'

class UserCreateView(generic.CreateView):
    template_name='registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(generic.TemplateView):
    template_name='registration/register_done.html'