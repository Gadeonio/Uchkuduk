$("figure img").hover(
				function() {
					$(this).animate({
						width: "400px",
						height: "280px",
					}, "slow");
				}, function() {
					$(this).animate({
						width: "370px",
						height: "250px",
					}, "slow");
				});