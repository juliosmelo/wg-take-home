from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class UserCreateView(CreateView):
    form_class = UserCreationForm
    success_url = 'success_user_creation'
    template_name = 'choc_customer/user_new.html'