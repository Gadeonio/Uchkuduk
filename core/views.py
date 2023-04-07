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


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context

def bad_request():
    return JsonResponse({'error': 'Bad request'}), 400

def json_response(data, code=200):
    return HttpResponse(status=code, mimetype="application/json", response=data)


class RecipeView(TitleMixin, NavMixin, TemplateView):
    template_name = "core/recipes.html"
    title = "Рецепты"


class Search(TitleMixin, NavMixin, TemplateView):
    template_name = "core/search.html"
    title = "Поиск"
