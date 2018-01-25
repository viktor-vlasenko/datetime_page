from datetime import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from core.models import Users

@method_decorator(csrf_exempt, name='dispatch')
def index(request):
    name = request.POST.get('name')    
    if name is not None:
        now = datetime.now()
        date = now.strftime("%d of %B, %Y")
        time = now.strftime("%H:%M")
        user = Users.objects.create(username=name, date=date, time=time)
        user.save()
        return render(request, 'core/index.html', context={
            'name': name,
            'current_time': time,
            'current_date': date
        })
    return render(request, 'core/index.html')