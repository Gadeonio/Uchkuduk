function formSubmit(formelem) {
					let name_recipe = document.getElementsByName("name_recipe")[0].value;
					let athor_recipe = document.getElementsByName("athor_recipe")[0].value;
					let text_recipe = document.getElementsByName("text_recipe")[0].value;
					var alerttext = `${athor_recipe}, ваш рецепт ${name_recipe}, начинающийся с ${text_recipe.slice(0,10)}... и т.д. отправлен нам на обработку`;
					alert(alerttext);
				}