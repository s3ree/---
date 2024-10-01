from django.shortcuts import render, redirect
from .forms import UserProfileForm, BookingForm
from .models import Booking

def personal_info(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # Log form data and user creation
            print("Personal Info form is valid")
            request.session['personal_info'] = form.cleaned_data
            user = form.save()
            request.session['user_id'] = user.id
            print(request.session.get('user_id'))
            print("User ID saved in session:", user.id)
            return redirect('book_kitchen')
        else:
            print("Personal Info form is invalid", form.errors)  # Log form errors
    else:
        print("Rendering Personal Info form")
        form = UserProfileForm()
    
    return render(request, 'personal_info.html', {'form': form})

def book_kitchen(request):
    user_id = request.session.get('user_id')
    
    # Check if session contains the user_id
    if not user_id:
        print("No user ID in session, redirecting to personal_info")
        return redirect('personal_info')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user_id = user_id
            booking.save()
            print(request.session.items())
            print("Booking saved successfully for user:", user_id)
            return redirect('success')  # Redirect to success page
        else:
            print("Booking form is invalid", form.errors)  # Log form errors
    else:
        print("Rendering Booking form")
        form = BookingForm()
    
    return render(request, 'book_kitchen.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')

def home(request):
    return render(request, 'home.html')

def user_bookings(request):
    user_id = request.session.get('user_id')
    if user_id:
        bookings = Booking.objects.filter(user_id=user_id)
        return render(request, 'user_bookings.html', {'bookings': bookings})
    else:
        return redirect('personal_info') 

