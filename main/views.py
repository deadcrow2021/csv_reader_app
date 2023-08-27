from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
from .serializers import DealsSerializer
from .forms import CSVForm

from .models import Deals

@api_view(['GET'])
def api_overview(request):
	api_urls = {
		'List':'/deals/',
        'Add': '/create',
		}
	return Response(api_urls)


@api_view(['GET'])
def deals_list(request):
    if request.query_params:
        items = Deals.objects.filter(**request.query_params.dict())
    else:
        items = Deals.objects.all()
 
    if items:
        serializer = DealsSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_deals(request):
    if request.method == 'POST':
        file_obj = request.FILES['file']
        # if file_obj.multiple_chunks():
        #     for i in file_obj.chunks():
        #         print(i)
        
        file_text = file_obj.read().decode()
        file_rows = list(filter(lambda el: el != '', file_text.split('\r\n')))
        try:
            for deal in file_rows[1:]:
                row = deal.split(',')
                obj = Deals(
                    customer = row[0],
                    item = row[1],
                    total = str(row[2]),
                    quantity = str(row[3]),
                    date = row[4]
                )
                obj.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(data={'error': err}, status=status.HTTP_403_FORBIDDEN)


def main(request):
    form = CSVForm()
    return render(request, 'main/main.html', {'form': form})
