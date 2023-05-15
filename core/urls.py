from django.urls import path

from . import views

app_name = "core"
urlpatterns = [
    path("don_t_touch_this", views.MainView.as_view(), name="main"),
    path("", views.IndexView.as_view(), name="index"),
    path("addrecipe/", views.AddRecipeView.as_view(), name="addrecipe"),
    path("recipes/", views.RecipeView.as_view(), name="recipes"),
    path("search/", views.SearchView.as_view(), name="search"),

    path("api/recipe/create/", views.CreateRecipeView.as_view()),
    path("api/recipe/", views.AllRecipeView.as_view()),
    path("api/recipe/<int:pk>/", views.ConcreteRecipeView.as_view()),
    path("api/recipe/author/<str:author>/", views.ConcreteRecipe2View.as_view()),

    path("login/", views.MyLoginView.as_view(), name="login"),
    path("registration/", views.register, name="register")
]