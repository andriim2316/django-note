from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test_function(request):
    return HttpResponse("""
    <h1>Hello this is a test page</h1>
    <p><a href='/'>Link</a> to the main page </p>
    """)