import os
from django.template import engines
from django.conf import settings
from django.shortcuts import render
from mockDownApp.models import YesNoBar
from django.template.loader import render_to_string
from .forms import SignUpForm

# Create your views here.


# @login_required(login_url='/accounts/login/')
def home(request):

    '''
    View home function that returns the home page
    '''
    yesNoBar = YesNoBar.objects.all()
    print(yesNoBar)
    context = {'yesNoBar': yesNoBar}
    # # print(context)

    return render(request, 'home.html', context)



def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username =username, password=raw_password)
			login(request, user)
		return redirect('home_page')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {"form":form})



# @login_required(login_url='/accounts/login/')
def search_results(request):

    #query all username to find search_term
    if 'name' in request.GET and request.GET["username"]:
        search_term =request.GET.get("username")
        search_user = Image.search_users(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message, "searched":search_user})

    else:

        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})


def yesNoBar(request):
    if request.method == "POST":
        name = request.POST["name"]
        category = request.POST["category"]
        yesText = request.POST["yesText"]
        noText = request.POST["noText"]
        colorBg = request.POST["colorBg"]
        name = request.POST["name"]
        name = request.POST["name"]
    return render(request,"home.html")


