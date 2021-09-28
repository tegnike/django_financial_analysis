from django.shortcuts import render

# 以下を全て追加
from django.views import generic
from django.views.generic import TemplateView

class IndexTemplateView(TemplateView):
    template_name = 'finchart/index.html'
