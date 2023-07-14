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

uschool.addEventListener("click", function () {
  // div 내용을 가져옴
  var divContent = this.innerHTML;

  // input 요소를 생성하고 div를 대체함
  var input = document.createElement("input");
  input.value = divContent;
  input.id = "new-input2";

  // 해제할 CSS 프로퍼티 목록
  var cssProperties = [
    "box-sizing",
    "padding",
    "border",
    "border-bottom",
    "font-size",
    "color",
    "width",
    "margin",
    "text-align",
    "font-weight",
    "position",
  ];

  // div에 적용된 CSS를 해제
  var divElement = this; // div 엘리먼트 참조를 변수에 저장
  cssProperties.forEach(function (property) {
    divElement.style.removeProperty(property);
  });

  // div를 input으로 대체
  this.parentNode.replaceChild(input, this);

  // input에 포커스를 설정
  input.focus();
});
