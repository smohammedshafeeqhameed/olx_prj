$( document ).ready(function() {

$("#search-btn").on('click', function(){
    var times = "<i class=\"fas fa-times\"></i>"
    var search = "<i class=\"fas fa-search\"></i>"
    if($(this).attr("class").indexOf("active") !==-1){
    $("#search-btn").html(times)
    $("#search-btn").removeClass("active")
    $("#search-btn").removeClass("btn-outline-danger")

    }
    else{
        console.log("h1")
    $("#search-btn").html(search)
    $("#search-btn").addClass("active")
    }
})
function form_submit() {
    document.getElementById("delete-form").submit();
   }
$( '#table-body' ).on( 'click', 'a', function( event ) {
    let id = $(this).attr('id')
    console.log(id)
    let val = false
    if(id){
        val = confirm("Are u sure?")
    }
    if(val == true) {
      document.getElementById("delete-form-"+id).submit();
   } 
  });
});

$('.collapseToggle').on('click', function() {
	$(".vertical-nav").toggleClass('collapse-side');
    $(".nav-link").toggleClass('collapse-side');
	$('.media').toggleClass('media-collapse');
    $('.link-text').toggleClass('menu-text');	
    $('#toggleIcon').toggleClass('rotate');
});
