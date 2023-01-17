$(document).ready(function() {
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
  });


  $('form').submit(function(e) {
    e.preventDefault();
    var data = {
    'username': $('input[name="username"]').val(),
    'email': $('input[name="email"]').val()
    };
    $.ajax({
    type: 'POST',
    url: '/update/' + userId,
    data: data,
    success: function() {
    alert('Les données ont été mises à jour avec succès!');
    }
    });
    });