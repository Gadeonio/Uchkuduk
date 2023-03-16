var main_id = document.querySelector("main").id;
var headtext = document.getElementById("headname");
var text;

switch(main_id) {
	case 'home':
		text = "Главная страница";
		break;
	case 'addrecipe':
		text = "Добавление рецептов";
		break;
	case 'recipes':
		text = "Рецепты";
		break;
	case 'search':
		text = "Поиск";
		break;
	default:
		text = "Алина, что за страница?";
};
headtext.textContent = text



