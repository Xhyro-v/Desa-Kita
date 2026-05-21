document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebar-overlay');
    const menuBtn = document.getElementById('menu-btn');
    const closeBtn = document.getElementById('close-btn');
    const dropdowns = document.querySelectorAll('.dropdown');

    function toggleSidebar() {
        sidebar.classList.toggle('active');
        overlay.classList.toggle('active');
    }

    menuBtn.addEventListener('click', toggleSidebar);
    closeBtn.addEventListener('click', toggleSidebar);
    overlay.addEventListener('click', toggleSidebar);

    dropdowns.forEach(dropdown => {
        const btn = dropdown.querySelector('.dropdown-btn');
        btn.addEventListener('click', () => {

            
            dropdown.classList.toggle('open');
        });
    });
});


let selectedAction = null;

const modal = document.getElementById("modalKonfirmasi");
const btnBatal = document.getElementById("btnBatal");
const btnKonfirmasi = document.getElementById("btnKonfirmasi");

const modalTitle = document.getElementById("modalTitle");
const modalMessage = document.getElementById("modalMessage");

const formGlobal = document.getElementById("formGlobal");



function openModal({ title, message, action }) {
    modalTitle.innerText = title;
    modalMessage.innerText = message;
    selectedAction = action;

    modal.style.display = "flex";
}


btnBatal.addEventListener("click", () => {
    modal.style.display = "none";
    selectedAction = null;
});





modal.addEventListener("click", (e) => {
    if (e.target === modal) {
        modal.style.display = "none";
    }
});





btnKonfirmasi.addEventListener("click", () => {
    if (!selectedAction) return;

    selectedAction(); 
    modal.style.display = "none";
});

function handleDeleteAnnouncement(id) {
    openModal({
        title: "Hapus Pengumuman?",
        message: "Data tidak bisa dikembalikan.",
        action: () => {
            const form = document.getElementById("formGlobal");
            form.action = "/announcement/delete/" + id;
            form.submit();
        }
    });
}

function handleDeleteReport(id) {
    openModal({
        title: "Hapus Laporan?",
        message: "Data tidak bisa dikembalikan.",
        action: () => {
            const form = document.getElementById("formGlobal");
            form.action = "/report/delete/" + id;
            form.submit();
        }
    });
}