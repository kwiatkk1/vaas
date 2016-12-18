# -*- coding: utf-8 -*-

from django.forms import ModelForm
from vaas.cluster.models import LogicalCluster, Dc, VclTemplate, VarnishServer, VclTemplateBlock


class LogicalCLusterModelForm(ModelForm):
    class Meta:
        model = LogicalCluster
        fields = '__all__'


class DcModelForm(ModelForm):
    class Meta:
        model = Dc
        fields = '__all__'


class VclTemplateModelForm(ModelForm):
    class Meta:
        model = VclTemplate
        fields = '__all__'


class VarnishServerModelForm(ModelForm):
    class Meta:
        model = VarnishServer
        fields = '__all__'


class VclTemplateBlockModelForm(ModelForm):
    class Meta:
        model = VclTemplateBlock
        fields = '__all__'
