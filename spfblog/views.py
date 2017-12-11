from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from spfblog.models import Entry


def blog_index(request):
    return SPFResponse(
        request,
        'spfblog/index.html',
        {'entries': Entry.objects.all()},
        'spfblog/spf_index.json'
    )


def article_index(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return SPFResponse(
        request,
        'spfblog/entry.html',
        {'entry': entry},
        'spfblog/spf_article.json'
    )


def SPFResponse(request, template_name, data, json_tempalte_name):
    if request.GET.get('spf'):
        str_response = render_to_string(
            json_tempalte_name,
            data
        ).encode('utf-8')
        return HttpResponse(str_response, content_type='application/json')
    else:
        return render(request, template_name, data)
