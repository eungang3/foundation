from django.urls import path 

from owners.views import OwnersView, DogsView, DogOwnersView 

urlpatterns = [
    path('owners', OwnersView.as_view()),
    path('dogs', DogsView.as_view()),
    path('dogowners', DogOwnersView.as_view())
]