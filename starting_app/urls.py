from django.urls import path

from starting_app import views

urlpatterns = [
    path('students', views.index, name='students'),
    path("student/<int:pk>/", views.get_student, name="student"),
    path("createStudent", views.createStudent, name="createStudent"),

    # path('contact', views.contact, name='contact'),
]