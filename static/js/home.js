$(document).ready(function(){
  var id = $(".btn-primary").attr('id');
  // $(function(){
  $('#products-tbody').find('tr').click(function(){
    $('.modal-body').text('<script src="http://dev-paywith.paytm.com/pptmbutton.min.js?button_id=51110f788b" pptmdata-custom_params="" pptmdata-muoid="'+id+'"></script>');
      var amount = $(this).children()[2].innerHTML;
      var productid = $(this).children()[0].innerHTML;
      $('#myModal').modal().on('show', function(){
    });
  });
});
