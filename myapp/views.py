from django.shortcuts import render
from django.http import JsonResponse
from .tasks import start_scraping_job
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request, 'dashboard.html', {})

@csrf_exempt
def start_scrape(request):
    data = json.loads(request.body)
    region = data.get('region')
    print("Region", region)
    task = start_scraping_job.delay(region)
    return JsonResponse({"message": "Scrape Started"})