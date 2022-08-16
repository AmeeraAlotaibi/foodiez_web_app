from .forms import LoginForm, RegisterForm


def processor(request):
    register_form = RegisterForm()
    login_form = LoginForm()
    return {'register_form': register_form, "login_form": login_form,}

# Since the forms are to be conditionally rendered in the templates, when can also do this here if needed
# by checking the request.user.is_authenticated
# some people would do this extra step, while others wouldn't