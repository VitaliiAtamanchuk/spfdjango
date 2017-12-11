import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from spfblog.models import Entry


def blog_index(request):
    return render(request,
                  'spfblog/main.html',
                  {'entries': Entry.objects.all()}
                  )


def article_index(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    json_response = render_to_string(
        'spfblog/spf_article.json',
        {'entry': entry}).replace("\n", "\\n")
    print(json_response)
    json_resp = json.loads(json_response)
    print(json_resp)
    if request.GET.get('spf'):
        json_response = render_to_string(
            'spfblog/spf_article.json',
            {'entry': entry}).replace("\r\n", "\\n")
        str_resp = str(json_response)
        print(str_resp)
        json_resp = json.loads(str_resp)
        return JsonResponse(json_resp)
        return JsonResponse({
            'title': 'SPF Page',
            'body': {
                'content': '<h1>' + entry.headline + '</h1>' + \
                           '<p class="help-text">' + entry.body + '</p>'
            }
        })
    else:
        return redirect('blog:index')