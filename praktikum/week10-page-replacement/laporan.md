# Laporan Praktikum Minggu 10

Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Pasya Awan Rizky Saputro 
- **NIM**   : 250202959
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah _page fault_.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari **manajemen memori virtual**, khususnya mekanisme page replacement.
Fokus utama praktikum adalah memahami bagaimana sistem operasi mengganti halaman (page) di memori utama ketika terjadi page fault, serta membandingkan performa algoritma **FIFO (First-In First-Out)** dan **LRU (Least Recently Used)**.

Mahasiswa akan mengimplementasikan **program simulasi page replacement**, menjalankan dataset uji, dan menyajikan hasil dalam bentuk tabel atau grafik.

---

## Ketentuan Teknis
 - Bahasa pemrograman **bebas** (Python / C / Java / lainnya).
 - Program berbasis **terminal** (tidak wajib GUI).
 - Fokus penilaian pada **logika algoritma dan keakuratan hasil simulasi**.

Struktur folder (sesuaikan dengan template repo):
```bash
praktikum/week10-page-replacement/
├─ code/
│  ├─ page_replacement.*
│  └─ reference_string.txt
├─ screenshots/
│  └─ hasil_simulasi.png
└─ laporan.md
```

---

## Langkah Praktikum
1. **Menyiapkan Dataset**  
Gunakan _reference_ string berikut sebagai contoh:
   ```bash
   7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
   ```  
2. **Implementasi FIFO**
   - Simulasikan penggantian halaman menggunakan algoritma FIFO.
   - Catat setiap _page hit_ dan _page fault_.
   - Hitung total _page fault_.
3. **Implementasi LRU**
   - Simulasikan penggantian halaman menggunakan algoritma LRU.
   - Catat setiap _page hit_ dan _page fault_.
   - Hitung total _page fault_.  
4. **Eksekusi & Validasi**  
   - Jalankan program untuk FIFO dan LRU.
   - Pastikan hasil simulasi logis dan konsisten.
   - Simpan screenshot hasil eksekusi.
5. **Analisis Perbandingan**  
Buat tabel perbandingan seperti berikut: 

   | Algoritma | Jumlah Page Fault | Keterangan |
   | --------- | ----------------- | ---------- |
   | FIFO      | …                 | …          |
   | LRU       | …                 | …          |
   - Jelaskan mengapa jumlah _page fault_ bisa berbeda.
   - Analisis algoritma mana yang lebih efisien dan alasannya.
6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
   git push origin main
   ```   

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
- Jelaskan mengapa jumlah page fault bisa berbeda.
- Analisis algoritma mana yang lebih efisien dan alasannya.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa perbedaan utama FIFO dan LRU?  
   **Jawaban:**  
2. Mengapa FIFO dapat menghasilkan _Belady’s Anomaly_?  
   **Jawaban:**  
3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
