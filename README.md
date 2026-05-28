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

## Installation

Clone repository:

```bash
git clone https://github.com/Xhyro-v/Desa-Kita.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn main:app --reload
```
or
```bash
python -m uvicorn main:app --reload
```

---

## Demo Aplikasi

### Screenshot Tampilan

- UI User/Warga

| Halaman Warga (1/2) | Halaman Warga(2/2) |
| :--- | :--- |
| ![Warga UI](https://github.com/user-attachments/assets/f1824c9f-9729-4ac2-b9f7-3f95d4f7ad2e) | ![Warga UI2](https://github.com/user-attachments/assets/a22b998a-2c07-417f-b6a3-e08716c5a8e7) |

- UI Pelaporan User/Warga

| Laporan | Inpeksi Laporan | Status Laporan |
| :--- | :--- | :--- |
| ![Laporan UI](https://github.com/user-attachments/assets/6ca15fd8-d1cb-46ce-beb3-482a68b9d978) | ![Inspect](https://github.com/user-attachments/assets/2941a2c1-a314-4015-ab42-b9d1dd7e911b) | ![Status Lap UI](https://github.com/user-attachments/assets/dbcca19b-2e5a-403e-9b03-61157e723c0b) |

- UI Admin/Moderator

| Pengumuman | Inpeksi Laporan | Status Laporan |
| :--- | :--- | :--- |
| ![Announcement UI](https://github.com/user-attachments/assets/17c7ebfb-cad0-4e60-b6d7-5ca5f5a672bc) | ![Inspect](https://github.com/user-attachments/assets/8c0b02d4-b540-4967-93e3-1c055eca926b) | ![Status UI](https://github.com/user-attachments/assets/8c9d5f2f-a086-4c1f-b85f-28a7c9ae0a06) |

### Video Pemakaian
Berisi cara penggunaan dari sisi warga dan admin.

[► Tonton Video Demo Pemakaian](Link_Video_YouTube_Atau_Drive_Lu_Di_Sini)

---

## Alur Status Laporan

```mermaid
graph LR
    A[Pending] --> B[In Progress]
    B --> C[Approved]
    B --> D[Rejected]
```

---

## Fitur Utama

- Sistem autentikasi dengan role (Warga & Admin)
- Dashboard khusus admin untuk monitoring
- Sistem pengumuman terpusat
- Manajemen laporan dengan halaman detail
- Status laporan yang berubah secara dinamis
- Tampilan responsive (HP dan desktop masih enak dipakai)

---

