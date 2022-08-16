
from .forms import LoginForm, RegisterForm


def processor(request):
    register_form = RegisterForm()
    login_form = LoginForm()
    return {'register_form': register_form, "login_form": login_form,}
    