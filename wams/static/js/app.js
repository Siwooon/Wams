

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
      document.getElementById("Etiquette").value += "," + newTag;
      }
      else{
        if(document.getElementById("Etiquette").value == newTag){
          document.getElementById("Etiquette").value = "";
        }else if(document.getElementById("Etiquette").value.startsWith(newTag+",")){
          document.getElementById("Etiquette").value = document.getElementById("Etiquette").value.replace(newTag+",", "");
        }else if(document.getElementById("Etiquette").value.startsWith(","+newTag, document.getElementById("Etiquette").length - newTag.length)){
          document.getElementById("Etiquette").value = document.getElementById("Etiquette").value.replace(","+newTag, "");
        }else document.getElementById("Etiquette").value = document.getElementById("Etiquette").value.replace(","+newTag, "");
      }
    }
    }

  $(".tagButton").click(function(){
    ajouterTag(this.id)});

  $(".plus").click(function(){
    tagListPlus = document.getElementsByClassName("tagButtonPlus");
    document.getElementById("submitCustomTags").style.display = 'block';
    document.getElementById("addTags").style.display = 'block';
    for (var i = 0 ; i < tagListPlus.length ; i++){
      tagListPlus[i].style.display='block';
    }
    this.style.display = 'none';
    document.getElementById("moins").style.display = 'block';
  });
  
  $(".moins").click(function(){
    tagListPlus = document.getElementsByClassName("tagButtonPlus");
    document.getElementById("submitCustomTags").style.display = 'none';
    document.getElementById("addTags").style.display = 'none';
    for (var i = 0 ; i < tagListPlus.length ; i++){
      tagListPlus[i].style.display='none';
    }
    this.style.display = 'none';
    document.getElementById("plus").style.display = 'block';
  });

  $(".submitCustomTags").click(function(){
    document.getElementById("addTags").style.display = 'none';
    document.getElementById("submitCustomTags").style.display = 'none';
    ajouterTag(document.getElementById("addTags").value);
    document.getElementById("addTags").value = "";
  });
  
  var listeQuestions= [];
  $('.update-button').click(function() {
    var sto = $(this).text();
    listeQuestions.push(sto);
    console.log(listeQuestions);

    var clonedButton = $(this).clone().removeClass('update-button').addClass('pageQuestionButton');
    $('#pageQuestions').append(clonedButton);
    $('#pageQuestions').append("<br>");

    var QuestionId = $(this).data('id');

    

    Réponse1Button = document.getElementById("R1")

    Réponse2Button = document.getElementById("R2")

    Réponse3Button = document.getElementById("R3")

    Réponse4Button = document.getElementById("R4")

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
        Réponse1Button.innerHTML = $('[name="Réponse1"]').val();
        Réponse2Button.innerHTML = $('[name="Réponse2"]').val();
        Réponse3Button.innerHTML = $('[name="Réponse3"]').val();
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
    var sto = $(this).text();
    var index = listeQuestions.indexOf(sto);
    listeQuestions.splice(index, 1);
    
    console.log(listeQuestions);
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
  radiobtn1.checked = false;
  radiobtn2 = document.getElementById("BonneRéponse2");
  radiobtn2.checked = false;
  radiobtn3 = document.getElementById("BonneRéponse3");
  radiobtn3.checked = false;
  radiobtn4 = document.getElementById("BonneRéponse4");
  radiobtn4.checked = false;
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

$("#envoyerPageQuestions").click(function() {
  $.ajax({
    type: "POST",
    url: "/add",
    data: listeQuestions,
    success: function() {
      console.log("Questionnaire ajouté !")
    }

  })



})





        


});

