from django.db import models


class Category(models.Model):
    class Meta:
        db_table = 'my_category'

    name = models.CharField(max_length=20, null=False)
    desc = models.CharField(max_length=256, null=False)


class Article(models.Model):
    class Meta:
        db_table = 'my_article'

    title = models.CharField(max_length=20, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.CharField(max_length=256, null=False)




