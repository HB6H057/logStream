$(document).ready(function(){
  $(".addCategoryBtn").on('click', function(){
    cate_name = $(".newCategoryName").val();
    $.get("/manage/post/delete/", { name: cate_name }).done(function(success){
      if (success = 'True'){
        alert('haha');
      }else{
        alert('hehe');
      }
    });
  });
});
