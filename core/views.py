import json

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, FormView
from django.http import JsonResponse




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
            athor = body_data['athor']
            text = body_data['text']
            msg = ""
            if text == '':
                msg = "Нужен сам рецепт!!!"
            elif athor == '':
                msg = "Спасибо за рецепт, Анонимус"
            else:
                msg = "Спасибо за рецепт, " + str(athor)
            return JsonResponse({'message': msg}, safe=False)
        else:
            return render(request, template_name=self.template_name)





class RecipeView(TitleMixin, NavMixin, TemplateView):
    template_name = "core/recipes.html"
    title = "Рецепты"


class Search(TitleMixin, NavMixin, TemplateView):
    template_name = "core/search.html"
    title = "Поиск"
