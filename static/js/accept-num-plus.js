// accept-num 요소들을 선택합니다.
const acceptNumElements = document.querySelectorAll("#accept-num");

// 개수를 표시할 함수를 정의합니다.
function countAcceptBox() {
  // 각 accept-num 요소를 순회하면서 값을 설정합니다.
  acceptNumElements.forEach((acceptNumElement, index) => {
    // 개수를 설정합니다.
    acceptNumElement.textContent = (index + 1).toString();
  });
}

// 페이지가 로드되면 개수를 계산하여 출력합니다.
window.addEventListener("load", countAcceptBox);
