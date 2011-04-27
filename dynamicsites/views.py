from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import Site
from django.conf import settings

def site_info(request):
    if request.method != 'GET':
        raise Http404
    site = None
    if settings.SITE_ID:
        site = Site.objects.get_current()
    args = {
        'site':site
    }
    return render_to_response('dynamicsites/site_info.html', args,
        context_instance=RequestContext(request))