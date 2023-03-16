$(document).ready(function() {
	$(".hidebox h1").css("background-color", "#29c5e6");
	$(".hidebox p").hide();
});
$(".hidebox h1").click(function () {
	$(this).next("p").toggle("slow");
	if ($(this).attr("flag") === "true"){
		$(this).css("background-color", "#e7e7e7");
		$(this).attr("flag", "false");
	}else{
		$(this).css("background-color", "#000000");
		$(this).attr("flag", "true");
	}
});