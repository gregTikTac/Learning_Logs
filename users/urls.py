from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # url авторизация по умолчанию
    path('', include('django.contrib.auth.urls'))
]