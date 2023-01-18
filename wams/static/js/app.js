$(document).ready(function() {

  var md = window.markdownit();  
  $('[name="Question"]').on("input", function(){
    var html = md.render($(this).val());
    $("#a").html(html);
  });


  $('.update-button').click(function() {
    var QuestionId = $(this).data('id');
    $.ajax({
      type: 'GET',
      url: '/update/' + QuestionId,
      success: function(data) {
        $('input[name="Label"]').val(data.Label);
        $('input[name="Etiquette"]').val(data.Etiquette);
        $('input[name="Question"]').val(data.Question);
        $('input[name="Réponse1"]').val(data.Réponse1);
        $('input[name="Réponse2"]').val(data.Réponse2);
        $('input[name="Réponse3"]').val(data.Réponse3);
        $('input[name="Réponse4"]').val(data.Réponse4);
        
      }
    });
  });

  
  $('[name="Label"]').on("input", function(){
      $("#text-display").text($(this).val());
  });

  $("#reset-button").click(function(){
  $('[name="Label"]').val("");
  $('[name="Etiquette"]').val("");
  $('[name="Question"]').val("");
  $('[name="Réponse1"]').val("");
  $('[name="Réponse2"]').val("");
  $('[name="Réponse3"]').val("");
  $('[name="Réponse4"]').val("");
});

        


});

