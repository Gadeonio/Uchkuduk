/*
Реализация AJAX с помощью асинхронного метода fetch. Современный вариант реализации AJAX.
*/

var sendbtn = document.getElementById("sendbtn");    // выбираем DOM-елемент (кнопку)

// Привязываем к элементу обработчик события "click"
sendbtn.addEventListener("click", function (e) {
    /* Инструкция preventDefault позволяет переопределить стандартное поведение браузера,
    если ее убрать, то браузер по-умолчанию обновит страницу после отправки данных формы */
    e.preventDefault();
    // Получаем данные полей формы
    let name_recipe = document.getElementsByName("name_recipe")[0].value;
    let athor_recipe = document.getElementsByName("athor_recipe")[0].value;
    let text_recipe = document.getElementsByName("text_recipe")[0].value;
    // Преобразуем полученные данные в JSON
    var formdata = JSON.stringify({ name: name_recipe, athor: athor_recipe, text: text_recipe});
    
    // Отправляем запрос через fetch (необходимо выставить соответствующий заголовок (headers)!)
    fetch("",
    {
        method: "POST",
        body: formdata,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        }

    })
    .then( response => {
        // fetch в случае успешной отправки возвращает Promise, содержащий response объект (ответ на запрос)
        // Возвращаем json-объект из response и получаем данные из поля message
        response.json().then(function(data) {
            console.log(data)
            let statfield = document.getElementById("statusfield");
            statfield.textContent = data.message;
            alert(data.message);
        });
    })
    .catch( error => {
        alert(error);
        console.error('error:', error);
    });

});
