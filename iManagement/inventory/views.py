from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Items
from .serializer import ItemSerializer



print("Loading views module...")
@api_view(['GET', 'POST'])
def get_items(request):
    if request.method == 'POST':
        item = ItemSerializer(data=request.data)
        if item.is_valid():
            print("is valid")
            item.save()
            return Response({"data" : item.data, "success" : True, "status":status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error" : {"message": "Kindly enter the valid data"}, "success" : False, "status": status.HTTP_400_BAD_REQUEST}, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        items = Items.objects.all()
        return Response({"data" : ItemSerializer(items, many=True).data, "success" : True, "status":status.HTTP_200_OK}, status=status.HTTP_200_OK)
    else:
        return Response({"error" : {"message": "Requested Page not found"}, "success" : False, "status": status.HTTP_404_NOT_FOUND}, status = status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def manage_item(request, item_id):
    try:
        item = Items.objects.get(pk=item_id)
        print("item ", item)
    except Items.DoesNotExist:
        return Response({"error" : {"message": "Requested ID not found"}, "success" : False, "status": status.HTTP_404_NOT_FOUND}, status = status.HTTP_404_NOT_FOUND)
    except:
        return Response({"error" : {"message": "Something went wrong"}, "success" : False, "status": status.HTTP_400_BAD_REQUEST}, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        print("In get request")
        return Response(ItemSerializer(item, many=False).data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        print("In put request")
        new_data = ItemSerializer(item, data=request.data)
        if new_data.is_valid():
            new_data.save()
            return Response({"data" : new_data.data, "success" : True, "status":status.HTTP_200_OK}, status=status.HTTP_200_OK)
        else:
            return Response({"error" : {"message": "Kindly enter the valid data"}, "success" : False, "status": status.HTTP_400_BAD_REQUEST}, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        print("In delete request")
        item.delete()
        return Response({"data" : "Item deleted successfully", "success" : True, "status":status.HTTP_204_NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"error" : {"message": "Requested Page not found"}, "success" : False, "status": status.HTTP_404_NOT_FOUND}, status = status.HTTP_404_NOT_FOUND)
