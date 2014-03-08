$(function () {
	$('input[type=file]').change(function(){
		$(this).closest('form').submit();
	});
});