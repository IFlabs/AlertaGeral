# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required, permission_required
from djtools.utils import rtr, httprr, str_to_dateBR, group_required, \
    user_has_profile, user_has_one_of_perms, render, get_rss_links, to_ascii
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from django.template import RequestContext
import django.shortcuts
from alerta.models import *


def index(request):
    alertas = Alerta.objects.filter(ativo=True).order_by('-id')[:12]
    return django.shortcuts.render(request, 'index.html',locals())