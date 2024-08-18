from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from np_post.models import Category


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        cat_dict = list(Category.objects.values())
        for i, j in zip(range(0, Category.objects.count()), range(1, Category.objects.count() + 1)):
            if Category.objects.filter(user=self.request.user.id, id=j):
                cat_dict[i]['subscribed'] = True
            else:
                cat_dict[i]['subscribed'] = False

        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        context['sections'] = cat_dict
        return context
