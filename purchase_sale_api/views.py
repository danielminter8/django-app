from __future__ import annotations

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from purchase_sale_api.models import PurchaseSaleData
from purchase_sale_api.services.processor import processor


def liveness(request):
    return JsonResponse({'data': 'Server is alive!'})


@csrf_exempt
def upload_csv(request):  # processFile

    if request.method != 'POST':
        return JsonResponse({'method not available'})

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        return JsonResponse({'file must be a csv'})

    try:
        processor(csv_file)
        return JsonResponse({'data': 'csv processed'})
    except Exception as e:
        print('err:', e)
        return JsonResponse({'data': 'error occured'})


def retrieve_data(request):  # retrieveRows

    if request.method != 'GET':
        return JsonResponse({'method not available'})

    country_code = request.GET.getlist('country')
    date = request.GET.getlist('date')

    if len(country_code) > 0 and len(date) > 0:
        data = PurchaseSaleData.objects.filter(
            country_code=country_code[0], date=date[0],
        ).values()

    return JsonResponse({'data': list(data)})
