from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect

from vaas.cluster.cluster import ServerExtractor
from vaas.cluster.models import LogicalCluster
from .forms import PurgeForm
from vaas.purger.purger import VarnishPurger


def purge_view(request):
    PurgeForm
    if request.method == 'POST':
        form = PurgeForm(request.POST)
        if form.is_valid():
            cluster = LogicalCluster.objects.get(pk=form.cleaned_data['cluster'])
            servers = ServerExtractor().extract_servers_by_clusters([cluster])
            result = VarnishPurger().purge_url(form.cleaned_data['url'], servers)
            messages.warning(
                request,
                'Url {} purged from cluster {} - cleaned {} server(s), errors occurred for {} server(s)'.format(
                    form.cleaned_data['url'], cluster.name, len(result['success']), len(result['error'])
                )
            )
            return HttpResponseRedirect('/')
    else:
        form = PurgeForm()

    return render(request, 'purge_form.html', {'form': form})
