from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


from mpl_toolkits.basemap import Basemap
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import base64


# Create your views here.

def index(request):
    map = Basemap(projection='cyl')
    map.bluemarble()
    map.nightshade(datetime.now(), delta=0.2)
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = figdata_png

    return HttpResponseRedirect(request, 'timemap/index.html', {'result':result})

