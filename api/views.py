# Create your views here.
from django.http import HttpResponse
from django.views.generic import View

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<div style="margin:50px auto 0px auto;text-align:center;width:100%;font-family:Arial,Sans,FreeSans;"><h1>We The People API for <a href="http://wh.gov">wh.gov</a></h1><h2>try <a href="/petitions/">/petitions/</a></h2></div>')
