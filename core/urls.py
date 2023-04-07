from django.urls import path

from . import views

app_name = "core"
urlpatterns = [
    path("don_t_touch_this", views.MainView.as_view(), name="main"),
    path("", views.IndexView.as_view(), name="index"),
    path("addrecipe/", views.AddRecipeView.as_view(), name="addrecipe"),
    path("recipes/", views.RecipeView.as_view(), name="recipes"),
    path("search/", views.Search.as_view(), name="search"),
]