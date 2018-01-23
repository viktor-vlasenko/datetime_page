from datetime import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
def index(request):
    name = request.POST.get('name')    
    if name is not None:
        now = datetime.now()
        current_date = now.strftime("%d-%m-%Y")
        current_time = now.strftime("%H:%M")
        return render(request, 'core/index.html', context={
            'name': name,
            'current_time': current_time,
            'current_date': current_date
        })
    return render(request, 'core/index.html')