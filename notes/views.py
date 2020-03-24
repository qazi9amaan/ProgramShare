from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import LabPost
import os
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings

# Create your views here.


class index(ListView):
    model = LabPost
    template_name = 'notes/index.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]
    paginate_by = 6


def about(request):
    return render(request, "notes/about.html")


class fullpost(DetailView):
    model = LabPost


class PostCreateView(CreateView):  # LoginRequiredMixin,
    model = LabPost
    fields = [

        "title",
        "description",
        "semester",
        "stream",
        "subject",
        
        "language",
        "file",
        "postbody",

    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def post_feed(request):
        form_class = FeedForm
        if request.method == 'POST':
            form = form_class(request.POST,request.FILES)
            if form.is_valid():
                feed = form.save(commit=False)
                feed.user = User.objects.get(pk=1)
                feed.pub_date=timezone.now()
                #instance = Feed(files=request.FILES['files'])
            # feed.files=request.FILES['files']
                feed.save()
                return redirect('home')
        else:
            form = form_class()
            return render(request, 'post_feed.html', {'form': form,})

from django.views.generic.edit import FormView
from .forms import FeedForm

class FileFieldView(FormView):
    form_class=FeedForm
    template_name='post_feed.html'
 '''success_url=???   #I dont know what to write here.I thought of putting this
render(request, 'post_feed.html', {'form': form,}) because I just want 
to reload the page but it gave an error,so I removed it entirely.'''

    def post_feed(self,request,*args,**kwargs):
        form_class=self.get_form_class()
        form=self.get_form(form_class)
        filez=request.FILES.getlist('files')
        if form.is_valid():
            for f in filez:
                f.save()
            return self.form_valid(form)     
        else:
            return self.form_invalid(form) 

