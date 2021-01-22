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
