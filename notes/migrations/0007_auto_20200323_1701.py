# Generated by Django 3.0.4 on 2020-03-23 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20200323_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='labpost',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='labpost',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='labpost',
            name='language',
            field=models.CharField(choices=[('plaintext', 'plaintext'), ('language-c', 'C'), ('language-csharp', 'C#'), ('language-cpp', 'C++'), ('language-python', 'Python'), ('language-java', 'Java'), ('language-javascript', 'JavaScript'), ('language-kotlin', 'Kotlin'), ('language-html,', 'HTML,'), ('language-css', 'CSS'), ('language-php7', 'PHP7'), ('language-xml', 'XML'), ('language-makefile', 'Makefile'), ('language-objective-c', 'Objective-C'), ('language-sql', 'SQL'), ('language-perl', 'Perl'), ('language-shell', 'Shell'), ('language-apache', 'Apache'), ('language-bash', 'Bash'), ('language-coffeescript', 'CoffeeScript'), ('language-diff', 'Diff'), ('language-go', 'Go'), ('language-http', 'HTTP'), ('language-json', 'JSON'), ('language-lesslua', 'LessLua'), ('language-markdown', 'Markdown'), ('language-ruby', 'Ruby'), ('language-rust', 'Rust'), ('language-scss', 'SCSS'), ('language-swift', 'Swift'), ('language-ini', 'INI'), ('language-typescript', 'TypeScript'), ('language-yaml', 'YAML')], default='plaintext', max_length=30),
        ),
        migrations.AlterField(
            model_name='labpost',
            name='postbody',
            field=models.TextField(),
        ),
    ]
