
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from rest_framework import status

class OrderCreateView(APIView):
    def post(self, request):
        # In a real setup we'd verify cart, calculate totals, reserve stock, etc.
        data = request.data
        order = Order.objects.create(user_id=data.get('user_id', 0), total=data.get('total',0))
        # TODO: send message to RabbitMQ (Celery task)
        return Response({'order_id': order.id}, status=status.HTTP_201_CREATED)

class OrderDetailView(APIView):
    def get(self, request, pk):
        try:
            o = Order.objects.get(pk=pk)
            return Response({'id': o.id, 'user_id': o.user_id, 'total': str(o.total), 'status': o.status})
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
