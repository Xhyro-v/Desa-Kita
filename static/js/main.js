const btn = document.getElementById("menu-btn");
const sidebar = document.getElementById("sidebar");

btn.addEventListener("click", () => {
    sidebar.classList.toggle("active");
});

const closeBtn = document.getElementById("close-btn");
closeBtn.addEventListener("click", () => {
    sidebar.classList.remove("active");
});

document.addEventListener("click", e => {
    if (!sidebar.contains(e.target) && !btn.contains(e.target)) {
        sidebar.classList.remove("active");
    }
});
const dropdownBtn = document.querySelector(".dropdown-btn");
const dropdownContent = document.querySelector(".dropdown-content");

dropdownBtn.addEventListener("click", () => {
    dropdownContent.classList.toggle("show");
});
