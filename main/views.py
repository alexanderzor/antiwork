from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from forms import FeedBackForm, CommentForm, SearchForm
from django.core.urlresolvers import reverse
from models import Company, New, NewsComment, Feedback, FeedbackComment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def feedback(request):
    if request.method == 'POST':
        form = FeedBackForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = FeedBackForm()
    context = {'form': form}
    return render(request, 'feedback.html', context)



def news(request):
    news_list = New.objects.all()
    paginator = Paginator(news_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)
    context = {'news': news}
    return render(request, 'news.html', context)

def new(request, key):
    new = New.objects.get(id=key)
    comments = NewsComment.objects.filter(parent=new).all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = NewsComment.objects.create(author=form.cleaned_data['name'],
                                                 content=form.cleaned_data['content'],
                                                 parent=new,
                                                 )
            comment.save()
            return HttpResponseRedirect(reverse('new', args=key))
    else:
        form = CommentForm()
    context = {'new': new, 'form': form, 'comments': comments, 'key': key}
    return render(request, 'new.html', context)


def index(request):
    feedback_list = Feedback.objects.filter(active=True).all()
    paginator = Paginator(feedback_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        feedbacks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        feedbacks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        feedbacks = paginator.page(paginator.num_pages)
    search_form = SearchForm()
    context = {'feedbacks': feedbacks, 'search_form': search_form}
    return render(request, 'index.html', context)


def review(request, key):
    feedback = Feedback.objects.get(id=key)
    comments = feedback.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = FeedbackComment.objects.create(author=form.cleaned_data['name'],
                                                     content=form.cleaned_data['content'],
                                                     parent=feedback,
                                                     )
            comment.save()
            return HttpResponseRedirect(reverse('review', args=key))
    else:
        form = CommentForm()
    context = {'feedback': feedback, 'comments': comments, 'form': form}
    return render(request, 'review.html', context)


def search(request):
    feedbacks = []
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            cd = search_form.cleaned_data
            key = unicode(cd['keyword'])
            feedbacks = Feedback.objects.filter(active=True, keywords__icontains=key)


    else:
        search_form = SearchForm()
    context = {'feedbacks': feedbacks}
    return render(request, 'index.html', context)
