from django.urls import path
from my_app.views import home, store_book,show_tasks,edit_tasks,delete_book,completed_tasks
urlpatterns = [
    
    path('',home),
    path('store_new_book/', store_book,name='store_book'),
    path('show_tasks/', show_tasks,name='show_tasks'),
    path('edit_tasks/<int:id>', edit_tasks,name='edit_tasks'),
    path('delete_book/<int:id>', delete_book,name='delete_book'),
    path('completed_tasks/<int:id>', completed_tasks,name='completed_tasks'),
]