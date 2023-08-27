from django import forms


class CSVForm(forms.Form):
    csv_file = forms.FileField(label="CSV File")