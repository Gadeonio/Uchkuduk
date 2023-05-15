import json
from functools import singledispatchmethod

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, FormView, View
from django.http import JsonResponse

from core import dbservice
from core.forms import RegistrationForm


class TitleMixin:
    title: str = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_title()
        return context


class NavMixin:
    navs = {'core:index': 'Главная', 'core:recipes': 'Рецепты', 'core:search': 'Поиск', 'core:addrecipe': 'Добавить рецепт'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['nav_names'] = self.get_nav_names()
        return context

    def get_nav_names(self):
        return self.navs


class MainView(TitleMixin, NavMixin, TemplateView):
    template_name = "core/main.html"
    title = 'Main'

    def get_title(self):
        return self.title

    def get_info(self):
        return 'Мем'


class IndexView(TitleMixin, NavMixin, TemplateView):
    template_name = "core/index.html"
    title = 'Главная страница'


class AddRecipeView(LoginRequiredMixin, TitleMixin, NavMixin, TemplateView):
    template_name = "core/addrecipe.html"
    title = "Добавление рецептов"

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)
            #лучше использовать loger вместо print

            name = body_data['name']
            author = body_data['author']
            text = body_data['text']
            msg = ""
            if text == '':
                msg = "Нужен сам рецепт!!!"
            elif author == '':
                msg = "Спасибо за рецепт, Анонимус"
            else:
                msg = "Спасибо за рецепт, " + str(author)
            return JsonResponse({'message': msg}, safe=False)
        else:
            return render(request, template_name=self.template_name)


class RecipeView(TitleMixin, NavMixin, TemplateView):
    template_name = "core/recipes.html"
    title = "Рецепты"


class SearchView(TitleMixin, NavMixin, TemplateView):
    template_name = "core/search.html"
    title = "Поиск"


class CreateRecipeView(View):
    http_method_names = ['post']

    @csrf_exempt
    def post(self, request):
        response = dbservice.create_recipe(request)
        return JsonResponse(response, safe=False)


class AllRecipeView(View):
    http_method_names = ['get']

    def get(self, request):
        response = dbservice.get_recipe_all()
        return JsonResponse(response, safe=False)


class ConcreteRecipe2View(View):
    http_method_names = ['get']

    def get(self, request, author: str):
        response = dbservice.get_recipe_by_author(author)
        return JsonResponse(response, safe=False)


class ConcreteRecipeView(View):
    http_method_names = ['get', 'put', 'delete']

    def get(self, request, pk: int):
        response = dbservice.get_recipe_by_pk(pk)
        return JsonResponse(response, safe=False)

    def put(self, request, pk):
        # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
        # или в данных нет обязательного поля 'reqtext'
        response = dbservice.update_recipe_by_pk(pk, request)
        return JsonResponse(response, safe=False)
    # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)

    def delete(self, request, pk):
        response = dbservice.delete_recipe_by_pk(pk)
        return JsonResponse(response)


class MyLoginView(TitleMixin, NavMixin, LoginView):
    template_name = "core/login.html"


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            return render(request, 'core/index.html', {'new_user': new_user})
        else:
            print(user_form.errors)
            return render(request, 'core/registration.html', {'user_form': user_form})
    else:
        user_form = RegistrationForm()
    return render(request, 'core/registration.html', {'user_form': user_form})

'''class RegisterView(FormView):
    template_name = "core/registration.html"
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        if self.form_class.is_valid:
            user = self.form_class.save(self.form_class, commit=False)
            user.save()
            return render(request, 'core/index.html', {'user': user})
        print(self.form_class.errors)
        return render(request, template_name=self.template_name)



    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return 'core:index'

"'''









