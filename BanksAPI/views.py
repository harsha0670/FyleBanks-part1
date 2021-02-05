from django.shortcuts import render
from rest_framework import generics
from BanksAPI.serializers import BankSerializer
from .models import Bank

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter

# Create your views here.

class AllBranches(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    pagination_class = None

class BankViewByBranch(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    pagination_class = LimitOffsetPagination

    search_fields = ['branch',]
    filter_backends = (SearchFilter,)

class BankViewBySearch(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    pagination_class = LimitOffsetPagination

    search_fields = ['ifsc','bank_id','branch','address','city','district','state','bank_name',]
    filter_backends = (SearchFilter,)



