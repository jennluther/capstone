from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.conf import settings
from homepage import models as hmod
from django.http import HttpResponseRedirect
import datetime

'''******************************************
*	hompage/index page
*		-Lets make a nice pretty page for this
*********************************************'''
def index(request):
	context={'because':"I like to think about django when I sleep",}
	return render(request,'index.html',context)
