from django.urls import path
#lets re-use the django login view.
from django.contrib.auth import views as auth_views

from .import views



#lets import a file called views from "myapp" application.
from finalapplication import views
urlpatterns =[
  #  path('index/',views.index,name='index'),
    path('',views.index,name='index'),
    path('services',views.services,name='services'),
    path('contactus',views.contactus,name='contactus'),
    path('home/',views.home,name='home'),

    path('home/<int:product_id>',views.product_detail,name='product_detail'),

  #receipt
   # this handles issueing receipts after making a sale.
    path('receipt/',views.receipt,name='receipt'),
   
    path('receipt/<int:receipt_id>',views.receipt_detail,name='receipt_detail'),
    
  #sales
  # gives us where we fill in information to sale a product
    path('issue_item/<str:pk>',views.issue_item,name='issue_item'),
   

  #add to stock
    path('add_to_stock/<str:pk>',views.add_to_stock,name='add_to_stock'),
    path('all_sales/',views.all_sales,name='all_sales'),

  # delete path.
    path('delete/<int:product_id>',views.delete_detail,name='delete_detail'),


  #login and logout
    path('login/',auth_views.LoginView.as_view(template_name='project/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='project/index.html'),name='logout'),
   # registration 
    path('registration/',views.registration,name='registration'),

   # image.
    path('upload/', views.upload_image, name='upload_image'),
    path('image-list/', views.image_list, name='image_list'),
    
]