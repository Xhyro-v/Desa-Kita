document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebar-overlay');
    const menuBtn = document.getElementById('menu-btn');
    const closeBtn = document.getElementById('close-btn');
    const dropdowns = document.querySelectorAll('.dropdown');

    // Toggle Sidebar
    function toggleSidebar() {
        sidebar.classList.toggle('active');
        overlay.classList.toggle('active');
    }

    menuBtn.addEventListener('click', toggleSidebar);
    closeBtn.addEventListener('click', toggleSidebar);
    overlay.addEventListener('click', toggleSidebar);

    // Dropdown Logic
    dropdowns.forEach(dropdown => {
        const btn = dropdown.querySelector('.dropdown-btn');
        btn.addEventListener('click', () => {
            // Tutup dropdown lain jika ingin (optional)
            // dropdowns.forEach(d => d !== dropdown && d.classList.remove('open'));
            
            dropdown.classList.toggle('open');
        });
    });
});