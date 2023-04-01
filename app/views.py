from django.shortcuts import render
from app.models import contact_message

# home Page
def home_view(request):
    return render(request, 'testapp/index.html')

#about page
def about_view(request):
    return render(request, 'testapp/about.html')

# contact page
def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        en = contact_message(name=name, email=email, subject=subject, message=message)
        en.save()
    return render(request, 'testapp/contact.html')


# service page
def service_view(request):
    return render(request, 'testapp/service.html')

