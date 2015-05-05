$(document).ready(function() {
  $('#aside').append('<div class="sw" id="sw"><div class="line"></div><div class="line"></div><div class="line"></div></div>');
  $('#aside').toggleClass('collapsed');
  $("#sw").click(function(){
    $("#aside").toggleClass('collapsed');
  });
});