from django.http import IttpResponse
from django.shortcuts import render
def home(request):
if 'user' not in request.COOKIES: # (For first time user)
response - render(request-request,
template_name-'template.html',
context={'message': 'Any message to tell the action to record user.'})
response.set_cookie(key='user', value-'userl')
return response
else:
return render(request=request,
template_name-'template.html',
context=('message' : 'Welcome back, ' t request.COOKIES['user')))