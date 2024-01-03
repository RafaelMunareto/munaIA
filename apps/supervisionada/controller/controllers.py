from django import forms
from django.shortcuts import render
from django.conf import settings
from ..forms import FileUploadForm
from ..scripts.tratamento_variaveis import TratamentoVariaveis
import os
import apps.supervisionada.scripts.constantes as constantes
import pandas as pd

def index(request):
    processado = False
    print("Initial 'processado':", processado)  # Debugging print

    form = FileUploadForm()
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            custom_filename = form.cleaned_data.get('custom_filename') or file.name
            file_path = os.path.join(settings.BASE_DIR, 'base', custom_filename)
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            request.session['uploaded_file_name'] = custom_filename
            processado = True
            form = FileUploadForm() 
           
    else:
        form = FileUploadForm()
    return render(request, 'supervisionada/home/index.html', {'form': form, 'processado': processado})


def processar_base(request):
    filename = request.session.get('uploaded_file_name', constantes.variaveis_csv_file)  
    file_path = os.path.join(settings.BASE_DIR, 'base', filename)
    data_processor = TratamentoVariaveis(file_path)
    display_table(request, file_path)
    data_processor.capturaDados()  
    data_processor.salvarVariaveis(constantes.variaveis_dir)
    return render(request, 'supervisionada/home/processado.html', {'mensagem': 'Base Processada'})


def display_table(request, file_path):
   
    df = pd.read_csv(file_path)
    data_list = df.to_dict(orient='records')

    # Pass the data to the template
    context = {'data_list': data_list}
    
    return render(request, 'data_table.html', context)