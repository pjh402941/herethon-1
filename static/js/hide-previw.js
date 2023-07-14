function setImageFn(f, previewId, targetId) {
  var file = f.files;

  if (!/\.(gif|jpg|jpeg|png)$/i.test(file[0].name)) {
    alert("gif, jpg, png 파일만 선택해 주세요.\n\n현재 파일: " + file[0].name);

    f.value = "";

    if (previewId === "profile-upload") {
      document.getElementById(targetId).innerHTML = "";
    } else if (previewId === "reupload") {
      document.getElementById(targetId).innerHTML = "";
    }
  } else {
    var reader = new FileReader();

    reader.onload = function (rst) {
      if (previewId === "profile-upload") {
        document.getElementById(targetId).innerHTML =
          '<img src="' + rst.target.result + '">';
      } else if (previewId === "reupload") {
        document.getElementById(targetId).innerHTML =
          '<img src="' + rst.target.result + '">';
      }
    };

    reader.readAsDataURL(file[0]);
  }
}
