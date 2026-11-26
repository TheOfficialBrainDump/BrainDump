from django.shortcuts import render, get_object_or_404
from .models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfileUpdateForm

def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)

    return render(request, 'accounts/profile.html', {
        'profile_user': profile_user,
    })

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)

    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {
        'form': form,
    })
