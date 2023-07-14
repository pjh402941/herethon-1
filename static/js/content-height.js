var header = document.querySelector("header.hd");
var bd = document.querySelector(".bd");
var content = document.querySelector(".content");

function setBdHeight() {
  var windowHeight = window.innerHeight;
  var headerHeight = header.offsetHeight;
  var minHeight = windowHeight - headerHeight;

  bd.style.height = Math.max(minHeight) + "px";
  content.style.height = bd.style.height;
}

setBdHeight();

window.addEventListener("resize", setBdHeight);

// class가 board-list인 요소의 높이를 확인하여 처리하는 함수
function handleBoardListHeight() {
  var boardList = document.querySelector(".board-list");
  var content = document.querySelector(".content");

  if (boardList.offsetHeight <= 50) {
    content.style.backgroundColor = "#F6F6F6";
    boardList.style.paddingTop = "0";
    boardList.style.marginTop = "25px";
  } else {
    content.style.backgroundColor = "";
    boardList.style.paddingTop = "";
    boardList.style.marginTop = "";
  }
}

// 페이지 로드 시와 윈도우 크기 변경 시 이벤트 처리
window.addEventListener("load", handleBoardListHeight);
window.addEventListener("resize", handleBoardListHeight);
