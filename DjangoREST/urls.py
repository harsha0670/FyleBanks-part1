from django.contrib import admin
from django.urls import path

from django.urls import path, include
from BanksAPI.views import BankViewByBranch
from BanksAPI.views import BankViewBySearch
# from BanksAPI.views import AllBranches



urlpatterns = [
    # path('api', AllBranches.as_view()),
    path('api/branches/autocomplete', BankViewByBranch.as_view()),
    path('api/branches',BankViewBySearch.as_view()),
    path('admin/', admin.site.urls),
]
