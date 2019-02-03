from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from crud.models import Empdtls
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from django.views import generic
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

# TemplateView displays the template in template_name
class AboutView(TemplateView):
    template_name = 'crud/login.html'

# This class checks whether the credentials are authenticated or not
class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:

                return HttpResponseRedirect('/empdetails/')
            
        else:
            return HttpResponse('user not registered')


# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return HttpResponseRedirect(settings.LOGIN_URL)

# Displays login form by clicking logout button
class LogoutView(TemplateView):
    template_name = 'crud/login.html'

# Displays list of all empdetails
class crudListView(ListView):
    model = Empdtls
    context_object_name='data'

# Displays empdetails
class crudDetailView(DetailView):
	model = Empdtls
	context_object_name = 'obj'

# Adds a new employee details
class EmpdtlsCreate(CreateView):
    model = Empdtls
    success_url = reverse_lazy('crud_List')
    fields = ['firstname','lastname','emp_id','mail_id','contact_no','gender']
    
# Edit the existing employee details
class EmpdtlsUpdate(UpdateView):
    model = Empdtls
    success_url = reverse_lazy('crud_List')
    fields = ['firstname','lastname','mail_id','contact_no','gender']

# Deletes the employee
class EmpdtlsDelete(DeleteView):
    model = Empdtls
    success_url = reverse_lazy('crud_List')

# class recentDetailView(DetailView):
#     model = Empdtls
#     template_name = "recent_emp.html"
#     pk_url_kwarg = "pk"
    #obj = Empdtls.objects.latest('id')
    #context_object_name = 'obj'
    #template_name = 'crud/recent_emp.html'
    #fields = ['firstname','lastname','mail_id','contact_no','gender']

    #obj = Empdtls.objects.latest('pk')    

# class EmpdtlsListView(generic.ListView):
#     model = Empdtls

#     def get_queryset(self):
#         return Book.objects.filter('pk')[:1]
	

class EmpdtlsList(ListView):
    model = Empdtls
    context_object_name = 'obj'   # your own name for the list as a template variable
    queryset = Empdtls.objects.latest('emp_id') # Get 5 books containing the title war
    template_name = 'crud/recent_emp.html'    