var searchVisible = 0;
var transparent = true;

var transparentDemo = true;
var fixedTop = false;

var navbar_initialized = false;

$(document).ready(function(){
    window_width = $(window).width();

    if($('.datepicker').length != 0){
        $('.datepicker').datepicker({
             weekStart:1,
             color: '{color}'
         });
    }

    // Init popovers
    gsdk.initPopovers();

});

gsdk = {
    misc:{
        navbar_menu_visible: 0
    },

    initPopovers: function(){
        if($('[data-toggle="popover"]').length != 0){
            $('body').append('<div class="popover-filter"></div>');

            //    Activate Popovers
           $('[data-toggle="popover"]').popover().on('show.bs.popover', function () {
                $('.popover-filter').click(function(){
                    $(this).removeClass('in');
                    $('[data-toggle="popover"]').popover('hide');
                });
                $('.popover-filter').addClass('in');
            }).on('hide.bs.popover', function(){
                $('.popover-filter').removeClass('in');
            });

        }
    },
}

$(".form-control").keyup(function () {
    //split the current value of searchInput
    var data = this.value.split(" ");
    //create a jquery object of the rows
    var jo = $(".content").find("tr");
    if (this.value == "") {
        jo.show();
        return;
    }
    //hide all the rows
    jo.hide();

    //Recusively filter the jquery object to get results.
    jo.filter(function (i, v) {
        var $t = $(this);
        for (var d = 0; d < data.length; ++d) {
            if ($t.is(":contains('" + data[d] + "')")) {
                return true;
            }
        }
        return false;
    })
    //show the rows that match.
    .show();
}).focus(function () {
    this.value = "";
    $(this).css({
        "color": "black"
    });
    $(this).unbind('focus');
}).css({
    "color": "#C0C0C0"
});



function validate(){
  var pass1 = document.getElementById("password").value
  var pass2 = document.getElementById("password_confirmation").value
   if( pass1 != pass2 ){
      alert( "Passwords don't match!" );
      document.getElementById("password").focus();
      return false;
   }
   var inputs = document.forms["registration_form"].getElementsByTagName("input");
   for(var i=0; i<inputs.length; i++) {
     if(!inputs[i].value) {
       alert("Empty fields not allowed");
       return false;
     }
   }
   return( true );
}

