from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Property, UserPreference
from django.contrib.auth import logout
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from .forms import PropertyForm

@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.save()
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm()
    return render(request, 'properties/add_property.html', {'form': form})

def home(request):
    return render(request, 'properties/home.html')

@login_required
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})

@login_required
def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'properties/property_detail.html', {'property': property})

@login_required
def recommended_properties(request):
    try:
        user_pref = UserPreference.objects.get(user=request.user)
        recommended = Property.objects.filter(
            Q(price__gte=user_pref.preferred_price_min) &
            Q(price__lte=user_pref.preferred_price_max) &
            Q(bedrooms=user_pref.preferred_bedrooms) &
            Q(bathrooms=user_pref.preferred_bathrooms)
        )
    except UserPreference.DoesNotExist:
        recommended = Property.objects.all()[:5] 
    
    return render(request, 'properties/recommended.html', {'properties': recommended})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')
