// 이전 페이지로 이동하는 함수
function goBack() {
  window.history.back();
}

// 뒤로가기 버튼 클릭 시 이벤트 처리
var backButton = document.getElementById("back");
backButton.addEventListener("click", goBack);

// 스와이프 동작 감지를 위한 변수 설정
var touchStartX = 0;
var touchEndX = 0;

// 터치 시작 위치 저장
window.addEventListener("touchstart", function (event) {
  touchStartX = event.changedTouches[0].screenX;
});

// 터치 종료 위치 저장 및 스와이프 동작 확인
window.addEventListener("touchend", function (event) {
  touchEndX = event.changedTouches[0].screenX;
  handleSwipe();
});

// 스와이프 동작 처리
function handleSwipe() {
  var swipeDistance = touchEndX - touchStartX;
  var minSwipeDistance = 100; // 최소한으로 인식할 스와이프 거리

  if (swipeDistance >= minSwipeDistance) {
    goBack();
  }
}
