from django.shortcuts import render

# Create your views here.



def home(request):

    '''
    View home function that returns the home page
    '''

    '''
    Here i use sql Group by in django annotes to filter out same polling unit and sum them
    '''


    return render(request, 'home.html', { })



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
