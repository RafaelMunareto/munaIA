from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField()

class FileUploadForm(forms.Form):
    file = forms.FileField()
    custom_filename = forms.CharField(required=False, label='Custom Filename')

    def clean_file(self):
        file = self.cleaned_data['file']
        extension = file.name.split('.')[-1].lower()
        if extension not in ['csv', 'txt']:
            raise forms.ValidationError("Unsupported file extension. Only CSV and TXT files are allowed.")
        return file

    def clean(self):
        cleaned_data = super().clean()
        file = cleaned_data.get('file')
        custom_filename = cleaned_data.get('custom_filename')
        
        if custom_filename:
            extension = file.name.split('.')[-1].lower()
            cleaned_data['custom_filename'] = f"{custom_filename}.{extension}"
        
        return cleaned_data