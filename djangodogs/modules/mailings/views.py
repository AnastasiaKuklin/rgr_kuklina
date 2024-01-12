from django.views.generic import ListView, DetailView
from .models import Announcement
from django.views.decorators.csrf import csrf_exempt
from .models import BotTable, Announcement
import requests
from django.http import HttpResponse


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'mailings/announcements_list.html'
    context_object_name = 'announcements'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
    
    # @csrf_exempt 
    # def send_message(request):
    #     if request.method == 'POST':                         
    #         # message = request.POST.get('message', '')  # получаем сообщение
    #         message = Announcement.full_description  # получаем сообщение
    #         subscribers = BotTable.objects.filter(users_agree='да')
    #         bot_token = '6363160747:AAGyssU1JFJQxBF_uzRYFHNknPmCZ8TD-WY' 

    #         for i in subscribers:
    #             url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    #             data = {'chat_id': i.chat_id, 'text': message}
    #             requests.post(url, data=data)

    #         return HttpResponse('Сообщение отправлено.')
    #     else:
    #         return HttpResponse('Ошибка', status=400)

    
class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'mailings/announcements_detail.html'
    context_object_name = 'announcement'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context
    
    @csrf_exempt 
    def send_message(request): # delete kwargs
        if request.method == 'POST':                
            # message = request.POST.get('message', '')  # получаем сообщение
            message = Announcement.objects.raw("SELECT id, full_description FROM app_articles") # получаем сообщение, Announcement.full_description
            subscribers = BotTable.objects.filter(users_agree='да')
            bot_token = '6363160747:AAGyssU1JFJQxBF_uzRYFHNknPmCZ8TD-WY' 

            for i in subscribers:
                url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
                data = {'chat_id': i.chat_id, 'text': message}
                requests.post(url, data=data)

            return HttpResponse('Сообщение отправлено.')
        else:
            return HttpResponse('Ошибка', status=400)
    
    
# @csrf_exempt 
# def send_message(request):
#     if request.method == 'POST':                         
#         # message = request.POST.get('message', '')  # получаем сообщение
#         message = Announcement.full_description  # получаем сообщение
#         subscribers = BotTable.objects.filter(users_agree='да')
#         bot_token = '6363160747:AAGyssU1JFJQxBF_uzRYFHNknPmCZ8TD-WY' 

#         for i in subscribers:
#             url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
#             data = {'chat_id': i.chat_id, 'text': message}
#             requests.post(url, data=data)

#         return HttpResponse('Сообщение отправлено.')
#     else:
#         return HttpResponse('Ошибка', status=400)




# Create your views here.
