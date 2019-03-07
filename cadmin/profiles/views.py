from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects_home')

    form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


