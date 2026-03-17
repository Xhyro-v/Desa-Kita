const btn = document.getElementById("menu-btn");
const sidebar = document.getElementById("sidebar");

btn.addEventListener("click", () => {
  sidebar.classList.toggle("active");
});