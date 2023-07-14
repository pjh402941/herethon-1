function handleSubmit(event) {
  event.preventDefault(); // 기본 제출 동작 방지

  // main.html로 이동
  window.location.href = "/pages/main/main-location.html";
}

// form 제출 이벤트 핸들러 연결
const form = document.querySelector(".form");
form.addEventListener("submit", handleSubmit);
