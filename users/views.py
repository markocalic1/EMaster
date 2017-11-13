from django.shortcuts import render,reverse,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic.base import RedirectView
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template


def home(request):
    context = {
        "title": "EMasters",
    }
    return render(request, "users/home.html", context)


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(
                username=username,
                password = raw_password
            )
            group = Group.objects.get(name='student')
            form.instance.groups.add(group)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register_form.html', {'form': form})


class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = 'users/home.html'
    template_name = 'users/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(self.request, user)

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')

class LogoutView(RedirectView):

    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

def about(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')

        content = template.render({ 'contact_name': contact_name, 'contact_email': contact_email, 'form_content': form_content, })

        email = EmailMessage(
            "New contact form submission",
            content,
            "Your website" + '',
            ['youremail@gmail.com'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        return redirect('about')

    return render(request, "users/about.html", { 'form': form_class, })

