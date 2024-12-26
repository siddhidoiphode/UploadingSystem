from django.shortcuts import render, redirect
from .forms import UploadContentForm
from .models import UploadedContent

def upload_content(request):
    if request.method == 'POST':
        form = UploadContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_content')
    else:
        form = UploadContentForm()
    uploaded_contents = UploadedContent.objects.all()
    return render(request, 'uploader/upload_content.html', {
        'form': form,
        'uploaded_contents': uploaded_contents,
    })
