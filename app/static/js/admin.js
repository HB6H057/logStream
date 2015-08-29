$(document).ready(function(){
  $(".addCategoryBtn").on('click', function(){
    cate_name = $(".newCategoryName").val();
    console.log(cate_name)
    $.post("/manage/category/get", { category: cate_name }).done(function(success){
      if (success = 'True'){
        console.log('success')
        window.location.href=window.location.href;
      }else{
        console.log('fail')
        alert('jquery: 添加失败啊 老大 你怎么写的程序!!!!');
      }
    });
  });
});
