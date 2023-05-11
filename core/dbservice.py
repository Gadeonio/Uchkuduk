import json

from django.db import connection


def get_recipe_all():
    result = [] # создаем пустой список
    with connection.cursor() as cursor:
        # Получаем итерируемый объект, где содержатся все строки таблицы contactrequests
        rows: tuple = cursor.execute("SELECT id, name, author, text, image FROM core_recipe").fetchall()
        # Каждую строку конвертируем в стандартный dict, который Flask может трансформировать в json-строку
        for row in rows:
            result.append(dict([
                ('id', row[0]),
                ('name', row[1]),
                ('author', row[2]),
                ('text', row[3]),
                ('image', row[4])
                ]))
    # возвращаем dict, где result - это список с dict-объектов с информацией
    return {'recipe': result}


# Получаем запрос с фильтром по id
def get_recipe_by_pk(pk):
    result = None
    print(id)
    with connection.cursor() as cursor:
        row = cursor.execute(f"SELECT id, name, author, text, image FROM core_recipe WHERE id = {pk}").fetchone()
        result = dict([
            ('id', row[0]),
            ('name', row[1]),
            ('author', row[2]),
            ('text', row[3]),
            ('image', row[4])
        ])
        print(result)
    return result


# Получаем все запросы по имени автора
def get_recipe_by_author(author):
    result = []
    with connection.cursor() as cursor:
        rows = cursor.execute(f"SELECT * FROM core_recipe WHERE author = '{author}'").fetchall()
        for row in rows:
            result.append(dict([
                ('id', row[0]),
                ('name', row[1]),
                ('author', row[2]),
                ('text', row[3]),
                ('image', row[4])
            ]))
    return {'recipe': result}


# Создать новый запрос
def create_recipe(request):
    with connection.cursor() as cursor:
        msg = None
        try:
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)
        #cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")     # текущая дата и время
        # INSERT запрос в БД
            cursor.execute(f'INSERT INTO core_recipe'
                           f'(name, author, text, image)'
                           f'VALUES ('
                           f"'{body_data['name']}', "
                           f"'{body_data['author']}', "
                           f"'{body_data['text']}', "
                           f"'')")
            # Возвращаем результат
            msg = "Recipe Created!"
        # если возникла ошибка запроса в БД
        finally:
            cursor.close()
            return {'message': msg}


# Удалить запрос по id в таблице
def delete_recipe_by_pk(pk):
    with connection.cursor() as cursor:
        msg = None
        try:
            # DELETE запрос в БД
            cursor.execute(f"DELETE FROM core_recipe WHERE id = {pk}")
            msg = "Recipe Deleted!"
        finally:
            cursor.close()
            return {'message': msg}


# Обновить текст запроса по id в таблице
def update_recipe_by_pk(pk, request):
    with connection.cursor() as cursor:
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        msg = None
        try:
            # UPDATE запрос в БД
            cursor.execute(f"UPDATE core_recipe SET text = '{body_data['text']}' WHERE id = {pk}")
            msg = "Recipe Updated!"
        except Exception:
            msg = Exception
        finally:
            cursor.close()
            return {'message': msg}