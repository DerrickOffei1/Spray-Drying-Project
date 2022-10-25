from django.shortcuts import redirect, render
from .forms import DataForm
from .models import Database

# Create your views here.
def index(request):
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-results')
    else:
        form = DataForm()
    context = {
        "form":form
    }
    return render(request, 'dashboard/index.html', context)

def results(request):
    data = Database.objects.all().first()
    context = {
        "data": data
    }
    return render(request, 'dashboard/results.html', context)