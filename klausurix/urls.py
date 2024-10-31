"""
URL configuration for klausurix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('exams/', views.exams, name='exams'),
    path('exams/<int:exam_id>/', views.exams_id, name='exams_id'),
    path('exams/<int:exam_id>/questions/', views.exam_questions, name='exams_questions'),
    path('exams/<int:exam_id>/questions/<int:question_id>/', views.exam_questions_id, name='exams_questions_id'),
    path('exams/<int:exam_id>/settings/number_of_questions/', views.exams_id_settings_number_of_questions, name='exams_id_settings_number_of_questions'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
