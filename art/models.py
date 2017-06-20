from django.db import models
from markdown import markdown
from tagging.fields import TagField
from tagging.registry import register
import datetime, tagging, os

class Art(models.Model):
    """
    Class defining art work model
    """

    def get_upload_path_high(instance, filename):
        return os.path.join(instance.art_type.category, "high", filename)

    def get_upload_path_low(instance, filename):
        return os.path.join(instance.art_type.category, "low", filename)

    title = models.CharField(max_length=250, help_text=u'Max 250 characters')
    slug = models.SlugField(unique=True, help_text=u'Suggested value automatically generated from title. Must be unique.')
    body = models.TextField()
    body_html = models.TextField(editable=False, blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    art_type = models.ForeignKey('Art_Category', on_delete=models.CASCADE)
    tags = TagField(help_text=u'Seperate tags with spaces.')
    url = models.URLField('URL', null=True, blank=True)
    image_highres = models.ImageField(upload_to=get_upload_path_high, null=True, blank=True)
    image_lowres = models.ImageField(upload_to=get_upload_path_low, null=True, blank=True)
    client_name = models.CharField(max_length=250, help_text=u'Max 250 characters', blank=True, null=True)

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        super(Art, self).save(force_insert, force_update)

    def low_res_image_tag(self):
        return markdown('<img src="/%s/%s/%s" width="30%" height="30%" />' % (self.art_type, "low", self.image_lowres))

    def high_res_image_tag(self):
        return markdown('<img src="/%s/%s/%s" width="70%" height="70%" />' % (self.art_type, "high", self.image_highres))

    @models.permalink
    def get_absolute_url(self):
        return ('art_detail_page', (), { 'slug': self.slug })

register(Art, tag_descriptor_attr='atags')


class Art_Category(models.Model):
    """
    Class defining art types
    """
    category = models.CharField(max_length=100, help_text=u'Max 100 characters')
    slug = models.SlugField(unique=True, help_text=u'Suggested value automatically generated from title. Must be unique.')

    class Meta:
        verbose_name = "Art Category"
        verbose_name_plural = "Art Categories"
        ordering = ['category']

    def __unicode__(self):
        return self.category

    def __str__(self):
        return self.category

class Art_Url(models.Model):
    body = models.TextField()
    body_html = models.TextField(editable=False, blank=True)
    url = models.URLField('URL', null=True, blank=True)
    art = models.ForeignKey('Art', on_delete=models.CASCADE)
    sequence = models.IntegerField()

    class Meta:
        ordering = ['sequence']

    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        super(Art_Url, self).save(force_insert, force_update)