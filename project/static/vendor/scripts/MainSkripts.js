$(function(){
    $("#user-comment-button").click(function(){
        $('#popup-container').show();
    })
})

$(function(){
    $('#close-popup').click(function(){
        $('#popup-container').hide();
    })
})

$(function() {
    const disableScroll = function(event) {
      event.preventDefault();
    }
  
    $('#user-comment-button').click(function() {
      $('html, body').css('overflow', 'hidden');
      $(window).on('mousewheel', disableScroll);
    });
  });