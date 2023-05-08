import json
from functools import singledispatchmethod


from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, FormView, View
from django.http import JsonResponse

from core import dbservice


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


class AddRecipeView(TitleMixin, NavMixin, TemplateView):
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




