from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sharing_app.urls')),
    path('user/', include('user_app.urls')),


]

# path('reg/', user_views.registration, name="registration"),
#  path('reg/', include('user_app.urls')),
# for user app: welcome -> registration
#                       -> login