from django.shortcuts import render
from .models import Indications, Resistence, Current
from django.http import JsonResponse
from django.db.models import Avg, Q
from datetime import datetime
from requests import get



from rest_framework import viewsets
from .serializers import VoltageSerializer


def index(request):
    values = Indications.objects.order_by('-time')[0:1]
    return render(request, 'system/index.html', {'values': values})


class VoltageViewSet(viewsets.ModelViewSet):
    queryset = Indications.objects.order_by('-id')
    serializer_class = VoltageSerializer


def indx(request):
    voltage = Indications.objects.order_by('-time').values('id', 'name', 'value', 'time')[0:1]
    current = Current.objects.order_by('-time').values('id', 'value', 'time')[0:1]
    resistence = Resistence.objects.order_by('-time').values('id', 'value', 'time')[0:1]
    return JsonResponse({'a': list(voltage), 'current': list(current), 'resistence': list(resistence)})


def hour(request):
    timE = str(datetime.now())[0:10]
    a = []
    aa = []
    aaa = []
    b = {}
    # Создаются переменные, к которым из AJAX будем обращаться
    for i in range(0, 24):
        a.append(f'h{i}')

    for i in range(0, 24):
        aa.append(f'i{i}')

    for i in range(0, 24):
        aaa.append(f's{i}')

    for i in range(0, 24):
        if i == 23:
            k = Indications.objects.filter(Q(time__gte=f'{timE} {i}:00:00') & Q(time__lte=f'{timE} 01:00:00')).aggregate(Avg('value'))
        else:
            if i < 10 and i != 9:
                k = Indications.objects.filter(Q(time__gte=f'{timE} 0{i}:00:00') & Q(time__lte=f'{timE} 0{str(i+1)}:00:00')).aggregate(
                    Avg('value'))
            elif i == 9:
                k = Indications.objects.filter(Q(time__gte=f'{timE} 09:00:00') & Q(time__lte=f'{timE} 10:00:00')).aggregate(
                    Avg('value'))
            else:
                k = Indications.objects.filter(Q(time__gte=f'{timE} {i}:00:00') & Q(time__lte=f'{timE} {i + 1}:00:00')).aggregate(
                    Avg('value'))

        b[a[i]] = k


    for i in range(0, 24):
        if i == 23:
            k = Resistence.objects.filter(Q(time__gte=f'{timE} {i}:00:00') & Q(time__lte=f'{timE} 01:00:00')).aggregate(Avg('value'))
        else:
            if i < 10 and i != 9:
                k = Resistence.objects.filter(Q(time__gte=f'{timE} 0{i}:00:00') & Q(time__lte=f'{timE} 0{str(i+1)}:00:00')).aggregate(
                    Avg('value'))
            elif i == 9:
                k = Resistence.objects.filter(Q(time__gte=f'{timE} 09:00:00') & Q(time__lte=f'{timE} 10:00:00')).aggregate(
                    Avg('value'))
            else:
                k = Resistence.objects.filter(Q(time__gte=f'{timE} {i}:00:00') & Q(time__lte=f'{timE} {i + 1}:00:00')).aggregate(
                    Avg('value'))

        b[aaa[i]] = k

    for i in range(0, 24):
        if i == 23:
            k = Current.objects.filter(Q(time__gte=f'{timE} {i}:00:00') & Q(time__lte=f'{timE} 01:00:00')).aggregate(
                Avg('value'))
        else:
            if i < 10 and i != 9:
                k = Current.objects.filter(
                    Q(time__gte=f'{timE} 0{i}:00:00') & Q(time__lte=f'{timE} 0{str(i + 1)}:00:00')).aggregate(
                    Avg('value'))
            elif i == 9:
                k = Current.objects.filter(
                    Q(time__gte=f'{timE} 09:00:00') & Q(time__lte=f'{timE} 10:00:00')).aggregate(
                    Avg('value'))
            else:
                k = Current.objects.filter(
                    Q(time__gte=f'{timE} {i}:00:00') & Q(time__lte=f'{timE} {i + 1}:00:00')).aggregate(
                    Avg('value'))

        b[aa[i]] = k

    b['date'] = timE

    return JsonResponse(b)
