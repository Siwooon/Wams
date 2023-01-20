

$(document).ready(function() {



  $("[name='Réponse1']").on("input", function() {
    Réponse1Button = document.getElementById("R1")
    Réponse1Button.innerHTML = $(this).val();
    
});
  $("[name='Réponse2']").on("input", function() {
    Réponse2Button = document.getElementById("R2")
    Réponse2Button.innerHTML = $(this).val();
    
  });

  $("[name='Réponse3']").on("input", function() {
    Réponse3Button = document.getElementById("R3")
    Réponse3Button.innerHTML = $(this).val();
    
  });

  

  $("[name='Réponse4']").on("input", function() {
    Réponse4Button = document.getElementById("R4")
    Réponse4Button.innerHTML = $(this).val();
    
  });

  
  

  $('.update-button').click(function() {
    var clonedButton = $(this).clone().removeClass('update-button').addClass('pageQuestionButton');
    $('#pageQuestions').append(clonedButton);
    $('#pageQuestions').append("<br>");

    var QuestionId = $(this).data('id');
    $.ajax({
      type: 'GET',
      url: '/update/' + QuestionId,
      success: function(data) {
        $('input[name="Label"]').val(data.Label);
        $('input[name="Etiquette"]').val(data.Etiquette);
        $('[name="Question"]').val(data.Question);
        //$("[name='editor']").val(data.Question);
        $('input[name="Réponse1"]').val(data.Réponse1);
        $('input[name="Réponse2"]').val(data.Réponse2);
        $('input[name="Réponse3"]').val(data.Réponse3);
        $('input[name="Réponse4"]').val(data.Réponse4);
        
        
      }
    });
  });

  $("#reset-button").click(function(){
  $('[name="Label"]').val("");
  $('[name="Etiquette"]').val("");
  $('[name="Question"]').val("");
  //$('[name="editor"]').val("");
  $('[name="Réponse1"]').val("");
  $('[name="Réponse2"]').val("");
  $('[name="Réponse3"]').val("");
  $('[name="Réponse4"]').val("");
  $('#a').empty()
});

$(document).on('click', '.pageQuestionButton', function() {
  $(this).remove();
});

        


});

