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


const btnHapus = document.getElementById('btnHapus');
const modalOverlay = document.getElementById('modalKonfirmasi');
const btnBatal = document.getElementById('btnBatal');
const btnKonfirmasiHapus = document.getElementById('btnKonfirmasiHapus');

btnHapus.addEventListener('click', () => {
    modalOverlay.style.display = 'flex'; 
});

btnBatal.addEventListener('click', () => {
    modalOverlay.style.display = 'none';
});


btnKonfirmasiHapus.addEventListener('click', () => {
    modalOverlay.style.display = 'none';
    
    alert("Data berhasil diproses untuk dihapus!"); 
});


window.addEventListener('click', (e) => {
    if (e.target === modalOverlay) {
        modalOverlay.style.display = 'none';
    }
});