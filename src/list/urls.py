from django.urls import path

from list.views import (
    list_view,
    list_delete_view,
    # list_done_view,
)

app_name='list'
urlpatterns = [
    path('', list_view, name="list"),
    path('<int:id>/delete/', list_delete_view),
    # path('<int:id>/done/', list_done_view),
]