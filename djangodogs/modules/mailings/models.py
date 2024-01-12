from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from django.urls import reverse
# from config_reader import config
# import mysql.connector
# from mysql.connector import errorcode



User = get_user_model()


class Announcement(models.Model):
    """
    Модель постов для объявления
    """    

    STATUS_OPTIONS = (
        ('published', 'Опубликовано'), 
        ('draft', 'Черновик')
    )

    title = models.CharField(verbose_name='Заголовок', max_length=255)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    short_description = models.TextField(verbose_name='Краткое описание', max_length=500)
    full_description = models.TextField(verbose_name='Текст объявления')
    thumbnail = models.ImageField(
        verbose_name='Превью поста', 
        blank=True, 
        upload_to='images/thumbnails/%Y/%m/%d/', 
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))]
    )
    status = models.CharField(choices=STATUS_OPTIONS, default='published', verbose_name='Статус поста', max_length=10)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    author = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_DEFAULT, related_name='author_posts', default=1)
    updater = models.ForeignKey(to=User, verbose_name='Обновил', on_delete=models.SET_NULL, null=True, related_name='updater_posts', blank=True)
    fixed = models.BooleanField(verbose_name='Зафиксировано', default=False)

    class Meta:
        db_table = 'app_articles'
        ordering = ['-fixed', '-time_create']
        indexes = [models.Index(fields=['-fixed', '-time_create', 'status'])]
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('announcements_detail', kwargs={'slug': self.slug}) 
    
    
class BotTable(models.Model):
    users_agree = models.CharField(max_length=10, blank=True, null=True)
    first_question = models.IntegerField(blank=True, null=True)
    second_question = models.IntegerField(blank=True, null=True)
    third_question = models.IntegerField(blank=True, null=True)
    fourth_question = models.IntegerField(blank=True, null=True)
    fifth_question = models.IntegerField(blank=True, null=True)
    sixth_question = models.IntegerField(blank=True, null=True)
    seventh_question = models.IntegerField(blank=True, null=True)
    eight_question = models.IntegerField(blank=True, null=True)
    chat_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'bot_table'
    
    # def telegram_bot_sendtext(self):
    #     bot_token = token=config.bot_token.get_secret_value()
    #     # DB CONNECT
    #     try:
    #         db = mysql.connector.connect(
    #         host=host,
    #         user=user,
    #         passwd=password,
    #         database=db_name
    #     )
    #     except mysql.connector.Error as err:
    #         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #             print("Что-то не так с вашим именем пользователя или паролем")
    #         elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #             print("База данных не существует")
    #         else:
    #             print(err)
    #     cursor = db.cursor()
    #     bot_chatID = DATABASES
        
