/*
$(document).ready(function(){
	$("p").click(function(){
		$("ul").toggle('slow');
	});
	
  	var count = 0;
 
 
	$("#test").click(function(){
		count += 1;
		var html = $("#message").text();
		if (count > 2) {
			var new_html = html + ' count';
			$("#message").toggle('fast')
			$("#message").html(new_html);
		} else {
			$("#message").toggle('slow')
			$("#message").html(new_html);
		}
	});  
});
*/