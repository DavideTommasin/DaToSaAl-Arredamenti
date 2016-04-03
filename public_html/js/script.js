$( document ).ready(function() {
    $(".btn-responsive-menu").click(function() {
	    $("#mainmenu").toggleClass("show");
		$("body").toggleClass("showmenu");
	});
	
	$(window).resize(function() {
		if($(window).width() >= 769){
			$("#mainmenu").removeClass("show");
			$("body").removeClass("showmenu");
		}
	});

	$("freccia").click(function() {
	    $("body").scrollTo("#header");
	});
});