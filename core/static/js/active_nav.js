var main_id = document.querySelector("main").id;
var navmenu = document.getElementsByClassName("top-menu")[0]
var navlist = navmenu.getElementsByTagName("li");
var menuelem;

switch(main_id) {
	case 'home':
		menuelem = navlist[0];
		break;
	case 'addrecipe':
		menuelem = navlist[3];
		break;
	case 'recipes':
		menuelem = navlist[1];
		break;
	case 'search':
		menuelem = navlist[2];
		break;
	default:
		menuelem = navlist[0];
}
menuelem.classList.add("active");