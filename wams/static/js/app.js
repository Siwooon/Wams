

$(document).ready(function() {
  // $('input[name="bonne_reponse"]').hide();

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

  function ajouterTag(newTag){
    if(document.getElementById("Etiquette").value == ""){
      document.getElementById("Etiquette").value += newTag;
    }else{
      if (!document.getElementById("Etiquette").value.includes(newTag)){
      document.getElementById("Etiquette").value += ", " + newTag;
      }
    }
    }

  $(".tagButton").click(function(){
    ajouterTag(this.id)});

  $(".plus").click(function(){
    document.getElementById("submitCustomTags").style.visibility = 'visible';
    document.getElementById("addTags").style.visibility = 'visible';
  });

  $(".submitCustomTags").click(function(){
    document.getElementById("addTags").style.visibility = 'hidden';
    document.getElementById("submitCustomTags").style.visibility = 'hidden';
    ajouterTag(document.getElementById("addTags").value);
    document.getElementById("addTags").value = "";
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
        $('[name="Réponse1"]').val(data.Réponse1);
        $('[name="Réponse2"]').val(data.Réponse2);
        $('[name="Réponse3"]').val(data.Réponse3);
        $('[name="Réponse4"]').val(data.Réponse4);
        $('[name="bonne_reponse"]').val(data.bonne_reponse);
        Réponse1Button = document.getElementById("R1")
        Réponse1Button.innerHTML = $('[name="Réponse1"]').val();
        Réponse2Button = document.getElementById("R2")
        Réponse2Button.innerHTML = $('[name="Réponse2"]').val();
        Réponse3Button = document.getElementById("R3")
        Réponse3Button.innerHTML = $('[name="Réponse3"]').val();
        Réponse4Button = document.getElementById("R4")
        Réponse4Button.innerHTML = $('[name="Réponse4"]').val();

        if ($('[name="bonne_reponse"]').val()==$('[name="Réponse1"]').val()) {
          radiobtn = document.getElementById("BonneRéponse1");
          radiobtn.checked = true;
        } else if ($('[name="bonne_reponse"]').val()==$('[name="Réponse2"]').val()) {
          radiobtn = document.getElementById("BonneRéponse2");
          radiobtn.checked = true;
        } else if ($('[name="bonne_reponse"]').val()==$('[name="Réponse3"]').val()) {
          radiobtn = document.getElementById("BonneRéponse3");
          radiobtn.checked = true;
        } else if ($('[name="bonne_reponse"]').val()==$('[name="Réponse4"]').val()) {
          radiobtn = document.getElementById("BonneRéponse4");
          radiobtn.checked = true;
        } 

        
      }
    });
  });

  $(document).on('click', '.pageQuestionButton', function() {
    $(this).remove();
  });

  $("#reset-button").click(function(){
  $('[name="Label"]').val("");
  $('[name="Etiquette"]').val("");
  $('[name="Question"]').val("");
  $('[name="Réponse1"]').val("");
  $('[name="Réponse2"]').val("");
  $('[name="Réponse3"]').val("");
  $('[name="Réponse4"]').val("");
  $('[name="bonne_reponse"]').val("");
  $('#a').empty()

  radiobtn1 = document.getElementById("BonneRéponse1");
  radiobtn.checked = false;
  radiobtn2 = document.getElementById("BonneRéponse2");
  radiobtn.checked = false;
  radiobtn3 = document.getElementById("BonneRéponse3");
  radiobtn.checked = false;
  radiobtn4 = document.getElementById("BonneRéponse4");
  radiobtn.checked = false;
  Réponse1Button.innerHTML = null
  Réponse2Button.innerHTML = null
  Réponse3Button.innerHTML = null
  Réponse4Button.innerHTML = null
});

$('#BonneRéponse1').change(function(){
  $('[name="bonne_reponse"]').val($('[name="Réponse1"]').val());
})

$('#BonneRéponse2').change(function(){
  $('[name="bonne_reponse"]').val($('[name="Réponse2"]').val());
})

$('#BonneRéponse3').change(function(){
  $('[name="bonne_reponse"]').val($('[name="Réponse3"]').val());
})

$('#BonneRéponse4').change(function(){
  $('[name="bonne_reponse"]').val($('[name="Réponse4"]').val());
})





        


});

