
# Laporan Praktikum Minggu 15
Topik: Proyek Kelompok – Mini Simulasi Sistem Operasi (Scheduling + Memory + Container)

---

## Identitas
- **Nama**  : Pasya Awan Rizky Saputro  
- **NIM**   : 250202959  
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan proyek ini, mahasiswa mampu:

1. Bekerja kolaboratif dalam tim dengan pembagian peran yang jelas.
2. Mengintegrasikan beberapa konsep sistem operasi dalam satu aplikasi sederhana.
3. Mengelola proyek menggunakan Git (branch/PR/commit yang rapi).
4. Menyusun dokumentasi dan laporan proyek yang sistematis.
5. Melakukan presentasi dan demo hasil proyek.

---

## Dasar Teori
Pada pertemuan ini, mahasiswa mengerjakan **proyek kelompok** untuk mengintegrasikan materi praktikum sebelumnya menjadi satu mini-aplikasi yang **bisa didemokan dan dipresentasikan**.

Setiap kelompok membangun aplikasi berbasis terminal yang:

Mensimulasikan minimal **2 konsep OS** (contoh: CPU scheduling + page replacement, atau scheduling + deadlock detection).
Menyediakan input dataset sederhana dan menampilkan output berupa tabel/ringkasan metrik.
Dapat dijalankan melalui **Docker** untuk memastikan reproducible environment.

---

## Ketentuan Teknis
- **Kelompok**: 3–5 mahasiswa.
- Bahasa pemrograman bebas (Python / C / Java / lainnya), aplikasi berbasis terminal.
- Wajib menggunakan Git kolaboratif (minimal: pembagian branch per fitur dan merge terkontrol).
- Wajib menyediakan cara jalan yang mudah (minimal ``README.md`` + perintah run) dan **demo via Docker**.  
Struktur folder (sesuaikan dengan template repo):
```bash
praktikum/week15-proyek-kelompok/
├─ code/
│  ├─ (source code proyek)
│  ├─ Dockerfile
│  ├─ README.md
│  └─ data/ (opsional)
├─ screenshots/
│  ├─ demo_run.png
│  └─ hasil_tabel.png
└─ laporan.md
```

---
## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
