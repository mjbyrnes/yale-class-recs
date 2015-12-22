function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
var csrftoken = getCookie('csrftoken');
$(function() {
  $(".btn-sub").click(function() {
    var id = $(this).attr("id")
    var dataString = 'cid='+ id;
    $.ajax({
      type: "POST",
      url: "/yale_class_recs/search/",
      data: dataString,
      success: function() {
        document.getElementById(id).html("<div class=\"btn btn-md btn-success btn-default\">Added</div>");
      }
    });
    return false;
  });
});




