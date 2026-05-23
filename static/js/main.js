document.addEventListener("DOMContentLoaded", function () {

    const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("sidebar-overlay");
    const menuBtn = document.getElementById("menu-btn");
    const closeBtn = document.getElementById("close-btn");
    const dropdowns = document.querySelectorAll(".dropdown");

    function toggleSidebar() {
        sidebar.classList.toggle("active");
        overlay.classList.toggle("active");
    }

    if (menuBtn) menuBtn.addEventListener("click", toggleSidebar);
    if (closeBtn) closeBtn.addEventListener("click", toggleSidebar);
    if (overlay) overlay.addEventListener("click", toggleSidebar);

    dropdowns.forEach(dropdown => {
        const btn = dropdown.querySelector(".dropdown-btn");
        if (btn) {
            btn.addEventListener("click", () => {
                dropdown.classList.toggle("open");
            });
        }
    });

    const modal = document.getElementById("modalKonfirmasi");
    const btnBatal = document.getElementById("btnBatal");
    const btnKonfirmasi = document.getElementById("btnKonfirmasi");

    const modalTitle = document.getElementById("modalTitle");
    const modalMessage = document.getElementById("modalMessage");

    const formGlobal = document.getElementById("formGlobal");

    let selectedAction = null;

    window.openModal = function ({ title, message, action, type = "warning" }) {
        if (!modal) return;

        modalTitle.innerText = title;
        modalMessage.innerText = message;
        selectedAction = action;

        const modalCard = modal.querySelector(".modal-card");
        const icon = modal.querySelector(".modal-icon i");

        modalCard.classList.remove("warning", "success", "submit");
        modalCard.classList.add(type);

        if (type === "warning") {
            icon.className = "fa-solid fa-triangle-exclamation";
        } else if (type === "submit") {
            icon.className = "fa-solid fa-paper-plane";
        } else if (type === "success") {
            icon.className = "fa-solid fa-circle-check";
        }

        btnKonfirmasi.classList.remove("btn-hapus", "btn-success");

        if (type === "warning") {
            btnKonfirmasi.classList.add("btn-hapus");
        } else {
            btnKonfirmasi.classList.add("btn-success");
        }

        modal.style.display = "flex";
    };

    if (btnBatal) {
        btnBatal.addEventListener("click", () => {
            modal.style.display = "none";
            selectedAction = null;
        });
    }

    if (modal) {
        modal.addEventListener("click", e => {
            if (e.target === modal) {
                modal.style.display = "none";
            }
        });
    }

    if (btnKonfirmasi) {
        btnKonfirmasi.addEventListener("click", () => {
            if (!selectedAction) return;
            selectedAction();
            modal.style.display = "none";
        });
    }

    window.handleDeleteAnnouncement = function (id) {
        openModal({
            title: "Hapus Pengumuman?",
            message: "Data tidak bisa dikembalikan.",
            type: "warning",
            action: () => {
                formGlobal.action = "/announcement/delete/" + id;
                formGlobal.submit();
            }
        });
    };

    window.handleDeleteReport = function (id) {
        openModal({
            title: "Hapus Laporan?",
            message: "Data tidak bisa dikembalikan.",
            type: "warning",
            action: () => {
                formGlobal.action = "/report/delete/" + id;
                formGlobal.submit();
            }
        });
    };

});


function handleSubmitAnnouncement() {
    const form = document.getElementById("formAnnouncement");

    if (!form) return;

    if (!form.checkValidity()) {
        form.reportValidity();
        return;
    }

    form.submit();
}

function handleSubmitReport() {
    const form = document.querySelector(".report-form-card form");

    if (!form.checkValidity()) {
        form.reportValidity();
        return;
    }

    openModal({
        title: "Kirim Laporan?",
        message: "Pastikan semua data sudah benar.",
        type: "submit",
        action: () => {
            form.submit();
        }
    });
}

function closeSuccessModal() {
    document.getElementById("modalSuccess").style.display = "none";
}

window.onload = function () {
    const urlParams = new URLSearchParams(window.location.search);

    if (urlParams.get("success") === "1") {
        const modalSuccess = document.getElementById("modalSuccess");
        modalSuccess.style.display = "flex";

        const currentPath = window.location.pathname;
        const id = urlParams.get("id");
        const btn = document.getElementById("btnCekLaporan");

        if (currentPath.includes("report")) {
            if (id) {
                btn.onclick = () => {
                    window.location.href = "/report/" + id + "/inspect";
                };
            } else {
                btn.onclick = () => {
                    window.location.href = "/report/laporan-saya";
                };
            }
        }

        else if (currentPath.includes("announcement")) {
            btn.innerText = "Lihat Pengumuman";

            if (id) {
                btn.onclick = () => {
                    window.location.href = "/announcement";
                };
            } else {
                btn.onclick = () => {
                    window.location.href = "/announcement";
                };
            }
        }

        window.history.replaceState({}, document.title, currentPath);
    }
};