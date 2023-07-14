document.addEventListener("DOMContentLoaded", function () {
  var nickname = document.getElementById("nickname");

  nickname.addEventListener("click", function () {
    // div 내용을 가져옴
    var divContent = this.innerHTML;

    // input 요소를 생성하고 div를 대체함
    var input = document.createElement("input");
    input.value = divContent;
    input.id = "new-input";

    // div를 input으로 대체
    this.parentNode.replaceChild(input, this);

    // input에 포커스를 설정
    input.focus();
  });
});
