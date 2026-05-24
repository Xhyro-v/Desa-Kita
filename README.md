# Citizen Report App (Desa-Kita)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F27?style=for-the-badge&logo=sqlalchemy&logoColor=white)

Aplikasi web untuk pelaporan warga yang dibuat dengan tujuan sederhana: membuat sistem RT/RW yang biasanya ribet jadi lebih rapi, cepat, dan bisa dilacak.

---

## Latar Belakang & Solusi

### Masalah yang Sering Terjadi
Di banyak lingkungan RT/RW, pelaporan masih pakai cara lama:
- Kertas (yang gampang hilang atau numpuk)
- Chat grup (yang tenggelam di antara pesan lain)
- Atau Laporan secara langsung

Akhirnya:
- Laporan sering terlewat
- Status nggak jelas
- Pengurus juga bingung tracking mana yang sudah ditangani

### Solusi yang Dibuat
**Desa-Kita** hadir sebagai platform terpusat.

Warga bisa:
- Kirim laporan langsung (real-time)
- Lihat status laporan
- Dapat pengumuman resmi tanpa harus scroll chat panjang

Di sisi lain, pengurus bisa:
- Mengelola laporan lebih terstruktur
- Memantau progress tanpa ribet

Intinya, lebih transparan dan tidak membuang waktu.

---

## Demo Aplikasi

### Video Pemakaian
Berisi cara penggunaan dari sisi warga dan admin.

[► Tonton Video Demo Pemakaian](Link_Video_YouTube_Atau_Drive_Lu_Di_Sini)

### Screenshot Tampilan

| Halaman Warga | Dashboard Admin |
| :--- | :--- |
| ![Warga UI](https://via.placeholder.com/400x250?text=Screenshot+Halaman+Warga) | ![Admin UI](https://via.placeholder.com/400x250?text=Screenshot+Dashboard+Admin) |

| Pengumuman | Status Laporan |
| :--- | :--- |
| ![Announcement UI](https://via.placeholder.com/400x250?text=Screenshot+Pengumuman) | ![Status UI](https://via.placeholder.com/400x250?text=Screenshot+Status+Laporan) |

---

## Fitur Utama

- Sistem autentikasi dengan role (Warga & Admin)
- Dashboard khusus admin untuk monitoring
- Sistem pengumuman terpusat
- Manajemen laporan dengan halaman detail
- Status laporan yang berubah secara dinamis
- Tampilan responsive (HP dan desktop masih enak dipakai)

---

## Alur Status Laporan

```mermaid
graph LR
    A[Pending] --> B[In Progress]
    B --> C[Approved]
    B --> D[Rejected]