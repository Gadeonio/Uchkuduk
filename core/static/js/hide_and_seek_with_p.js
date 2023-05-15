$(document).ready(function() {
	$(".hidebox h1").css("background-color", "#C0C0C0");
	$(".hidebox p").hide();
});
$(".hidebox h1").click(function () {
	$(this).next("p").toggle("slow");
	if ($(this).attr("flag") === "true"){
		$(this).css("background-color", "#DCDCDC");
		$(this).attr("flag", "false");
	}else{
		$(this).css("background-color", "#C0C0C0");
		$(this).attr("flag", "true");
	}
});