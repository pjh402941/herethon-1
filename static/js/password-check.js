function isSame() {
  var pw = document.getElementById("upw1").value;
  var confirmPW = document.getElementById("upw2").value;
  if (pw.length < 8 || pw.length > 16) {
    window.alert("비밀번호는 6글자 이상, 16글자 이하만 이용 가능합니다.");
    document.getElementById("upw1").value = document.getElementById(
      "upw2"
    ).value = "";
    document.getElementById("same").innerHTML = "";
  }
  if (
    document.getElementById("upw1").value != "" &&
    document.getElementById("upw2").value != ""
  ) {
    if (
      document.getElementById("upw1").value ==
      document.getElementById("upw2").value
    ) {
      document.getElementById("same").innerHTML = "비밀번호가 일치합니다.";
      document.getElementById("same").style.color = "blue";
    } else {
      document.getElementById("same").innerHTML =
        "비밀번호가 일치하지 않습니다.";
      document.getElementById("same").style.color = "red";
    }
  }
}
