/*
Реализация AJAX с помощью асинхронного метода fetch. Современный вариант реализации AJAX.
*/
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

var sendbtn = document.getElementById("sendbtn");    // выбираем DOM-елемент (кнопку)

// Привязываем к элементу обработчик события "click"
sendbtn.addEventListener("click", function (e) {
    /* Инструкция preventDefault позволяет переопределить стандартное поведение браузера,
    если ее убрать, то браузер по-умолчанию обновит страницу после отправки данных формы */
    e.preventDefault();
    // Получаем данные полей формы
    let recipe_n = document.getElementsByName("name_recipe")[0].value;
    let recipe_a = document.getElementsByName("athor_recipe")[0].value;
    let recipe_t = document.getElementsByName("text_recipe")[0].value
    // Преобразуем полученные данные в JSON
    var formdata = JSON.stringify({ firstname: recipe_n, lastname: recipe_a, reqtext: recipe_t});
    
    // Отправляем запрос через fetch (необходимо выставить соответствующий заголовок (headers)!)
    const request = new Request(
    /* URL */,
    {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin' // Do not send CSRF token to another domain.
     }

    fetch(request)(
    {
        method: "POST",
        body: formdata,
        headers: {
            headers: {'X-CSRFToken': csrftoken},
            'Content-Type': 'application/json'
        }
    })
        const request = new Request(
    /* URL */,
    {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin' // Do not send CSRF token to another domain.
     }
);
});
    .then( response => {
        // fetch в случае успешной отправки возвращает Promise, содержащий response объект (ответ на запрос)
        // Возвращаем json-объект из response и получаем данные из поля message
        response.json().then(function(data) {
            console.log(data)
            let statfield = document.getElementById("statusfield");
            statfield.textContent = data.message;
            //statfield.textContent.bold();
            //alert(data.message);
        });
    })
    .catch( error => {
        alert(error);
        console.error('error:', error);
    });

});
