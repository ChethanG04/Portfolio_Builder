from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_portfolio_form, name='show_portfolio_form'),  # Show the portfolio form
    path('submit/', views.save_portfolio, name='save_portfolio'),      # Handle form submission
    path('success/', views.success, name='success'),                  # Show success page after submission
]
