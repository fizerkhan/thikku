$(document).ready(function() {
  var $result = $('#result');
  var $message = $('#message');
  var $submitBtn = $('#submit');

  $('#clear').click(function(e) {
    e.preventDefault();
    $result.html('');
    $message.val('');
  });

  $('#form-direction').submit(function() {
      $result.html('');

      var message = $message.val();
      if (!message) {
        $result.html('Message cannot be empty.');
        return false;
      }

      var array = message.split(':');
      if (array.length !== 2 || !array[0] || !array[1]) {
        $result.html('Message must be in the format of Origin:Destination');
        return false;
      }

      var action = $(this).attr('action');
      $submitBtn.attr('disabled','disabled');
      $.ajax({
          url: action,
          type: 'POST',
          data: 'message=' + message,
          success: function(data){
            $submitBtn.removeAttr('disabled');
            $result.html('');
            $message.val(data);
          },
          error: function(data) {
            $submitBtn.removeAttr('disabled');
            $result.html('Sorry, an error occurred. ' + data.responseText);
          }
      });
      return false;
  });

});
