
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.models import User
from .forms import RegistrationForm, EditProfileForm, EditUserProfileForm
from .forms import AssignmentForm
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from pagedown.widgets import PagedownWidget
from django import forms
from django.urls import reverse_lazy
from django.contrib.contenttypes.models import ContentType
from django.views.generic.edit import FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.db.models import Q


# Create your views here.
def home(request):
	#num_users=Author.objects.count()
	#front_page=TextModel.objects.all()
	return render(
		request,
		'home.html',
		context={}
		)

class AssignmentListView(generic.ListView):
	model=Assignment
	paginate_by = 10

# class ItemListView(generic.ListView):
# 	model=Item

# class ItemDetailView(generic.DetailView):
# 	model=Item




class AssignmentDetailView(LoginRequiredMixin,generic.DetailView):
	model=Assignment
	


class AssignmentCommentCreate(LoginRequiredMixin, generic.CreateView):
	model = AssignmentComment
	fields = ['inference','excel_sheet','result']

	def get_context_data(self, **kwargs):
		context = super(AssignmentCommentCreate, self).get_context_data(**kwargs)
		context['blog'] = get_object_or_404(Assignment, pk = self.kwargs['pk'])
		return context
	
        
	def form_valid(self, form):
		form.instance.author = self.request.user
		form.instance.blog=get_object_or_404(Assignment, pk = self.kwargs['pk'])
		return super(AssignmentCommentCreate, self).form_valid(form)

	def clean(self):
		try:
			qs = AssignmentComment.objects.filter(name=self.cleaned_data.get('result'))
			if self.instance.pk is not None:
				qs = qs.filter(~Q(pk=self.instance.pk))
				course = qs.get()
				if course>0 and course<100:
					self.instance.autocheck = True
		except AssignmentComment.DoesNotExist:
			course = None

	def get_success_url(self): 
		return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})





# class ItemCommentCreate(LoginRequiredMixin, generic.CreateView):
#     model = ItemComment
#     fields = ['description',]

#     def get_context_data(self, **kwargs):
#         context = super(ItemCommentCreate, self).get_context_data(**kwargs)
#         context['item'] = get_object_or_404(Item, pk = self.kwargs['pk'])
#         return context
        
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         form.instance.item=get_object_or_404(Item, pk = self.kwargs['pk'])
#         return super(ItemCommentCreate, self).form_valid(form)

#     def get_success_url(self): 
#         return reverse('item-detail', kwargs={'pk': self.kwargs['pk'],})








# # class CartCreate(LoginRequiredMixin,generic.CreateView):
# 	model=Cart
# 	fields=[]
# 	def get_context_data(self,**kwargs):
# 		context=super(CartCreate,self).get_context_data(**kwargs)
# 		context['product']=get_object_or_404(Item,pk=self.kwargs['pk'])
# 		context['user']=self.request.user
# 		return context
# 	def form_valid(self,form):
# 		form.instance.user=self.request.user
# 		form.instance.product=get_object_or_404(Item,pk=self.kwargs['pk'])
# 		return super(CartCreate,self).form_valid(form)
# 	def get_success_url(self):
# 		return reverse('item-detail',kwargs={'pk':self.kwargs['pk']})






class UserProfileListView(generic.ListView):
	model=UserProfile

class UserProfileDetailView(LoginRequiredMixin,generic.DetailView):
	model=UserProfile


def register(request):

	if request.method == 'POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts/login')
	else:
		form=RegistrationForm()
		args = {'form':form}
	return render(request,'reg_form.html', {'form':form})




def profile(request):
	args={"user":request.user}

	return render(request,'profile.html',args)


@login_required
def edit_profile(request):

	if request.method =='POST':
		form=EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/')

	else:
		form=EditProfileForm(instance=request.user)
		args={'forms':form}
		return render(request,'user_change.html', {'form':form})


@login_required
def edit_user_profile(request):
		if request.method =='POST':
			form=EditUserProfileForm(request.POST, instance=request.user.userprofile)
			if form.is_valid():
				form.save()
				return redirect('/')

		else:
			form=EditUserProfileForm(instance=request.user.userprofile)
			args={'forms':form}
			return render(request,'user_profile_change.html', {'form':form})








class AssignmentCreateView(LoginRequiredMixin,generic.CreateView):
	model=Assignment
	form_class=AssignmentForm
	template_name='blog_create.html'

	def form_valid(self,form):
		blog=form.save(commit=False)
		blog.author=UserProfile.objects.get(user=self.request.user)
		blog.save()
		return redirect('/')




class AssignmentUpdate(LoginRequiredMixin,generic.UpdateView):
	model=Assignment
	fields=['title','file_pdf']
	template_name_suffix='_update_form'





class AssignmentDelete(LoginRequiredMixin,generic.DeleteView):
	
	model=Assignment
	success_url=reverse_lazy('profile')