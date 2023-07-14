var input = document.getElementById("search");

input.addEventListener("keyup", function (event) {
  if (event.key === "Enter") {
    event.preventDefault();
    document.getElementById("search-submit").click();
  }
});
