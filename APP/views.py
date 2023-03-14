from django.shortcuts import render

# Create your views here.

def ifconditional(request):
    D = {'a' : 10}
    return render(request, 'ifconditional.html', D)

def if_elseconditional(request):
    D = {'a' : 10, 'b' : 20}
    return render(request, 'if_elseconditional.html', D)

def if_elif_else_conditional(request):
    D = {'a' : 10, 'b' : 30, 'c' : 50}
    return render(request, 'if_elif_else_conditional.html', D)

def nested_if_else(request):
    D = {'a' : 50, 'b' : 30, 'c' : 20}
    return render (request, 'nested_if_else.html', D)

def loop(request):
    D = {'name' : 'SHUBHAM'}
    return render(request, 'loop.html', D)
