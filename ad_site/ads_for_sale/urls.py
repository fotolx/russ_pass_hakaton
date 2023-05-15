from django.urls import path
from .views import home, RegisterView, AdsList
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    # path('', cache_page(60*5) (PostsList.as_view())), 
    path('ads/', AdsList.as_view()), 
    # # path('<int:pk>', cache_page(60*5) (PostDetail.as_view()), name='details'),
    # path('<int:pk>', PostDetail.as_view(), name='details'),
    # path('search', SearchList.as_view(), name='search'),
    # path('add', PostsAdd.as_view()), 
    # path('<int:pk>/edit/', PostEdit.as_view(), name='edit_post'),
    # path('<int:pk>/delete/', PostDelete.as_view(), name='delete_post'),
    # path('<int:pk>/subscribe/', SubscribeToCategory.as_view(), name = 'subscribe'),
    # path('<int:pk>/unsubscribe/', UnSubscribeToCategory.as_view(), name = 'unsubscribe'),
]