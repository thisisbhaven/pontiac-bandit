from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from .models import Product, Customer, Order, BPM
from .serializers import ProductSerializer, ProductCreateSerializer, CustomerSerializer, CustomerCreateSerializer, OrderSerializer, OrderCreateSerializer, BPMSerializer

# Create your views here.

# Product APIs
class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

class ProductUpdate(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDelete(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Customer APIs

class CustomerList(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CustomerCreateSerializer


class CustomerUpdate(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDelete(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Order APIs

class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderCreate(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

class OrderDetail(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUpdate(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDelete(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class BPMDetail(DestroyAPIView):
    queryset = BPM.objects.all()
    serializer_class = BPMSerializer