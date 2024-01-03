from django.shortcuts import render
from ..forms import FileUploadForm
from ..scripts.tratamento_variaveis import TratamentoVariaveis


def index(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            processador = TratamentoVariaveis(file_path)
            processador.capturaDados()
    else:
        form = FileUploadForm()

    return render(request, 'supervisionada/index.html', {'form': form})

def handle_uploaded_file(f):
    file_path = 'algum_nome_arquivo'
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path
