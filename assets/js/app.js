
$(document).ready(function(){

	$(".del-post-link").click(function(e){
		// prevent link redirection even if it was just a #
		e.preventDefault();
		// submit the next form
		$(this).next().submit();

	});

	$(".critical-frm").submit(function(e){
		if( !confirm('Are you sure?') )
		    e.preventDefault();
	});

	$(".comment").keyup(function(){
		if($(".comment").val()){
			$(".comment-btn").show()
		}else{
			$(".comment-btn").hide()
		}
	});



	$('.edit-comment').click(function(e){
		e.preventDefault();
		comment_el = $(this).closest(".comment-action-btn").next();
		comment_form = comment_el.next();
		comment_textarea = comment_form.children('textarea').hide();
		comment_form.show();
		comment_textarea.show();
		comment_el.hide();
		comment_textarea.focus();
		$('.comment-action-btn').hide();
	});

	$('.comment-cancel-btn').click(function(e){
		e.preventDefault();
		comment_form = $(this).closest(".comment-frm");
		comment_el = comment_form.prev();
		original_text = comment_el.text();
		comment_textarea = comment_form.children('textarea');
		comment_textarea.val(original_text);
		comment_form.hide();
		comment_el.show();
		$('.comment-action-btn').show();
	});

});