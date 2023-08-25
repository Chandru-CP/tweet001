from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ChangeUsernameForm, ChangeEmailForm, ChangeProfilePictureForm, ChangeMobileNumberForm
from .models import UserProfile


@login_required
def settings_view(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        username_form = ChangeUsernameForm(request.POST, instance=user)
        email_form = ChangeEmailForm(request.POST, instance=user)
        profile_picture_form = ChangeProfilePictureForm(request.POST, request.FILES, instance=user_profile)
        mobile_number_form = ChangeMobileNumberForm(request.POST, instance=user_profile)

        if (username_form.is_valid() and email_form.is_valid() and profile_picture_form.is_valid()
                and mobile_number_form.is_valid()):
            username_form.save()
            email_form.save()
            profile_picture_form.save()
            mobile_number_form.save()
            messages.success(request, 'Settings updated successfully.')
            return render(request, 'django_setting/setting.html')
    else:
        username_form = ChangeUsernameForm(instance=user)
        email_form = ChangeEmailForm(instance=user)
        profile_picture_form = ChangeProfilePictureForm(instance=user_profile)
        mobile_number_form = ChangeMobileNumberForm(instance=user_profile)

    return render(
        request,
        'django_setting/settings.html',
        {
            'username_form': username_form,
            'email_form': email_form,
            'profile_picture_form': profile_picture_form,
            'mobile_number_form': mobile_number_form,
        }
    )
