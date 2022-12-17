from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
# from django.shortcuts import render
# from django.db.models import Q
# from django.db import LoginRequiredMixin

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    
    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:1]
        context['all_stories'] = NewsStory.objects.all()
        return context

class StoryView(generic.DetailView):
    model               = NewsStory
    template_name       = "news/story.html"
    context_object_name = "story"
    

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = "storyForm"
    template_name = "news/createStory.html"
    success_url = reverse_lazy("news:index")


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# class StoryEditView(generic.UpdateView):
#     model=NewsStory
#     # form_class = StoryForm
#     fields = ["title", 'pub_date', 'content']

#     def get_success_url(self) -> str:
#             return reverse_lazy('news:story', kwargs={'pk':self.kwargs['pk']})

#     def get_queryset(self):
#         qs = super().get_queryset()
#         if not self.request.user.is_authenticated:
#             raise qs.model.DoesNotExist

#         qs = qs.filter(author=self.request.user)
#         return qs
    
# class StoryDeleteView(LoginRequiredMixin, generic.DeleteView):
#     models=NewsStory
#     success_url = reverse_lazy('news:index')

#     def get_queryset(self):
#         """filter to pnly allow delete of own stories"""
#         qs = super().get_queryset()
#         return qs.filter(author=self.request.user)

