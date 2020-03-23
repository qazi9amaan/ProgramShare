from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.core.files import File

# Create your models here.


class LabPost(models.Model):

    title = models.CharField(max_length=100)
    subject = models.CharField(default="abcd", max_length=100)
    file = models.FileField(null=True,upload_to='files/',blank=True)

    STREAM = (
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('EEE', 'EEE'),
        ('MECH', 'MECH'),
        ('CV', 'CV'),
        ('BCA', 'BCA'),
        ('BBA', 'BBA'),
        ('MCA', 'MCA'),
        ('MBA', 'MBA'),
        ('LLB', 'LLB'),
        ('LLM', 'LLM'),
        ('B-ARCH', 'B-ARCH'),
        ('BBA-HEM', 'BBA-HEM'),
        ('B-DES', 'B-DES'),
    )

    stream = models.CharField(
        default='CSE', max_length=30, choices=STREAM)

    SEMESTER = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
    )
    semester = models.IntegerField(default=1, choices=SEMESTER)
    description = models.TextField(blank=True, max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    CHOICES = (
        ('plaintext', 'plaintext'),
        ('language-c', 'C'),
        ('language-csharp', 'C#'),
        ('language-cpp', 'C++'),
        ('language-python', 'Python'),
        ('language-java', 'Java'),
        ('language-javascript', 'JavaScript'),
        ('language-kotlin', 'Kotlin'),
        ('language-html,', 'HTML,'),
        ('language-css', 'CSS'),
        ('language-php7', 'PHP7'),
        ('language-xml', 'XML'),
        ('language-makefile', 'Makefile'),
        ('language-objective-c', 'Objective-C'),
        ('language-sql', 'SQL'),
        ('language-perl', 'Perl'),
        ('language-shell', 'Shell'),
        ('language-apache', 'Apache'),
        ('language-bash', 'Bash'),
        ('language-coffeescript', 'CoffeeScript'),
        ('language-diff', 'Diff'),
        ('language-go', 'Go'),
        ('language-http', 'HTTP'),
        ('language-json', 'JSON'),
        ('language-lesslua', 'LessLua'),
        ('language-markdown', 'Markdown'),
        ('language-ruby', 'Ruby'),
        ('language-rust', 'Rust'),
        ('language-scss', 'SCSS'),
        ('language-swift', 'Swift'),
        ('language-ini', 'INI'),
        ('language-typescript', 'TypeScript'),
        ('language-yaml', 'YAML'),
    )

    language = models.CharField(
        default='plaintext', max_length=30, choices=CHOICES)
    postbody = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.title
        

    def get_absolute_url(self):
        return reverse('full_post', kwargs={'pk': self.pk})