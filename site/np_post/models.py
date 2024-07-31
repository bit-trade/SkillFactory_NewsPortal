from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from .consts import RATING, ARTICNEWS


class Author(models.Model):
    full_name = models.CharField(max_length=50)
    rating = models.IntegerField(default=RATING['default'], choices=RATING)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        summ_rating_posts = 0
        for post in self.Posts.all():
            summ_rating_posts += post.rating

        summ_rating_comments = 0
        for comment in self.user.Comments.all():
            summ_rating_comments += comment.rating

        summ_rating_users_comments = 0
        for post in self.Posts.all():
            for comment in post.comment_set.all():
                summ_rating_users_comments += comment.rating

        self.rating = summ_rating_posts * 3 + summ_rating_comments + (summ_rating_users_comments - summ_rating_comments)
        self.save()

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name_cat = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name_cat.title()


class Post(models.Model):
    title = models.CharField(max_length=170)
    text_post = models.TextField()
    rating = models.IntegerField(default=RATING['default'], choices=RATING)
    date_creation = models.DateTimeField(auto_now_add=True)
    publication_type = models.CharField(max_length=8, default=ARTICNEWS['news'], choices=ARTICNEWS)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, related_name='Posts')
    category = models.ManyToManyField(Category)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text_post[:124]}...'

    def __str__(self):
        return f'<h2>{self.title.title()}<h2>\n\n{self.text_post}'

    def get_absolute_url(self):
        return reverse('public_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text_comm = models.TextField()
    data_add_comm = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=RATING['default'], choices=RATING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Comments')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return self.text_comm[:80]

