function setImageFn(f) {
  var file = f.files;

  if (!/\.(gif|jpg|jpeg|png)$/i.test(file[0].name)) {
    alert("gif, jpg, png 파일만 선택해 주세요.\n\n현재 파일 : " + file[0].name);

    f.value = "";

    document.getElementById("preview").innerHTML = "";
  } else {
    var reader = new FileReader();

    reader.onload = function (rst) {
      document.getElementById("preview").innerHTML =
        '<img src="' + rst.target.result + '">';
    };

    reader.readAsDataURL(file[0]);
  }
}
