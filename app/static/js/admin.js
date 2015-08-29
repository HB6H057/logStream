$(document).ready(function(){
  $(".addCategoryBtn").on('click', function(){
    cate_name = $(".newCategoryName").val();
    console.log(cate_name)
    $.post("/manage/category/get", { category: cate_name }).done(function(data){
      console.log(data.success)
      if (data.success == true){
        $(".selCategory").html(data.html)
      }else{
        console.log('fail')
        alert('jQuery说到: 添加失败啊 老大 你怎么写的程序!!!!');
      }
    }, "json");
  });
});
