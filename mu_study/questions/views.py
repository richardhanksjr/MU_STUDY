from django.shortcuts import render

def nextquestion(request):
    context = {'question': 'question'}
    template = 'questions/test.html'
    return render(request, template, context)
