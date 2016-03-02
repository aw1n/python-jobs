from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from cities_light.models import City

from .models import Job, Category
from .forms import JobForm


class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'
    queryset = Job.objects.filter(published_at__isnull=False)

    def get_object(self):
        # Call the superclass
        object = super(JobDetailView, self).get_object()
        # Increment and save the number of views
        object.times_viewed += 1
        object.save()
        # Return the object
        return object


class PublishedListView(ListView):
    model = Job
    queryset = Job.objects.filter(published_at__isnull=False)

    def head(self, *args, **kwargs):
        last_published = self.get_queryset().latest('published_at')
        response = HttpResponse('')
        # RFC 1123 date format
        response['Last-Modified'] = last_published.published_at.strftime(
            '%a, %d %b %Y %H:%M:%S GMT'
        )
        return response

    def get_context_data(self, **kwargs):
        context = super(PublishedListView, self).get_context_data(**kwargs)
        context['titlepage'] = "Published"
        return context


class JobByCategoryListView(ListView):
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Job.objects.filter(
            category=self.category,
            published_at__isnull=False
        )

    def get_context_data(self, **kwargs):
        context = super(JobByCategoryListView, self).get_context_data(**kwargs)
        context['titlepage'] = "categorized as %s" % self.category
        return context


class JobByPlaceListView(ListView):
    def get_queryset(self):
        self.place = get_object_or_404(City, pk=self.args[0])
        return Job.objects.filter(
            place=self.place,
            published_at__isnull=False
        )

    def get_context_data(self, **kwargs):
        context = super(JobByPlaceListView, self).get_context_data(**kwargs)
        context['titlepage'] = "to work in %s" % self.place
        return context


class JobCreate(CreateView):
    form_class = JobForm
    template_name = 'jobpost_form.html'


class JobUpdate(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobpost_form.html'


class JobDelete(DeleteView):
    model = Job
    success_url = reverse_lazy('jobs-published')