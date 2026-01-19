
# Laporan Praktikum Minggu 14
Topik: Penyusunan Laporan Praktikum Format IMRAD

---

## Identitas
- **Nama**  : Pasya Awan Rizky Saputro  
- **NIM**   : 250202959  
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menyusun laporan praktikum dengan struktur ilmiah (Pendahuluan–Metode–Hasil–Pembahasan–Kesimpulan).
2. Menyajikan hasil uji dalam bentuk tabel dan/atau grafik yang jelas.
3. Menuliskan analisis hasil dengan argumentasi yang logis.
4. Menyusun sitasi dan daftar pustaka dengan format yang konsisten.
5. Mengunggah draft laporan ke repositori dengan rapi dan tepat waktu.

---

## Dasar Teori
Pada pertemuan ini, mahasiswa menyusun **laporan praktikum ilmiah** secara sistematis menggunakan format **IMRAD** (_Introduction, Methods, Results, and Discussion_) yang ditutup dengan **Kesimpulan**.

Laporan IMRAD digunakan untuk merangkum praktikum-praktikum sebelumnya (mis. scheduling, page replacement, deadlock detection, VM/Docker) agar hasil uji dapat dipahami, direplikasi, dan dievaluasi secara akademik.

---

## Ketentuan Teknis
- Laporan ditulis dalam ``Markdown`` pada file ``laporan.md``.
- Topik laporan boleh memilih salah satu dari praktikum sebelumnya:
  - Scheduling (FCFS/SJF)
  - Page Replacement (FIFO/LRU)
  - Deadlock Detection
  - VM/Docker (resource management)
- Wajib menyertakan minimal:
  - 1 tabel hasil (atau lebih)
   - 1 gambar (screenshot, diagram, atau grafik)
   - sitasi dan daftar pustaka

Struktur folder (sesuaikan dengan template repo):
```bash
praktikum/week14-laporan-imrad/
├─ code/
│  └─ (opsional) file kode/data pendukung
├─ screenshots/
│  ├─ (wajib) bukti hasil uji
│  └─ (opsional) grafik/diagram
└─ laporan.md
```

---

## Langkah Praktikum
1. **Menentukan Topik Laporan**  
Pilih 1 topik dari praktikum sebelumnya (mis. Minggu 9/10/11/13) dan tetapkan tujuan eksperimen yang ingin disampaikan.
2. **Menyiapkan Bahan**
     - Kode/program yang digunakan.
     - Dataset/parameter uji (jika ada).
     - Bukti hasil eksekusi (screenshot) dan/atau grafik.
3. **Menulis Laporan dengan Struktur IMRAD**  
Tulis ``praktikum/week14-laporan-imrad/laporan.md`` dengan struktur minimal berikut:
   - **Pendahuluan (Introduction)**: latar belakang, rumusan masalah/tujuan.
   - **Metode (Methods)**: lingkungan uji, langkah eksperimen, parameter/dataset, cara pengukuran.
   - **Hasil (Results)**: tabel/grafik hasil uji, ringkasan temuan.
   - **Pembahasan (Discussion)**: interpretasi hasil, keterbatasan, perbandingan teori/ekspektasi.
   - **Kesimpulan**: 2–4 poin ringkas menjawab tujuan.     
4. **Menyajikan Tabel/Grafik**  
     - Tabel harus diberi judul/keterangan singkat.
     - Jika menggunakan grafik: jelaskan sumbu dan arti grafik.   
5. **Sitasi dan Daftar Pustaka**
     - Cantumkan referensi minimal 2 sumber.
     - Gunakan format konsisten (mis. daftar bernomor).
6. **Commit & Push Draft**
     ```bash
     git add .
     git commit -m "Minggu 14 - Draft Laporan IMRAD"
     git push origin main
     ``` 

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash

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
1. Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?  
   **Jawaban:**  
2. Apa perbedaan antara bagian Hasil dan Pembahasan?  
   **Jawaban:**  
3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
