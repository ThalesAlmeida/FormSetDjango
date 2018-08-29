from django.urls import path
from family.views import ProfileFamilyMemberCreate, ProfileList

urlpatterns = [
    path('add/', ProfileFamilyMemberCreate.as_view(), name='profile-add'),
    path('list/', ProfileList.as_view(), name='profile-list'),
]