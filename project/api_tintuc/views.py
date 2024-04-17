from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Giaidau, Tintuc
from .serializers import GiaidauSerializers, TintucSerializers

# ------------------------------- GIẢI ĐẤU ---------------------------------

@api_view(['GET', 'POST'])
def gd_list(request):
    if request.method == 'GET':
        gds = Giaidau.objects.all()
        serializer = GiaidauSerializers(gds, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GiaidauSerializers(data=request.data)
        if serializer.is_valid():
            gd = serializer.save()
            response_data = {
                'message': 'Giai dau da duoc them thanh cong!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def gd_detail(request, pk):
    try:
        gd = Giaidau.objects.get(pk=pk)
    except Giaidau.DoesNotExist:
        return Response({'Error': 'Khong the tim thay giai dau!'}, status=404)

    if request.method == 'GET':
        serializer = GiaidauSerializers(gd)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GiaidauSerializers(gd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Giai dau da duoc cap nhat thanh cong!',
                'data': serializer.data,
            }
            return Response(response_data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        gd.delete()
        return Response({'message': 'Giai dau da duoc xoa thanh cong!'}, status=204)
    

    # ------------------------------- TIN TỨC ---------------------------------

@api_view(['GET', 'POST'])
def tt_list(request):
    if request.method == 'GET':
        tts = Tintuc.objects.all()
        serializer = TintucSerializers(tts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TintucSerializers(data=request.data)
        if serializer.is_valid():
            tt = serializer.save()
            response_data = {
                'message': 'Tin tuc da duoc them thanh cong!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'DELETE'])
def tt_detail(request, pk):
    try:
        tt = Tintuc.objects.get(pk=pk)
    except Tintuc.DoesNotExist:
        return Response({'Error': 'Khong the tim thay tin tuc!'}, status=404)

    if request.method == 'GET':
        serializer = TintucSerializers(tt)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TintucSerializers(tt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Tin tuc da duoc cap nhat thanh cong!',
                'data': serializer.data,
            }
            return Response(response_data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        tt.delete()
        return Response({'message': 'Tin tuc da duoc xoa thanh cong!'}, status=204)
    