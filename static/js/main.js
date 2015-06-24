/**
 * Created by Катерина on 26.01.2015.
 */

$(window).ready(function() {
    $("#category").selectmenu({
        appendTo: $('#category').parent()
    });
    $("#theme").selectmenu({
        appendTo: $('#theme').parent()
    });
})


$(document).on('ready', function() {
    /*$('input[data-mask]').inputmask({
        mask: $('input[data-mask]').attr('data-mask')
    });*/

   $('#navigation').find('li').each(function() {
   		$(this).hover(function() {
   			$(this).find('.pop-wind').fadeIn();
   		}, function() {
   			$(this).find('.pop-wind').fadeOut();
   		});
   });

   $('.smooth-hover').find('li').each(function() {
   		$(this).hover(function() {
   			$(this).append('<span>' + $(this).text() + '</span>')
   			$(this).find('span').fadeIn(400);
   		}, function() {
   			$(this).find('span').remove();
   		});
   });

// Настройка радио

  var anonClickCounter = 0;
  var nonAnonCounter = 0;
  var rightStart = false;
  $('#anonymous').click(function() {
 	rightStart = true;
  	nonAnonCounter = 0;
  	anonClickCounter++;
  	changeColor($('.label-1'), '#E51E24');
  	changeColor($('.label-2'), '#6996B5');
  	if(anonClickCounter < 2 && rightStart) {
  		$('.dis-name').fadeToggle(350);
  		$('.dis-phone').fadeToggle(350);
  		$('.dis-mail').fadeToggle(350);
  		$('.text-danger').hide();
  	}
  });

  $('#non-anonymous').click(function() {
  	anonClickCounter = 0;
  	nonAnonCounter++;
  	changeColor($('.label-2'), '#E51E24');
  	changeColor($('.label-1'), '#6996B5');
  	if(nonAnonCounter < 2 && rightStart) {
  		$('.dis-name').fadeToggle(350);
  		$('.dis-phone').fadeToggle(350);
  		$('.dis-mail').fadeToggle(350);
  		$('.text-danger').show();
  	}
  });

  function changeColor(block, color) {
  		block.css({'color': color});
  }
  $('.add-comment').click(function() {
  	$('.add-comment-block').animate({height : 'toggle'}, 300);
  });
});