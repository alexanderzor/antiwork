from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from forms import FeedBackForm, CommentForm, SearchForm
from django.core.urlresolvers import reverse
from models import Company, New, Comment


# Create your views here.
def feedback(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = FeedBackForm()
    context = {'form': form}
    return render(request, 'feedback.html', context)



def news(request):
    new = New.objects.all()
    context = {'news': new}
    return render(request, 'news.html', context)

def new(request, key):
    new = New.objects.get(id=key)
    comments = Comment.objects.filter(parent=new).all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment.objects.create(author=form.cleaned_data['name'],
                                             content=form.cleaned_data['content'],
                                             parent=New.objects.filter(id=key).first()
                                             )
            comment.save()
            return HttpResponseRedirect(reverse('new', args=key))
    else:
        form = CommentForm()
    context = {'new': new, 'form': form, 'comments': comments, 'key': key}
    return render(request, 'new.html', context)


def index(request):
    companies = Company.objects.all()
    search_form = SearchForm()
    context = {'companies': companies, 'search_form': search_form}
    return render(request, 'index.html', context)


def review(request, key):
    company = Company.objects.get(id=key)
    feedbacks = company.feedbacks.all()
    context = {'company': company, 'feedbacks': feedbacks}
    return render(request, 'review.html', context)


def search(request):
    companies = []
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            cd = search_form.cleaned_data
            key = unicode(cd['keyword'])
            companies = Company.objects.filter(keywords__icontains=key)


    else:
        search_form = SearchForm()
    context = {'companies': companies}
    return render(request, 'index.html', context)
