from django.urls import path
from aplication.medicines import views

app_name = 'medicines'  # Define el namespace aquí

urlpatterns = [
    path('medicamento_list/', views.MedicamentoListView.as_view(), name="medicamento_list"),
    path('medicamento_create/', views.MedicamentoCreateView.as_view(), name="medicamento_create"),
    path('medicamento_update/<int:pk>/', views.MedicamentoUpdateView.as_view(), name='medicamento_update'),
    path('medicamento_delete/<int:pk>/', views.MedicamentoDeleteView.as_view(), name='medicamento_delete'),
]
