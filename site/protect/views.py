# from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from np_post.models import Category


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        context['sections'] = Category.objects.all()
        context['subs'] = Category.objects.filter(user=self.request.user.id, id=2)
        context['slovar'] = {
            'Category': {
                'id_cat': 8,
                'name_cat': 'Category',
                'description': 'Bla Bla Bla Bla La La',
                'subscribed': True
            }
        }
        return context


# def dictgen():
#     user = User.objects.get(pk=1)
#     keys = ['id', 'name', 'description', 'subs']
#     values = []
#     for v in Category.objects.all():
#         values.append(v.id)
#         values.append(v.name_cat)
#         values.append(v.description)
#         for subs in Category.objects.filter(user=user.id):
#             if subs.name_cat == v.name_cat:
#                 values.append(True)
#
#     d = {k: v for k, v in zip(keys, values)}
#     dict_variable = {key:value for (key,value) in d.items()}

