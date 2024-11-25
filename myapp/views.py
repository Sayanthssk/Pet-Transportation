from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib import messages

from .form import *

from .models import *

# Create your views here.

# class SessionCheckMixin:
#     """Mixin to check session values and redirect if not set."""
    
#     session_key = 'userid'  # Change this to the key you're storing in the session
    
#     def dispatch(self, request, *args, **kwargs):
#         if not request.session.get(self.session_key):
#             messages.warning(request, "Please log in to access this page.")
#             return redirect('login')  # Replace 'login' with your login URL name
#         return super().dispatch(request, *args, **kwargs)
    

class Viewuser(View):
    def get(self, request):
        c = User_model.objects.all()
        return render(request, 'Viewuser.html', { 's':c })
    

class Viewservice(View):
    def get(self, request):
        c = Diver_model.objects.all()
        return render(request, 'ViewServiceProvider.html', { 's':c })
    
class Viewcomplaint(View):
    def get(self, request):
        c = Complaint_model.objects.all()
        return render(request, 'Viewcomplaint.html', { 's':c })
    

class Reply(View):
    def get(self, request, pk):
        feedback = get_object_or_404(Complaint_model, pk = pk)
        print(feedback)
        return render(request, 'reply.html', {'feedback': feedback})
    
    def post(self, request, pk):
        
        feedback = get_object_or_404(Complaint_model, pk = pk)
        form = Reply_form(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('viewcomplaint')
        
class Feedview(View):
    def get(self, request):
        c = Feedback_model.objects.all()
        return render(request, 'viewFeedback.html', { 's':c })
    
class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            obj = Login_model.objects.get(username = username, password = password)
            request.session['userid'] = obj.id
            if obj.type == 'admin':
                return redirect('admindash')
            elif obj.type == 'user':
                return render(request, 'userdash.html')
            elif obj.type == 'serviceprovider':
                return render(request, 'serviceproviderdash.html')
            else:
                return HttpResponse('Invalid credentials')

        except Login_model.DoesNotExist:
            messages.error(request, "invalid username or password")
            return redirect('login')
        
class Logout(View):
    def get(self, request):
        request.session.flush()
        return redirect('login')
        
class Admin_dash(View):
    def get(self, request):
        return render(request, 'Admindash.html')