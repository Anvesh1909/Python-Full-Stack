from multiprocessing.spawn import import_main_path
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('products',views.products,name='products'),
    path("product_detail/<slug:slug>",views.product_details,name="product_detail")
]


urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)