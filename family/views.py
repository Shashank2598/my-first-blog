from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def familypage(request):
	return render(request,'family/familypage.html',{})