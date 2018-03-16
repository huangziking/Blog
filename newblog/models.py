from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    '''
    Djiango 要求必须继承models.Model类
    Category 只用指定一个分类名name
    CharField指定其数据类型为字符型,max_length为字符最大长度
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    '''
    Tag 标签
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):

    '''
    title: 标题,charfield  body:文章正文,textField
    creat_time:创建时间,DateTimeField
    modified_time:最后修改时间，datetimefield
    excerpt:文章摘要，charfield blank=true允许该值为空
    '''
    title = models.CharField(max_length=70)

    body = models.TextField()

    creat_time = models.DateTimeField()

    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200,blank=True)

    '''
    分类和标签：一篇文章只有一个分类，一个分类可以有多篇文章所以使用一对多foreignkey
    一篇文章可以有多个标签，一个标签可以有多篇文章所以用多对多 manytomanyfield,且文章可以没有标签blank=True
    '''

    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag,blank=True)
    '''
    User从django.contrib.auth.model模块导入
    django.contrib.auth是Django内置应用，用于处理网站用户的注册登录等流程
    User是django的用户模型
    一篇文章只能有一个作者，一个作者可以有多个文章即为一对多foreignKey
    '''
    auther = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title