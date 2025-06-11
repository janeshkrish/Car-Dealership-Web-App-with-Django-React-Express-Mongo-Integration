from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home_view(request):
    return HttpResponse("<h1>Welcome to Dealership App</h1>")

def about_view(request):
    return HttpResponse("<h1>About Us</h1><p>This is the About page.</p>")

def contact_view(request):
    return HttpResponse("<h1>Contact Us</h1><p>This is the Contact page.</p>")

@csrf_exempt
def sentiment_analysis(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        review = data.get('review', '')

        # Mock sentiment logic
        if any(word in review.lower() for word in ['good', 'great', 'excellent']):
            sentiment = 'positive'
        elif any(word in review.lower() for word in ['bad', 'terrible', 'poor']):
            sentiment = 'negative'
        else:
            sentiment = 'neutral'

        return JsonResponse({'review': review, 'sentiment': sentiment})
    else:
        return JsonResponse({'error': 'Only POST method allowed'}, status=405)
