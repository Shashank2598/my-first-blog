from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import post,Comment,Profile
from django.views import generic
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import get_object_or_404
from .forms import UserForm,LoginForm,ProfileForm,AddPostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm,LoginForm
# Create your views here.
class homeview(generic.ListView):
	template_name = 'home/homepage.html'

	def get(self,request):
		queryset = post.objects.all()
		return render(request,'home/homepage.html',{ 'object_list':queryset ,'user':request.user})
	def post(self,request):
		queryset = post.objects.filter(title__icontains 
			= request.POST['searchbox'])
		return render(request,'home/homepage.html',{ 'object_list':queryset,'user': request.user })

class detailview(generic.DetailView):
	model = post
	template_name = 'home/detailview.html'
	def get(self,request,**kwargs):
		selected_object = post.objects.get(pk=kwargs['pk'])
		return render(request,'home/detailview.html',{
			'object' : selected_object,
			'all_comments': selected_object.comment_set.all(),
			})

	def post(self,request,**kwargs):
		selected_object = post.objects.get(pk=kwargs['pk'])
		value = request.POST.get('again')
		new_comment = Comment(name=value)
		new_comment.save()
		selected_object.comment_set.add(new_comment)
		return render(request,'home/detailview.html',{
			'object' : selected_object,
			'all_comments': selected_object.comment_set.all(),
			})


class postCreate(CreateView):
	model = post
	form_class = AddPostForm

class UserFormView(View):
	template_name='home/user_template.html'
	def get(self,request):
		if request.user.is_authenticated:
			return redirect('home:homepage')
		return render(request,self.template_name,{'form1':UserForm(),
						'form2':LoginForm()
						})

	def post(self,request):
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			user = authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('home:homepage')
		return render(request,self.template_name,{'form1':UserForm(),
			'form2':LoginForm()
			})

def logoutkrdo(request):
	logout(request)
	return redirect('home:user_form_view')

class loginkrdo(View):
	template_name = 'home/user_template.html'
	def get(self,request):
		return render(request,self.template_name,{'form1':UserForm(),'form2':LoginForm()})

	def post(self,request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home:homepage')
		else:
			return render(request,self.template_name,{'form1':UserForm(),
				'form2':LoginForm()
				})

class profileupdate(View):
	template_name = 'home/profile_template.html'
	def get(self,request,**kwargs):
		form = ProfileForm()
		return render(request,self.template_name,{'form':form})

	def post(self,request,**kwargs):
		try:
			prof = request.user.profile
			prof.bio = request.POST['bio']
			prof.save()
			return redirect('home:homepage')
		except:
			profile = Profile(user=request.user)
			profile.bio = request.POST['bio']
			profile.save()
			return redirect('home:homepage')
