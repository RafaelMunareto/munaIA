from django.shortcuts import render
from ..forms import FileUploadForm

def index(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            # Processamento do script
           
            # Redirecionar ou processar conforme necessário
    else:
        form = FileUploadForm()

    return render(request, 'supervisionada/index.html', {'form': form})

def handle_uploaded_file(f):
    with open('algum_nome_arquivo', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
