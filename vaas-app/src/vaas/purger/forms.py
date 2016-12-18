from django import forms
from django.core.validators import URLValidator
from vaas.cluster.models import LogicalCluster


class PurgeForm(forms.Form):
    url = forms.CharField(label='Url to purge', max_length=100, validators=[URLValidator()])
    cluster = forms.ChoiceField(label='Varnish cluster', choices=[])

    def __init__(self, *args, **kwargs):
        super(PurgeForm, self).__init__(*args, **kwargs)
        self.fields['cluster'].choices = [(cluster.id, cluster.name) for cluster in LogicalCluster.objects.all()]