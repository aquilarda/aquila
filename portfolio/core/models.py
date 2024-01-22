from django.db import models

class About(models.Model):
    about_me = models.TextField("Hakkimda Yazisi")

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = "aboutme"

    def __str__(self):
        return self.about_me

class Project(models.Model):
    project_title = models.CharField("Proje Basligi", max_length=100)
    project_description = models.TextField("Proje aciklama")

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"

    def __str__(self):
        return self.project_title

class Blog(models.Model):
    blog_title = models.CharField("Blog Baslik", max_length=500)
    blog_description = models.TextField("Blog yazi")
    blog_url = models.URLField("Blog link")

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"

    def __str__(self):
        return self.blog_title
