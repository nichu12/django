from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def home(request):
    return render(request,"ind.html")
    