from django.test import TestCase
from django.shortcuts import render, redirect
# Create your tests here.
def test(request):
    return render(request, 'bank/welcome.html')
