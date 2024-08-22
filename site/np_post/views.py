from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .models import Post, Category
from .filters import PublicFilter
from .forms import PublicForm, SectionForm
from .consts import ARTICNEWS


class PublicList(ListView):
    model = Post
    ordering = '-date_creation'
    template_name = 'publics.html'
    context_object_name = 'publics'
    paginate_by = 10


class SectionsList(ListView):
    model = Category
    template_name = 'sections.html'
    content_type = 'sections'


class PublicDetail(DetailView):
    model = Post
    template_name = 'public_detail.html'
    context_object_name = 'public_detail'


class SectionDetail(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'section_detail.html'
    context_object_name = 'section_detail'


class SectionCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('np_post.add_category',)
    form_class = SectionForm
    model = Category
    template_name = 'section_edit.html'


class PublicUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('np_post.change_post',)
    login_url = '/sign/login/'
    form_class = PublicForm
    model = Post
    template_name = 'public_edit.html'


class SectionUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('np_post.change_category',)
    form_class = SectionForm
    model = Category
    template_name = 'section_edit.html'


class PublicDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('np_post.delete_post',)
    model = Post
    template_name = 'public_delete.html'
    success_url = reverse_lazy('home')


class SectionDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('np_post.delete_category',)
    model = Category
    template_name = 'section_delete.html'
    success_url = reverse_lazy('sections')


class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PublicFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsList(ListView):
    model = Post
    queryset = Post.objects.filter(publication_type=ARTICNEWS.NEWS)
    ordering = '-date_creation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 7


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('np_post.add_post',)
    form_class = PublicForm
    model = Post
    template_name = 'public_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.publication_type = ARTICNEWS.NEWS
        # form.send_email()
        return super().form_valid(form)


class ArticlesList(ListView):
    model = Post
    queryset = Post.objects.filter(publication_type=ARTICNEWS.ARTICLE)
    ordering = '-date_creation'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 7


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('np_post.add_post',)
    form_class = PublicForm
    model = Post
    template_name = 'public_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.publication_type = ARTICNEWS.ARTICLE
        return super().form_valid(form)

