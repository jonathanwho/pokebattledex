/**
 * Method checks whether or not this |elm| is visible.
 * @return True if onscreen, False otherwise
 */
function onscreen(elm) { 
  try {
    var windowHeight = $(window).height(), // Viewport Height
     distanceToTop = $(window).scrollTop(), // Scroll Top
     elementHeight = $(elm).offset().top + $(elm).height();
  } catch (err) {
    console.log(err);
    return false;
  } 
  console.log("onscreen is: " + (elementHeight < (windowHeight + distanceToTop))) 
  console.log("elementHeight == " + elementHeight)
  console.log("windowHeight + distanceToTop  == " + (windowHeight + distanceToTop)) 
  return (Math.abs(elementHeight) < Math.abs(windowHeight + distanceToTop));
}

/**
 * @param The original string.
 * @return The original string with the first letter capitalized.
 */
function capitaliseFirstLetter(string)
{
  return string.charAt(0).toUpperCase() + string.slice(1);
}

/**
 * Sends an AJAX request 
 */
function get_pokemon(pokemon_name, scroll) {  
  pokemon_name = capitaliseFirstLetter(pokemon_name.trim());

  // removes the currently selected pokemon and highlights the current one
  $('li').removeClass("active"); 
  var pokemon_element = $("[id='" + pokemon_name + "']");
  pokemon_element.addClass('active'); 
  console.log("scroll is : " + scroll);
  
  // scrolls down the the currently selected pokemon
  if (scroll && !onscreen(pokemon_element)) {
    var container = $('.sidebar'); 
    var element = $('.active'); 
    try {
      var offset = element.offset().top - container.offset().top + container.scrollTop(); 
      container.scrollTop(Math.abs(offset));

      container.animate({
          scrollTop: offset
      });
    } catch (err) { console.log(err); }
  }
  
  // sends an AJAX request to get pokemon data 
  $.ajax({
    type: "GET",
    url: "/stats/" + pokemon_name,
    success: function(data){
      // json = $.parseJSON(data);
      // console.log(json.atk);
      $('#data').html(data); 
    },
    error: function(msg) {
      $('#data').html("\"" + pokemon_name + "\" is not in the database."); 
    }
  });
}

/**
 * Adds a list of pokemon for the input autocompletion.
 * @param pokemon_list The list of pokemon.
 */ 
function add_pokemon(pokemon_list) { 
  $("#pokemon_input").autocomplete({
    source: pokemon_list,
    // change: function(event, ui) {
    //   console.log("Change: " + ui.item.value); 
    //   get_pokemon(this.value);
    // },
    select: function(event, ui) {
      console.log("Selected: " + ui.item.value); 
      get_pokemon(ui.item.value, true);
    }
  });
}

$(function() { 
  $("#search").submit(function() {
    get_pokemon($("#pokemon_input").val(), true);
    return false;
  });
  $('li').on('click', function (e) { 
    e.preventDefault(); 
    var pokemon = this.children[0].text;
    get_pokemon(pokemon, false);
    $("#pokemon_input").val(pokemon);
  }); 
});