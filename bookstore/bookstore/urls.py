

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet , index
from django.contrib import admin

router = DefaultRouter()
router.register(r'books', BookViewSet)




urlpatterns = [
    path('index/',index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
