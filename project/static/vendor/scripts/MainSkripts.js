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
    const enableScroll = function(event){

    }
  
    $('#user-comment-button').click(function() {
      $('html, body').css('overflow', 'hidden');
      $(window).on('mousewheel', disableScroll);
    });

    $('#close-popup').click(function() {
      $('html, body').css('overflow', 'visible');
      $(window).on('mousewheel', enableScroll);
    });

  });