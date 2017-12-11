from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from spfblog.models import Entry


def blog_index(request):
    return render(request,
                  'home_page.html',
                  {'entries': Entry.objects.all()}
                  )


def article_index(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.GET.get('spf'):
        return JsonResponse({
            'title': 'SPF Page',
            'body': {
                'content': '<h1>' + entry.headline + '</h1>' + \
                            '<p class="help-text">' + entry.body + '</p>'
            }

        })
    else:
        return redirect('blog:index')