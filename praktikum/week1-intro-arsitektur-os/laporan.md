
# Laporan Praktikum Minggu 1
"Arsitektur Sistem Operasi dan Kernel"

---

## Identitas
- **Nama**  : Pasya Awan Rizky Saputro  
- **NIM**   : 250202959 
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan peran sistem operasi dalam arsitektur komputer.
2. Mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
3. Membandingkan model arsitektur OS (monolithic, layered, microkernel).
4. Menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu digital (draw.io / mermaid).

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari **arsitektur dasar sistem operasi**: bagaimana komponen OS bekerja, serta bagaimana interaksi antara user, aplikasi, kernel, dan hardware terjadi.  

Mahasiswa juga diperkenalkan pada:
- Perbedaan mode eksekusi **kernel mode** dan **user mode**.
- Mekanisme **system call** (panggilan sistem).
- Perbandingan model arsitektur OS seperti **monolithic kernel**, **layered approach**, dan **microkernel**.

Eksperimen akan dilakukan menggunakan perintah dasar Linux untuk melihat informasi kernel dan modul aktif.

---

## Langkah Praktikum
1. **Setup Environment**
   - Pastikan Linux (Ubuntu/WSL) sudah terinstal.
   - Pastikan Git sudah dikonfigurasi dengan benar:
     ```bash
     git config --global user.name "Nama Anda"
     git config --global user.email "email@contoh.com"
     ```

2. **Diskusi Konsep**
   - Baca materi pengantar tentang komponen OS.
   - Identifikasi komponen yang ada pada Linux/Windows/Android.

3. **Eksperimen Dasar**
   Jalankan perintah berikut di terminal:
   ```bash
   uname -a
   whoami
   lsmod | head
   dmesg | head
   ```
   Catat dan analisis modul kernel yang tampil.

4. **Membuat Diagram Arsitektur**
   - Buat diagram hubungan antara *User → System Call → Kernel → Hardware.*
   - Gunakan **draw.io** atau **Mermaid**.
   - Simpan hasilnya di:
     ```
     praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png
     ```

5. **Penulisan Laporan**
   - Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam `laporan.md`.
   - Tambahkan screenshot hasil terminal ke folder `screenshots/`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
whoami
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/linux-minggu1.png)

---

## Analisis
- Makna hasil percobaan
   * uname -a Linux atau sistem Unix-like itu berguna untuk mengecek info dasar tentang sistem operasi yang sedang di pakai
   * whoami berguna untuk melihat identitas user yang sedang login di terminal
   * lsmod | head digunakan untuk menginspeksi daftar modul kernel aktif, yaitu komponen modular yang dapat dimuat secara dinamis untuk mendukung perangkat keras, sistem file, atau fitur jaringan tanpa memerlukan reboot sistem
   * dmesg | head digunakan untuk menampilkan pesan-pesan diagnostik dari kernel Linux dengan membatasi output hanya pada baris-baris awal
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
   * Fungsi Kernel: Kernel bertanggung jawab atas manajemen hardware dan logging internal melalui fungsi printk() (atau variannya seperti dev_info()), yang menyimpan pesan di ring buffer (struktur sirkular di memori kernel space). 
   * System Call: Akses ke ring buffer dilakukan melalui system call seperti read() pada file virtual /proc/kmsg atau /dev/kmsg (di kernel modern), yang memetakan kernel space ke user space. 
   * Arsitektur OS: Dalam arsitektur Linux (monolitik dengan ekstensi modular), dmesg merepresentasikan interaksi antara kernel core dan modul (e.g., pesan dari driver USB atau filesystem).
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
   * Perintah dan sintaks berbeda perintah terminal di Linux tidak sama dengan command prompt di Windows.

   * Struktur file dan path berbeda Linux memakai “/”, sedangkan Windows memakai “\”.

   * Output dan perilaku program bisa berbeda karena perbedaan sistem file, izin akses, dan manajemen proses.

---

## Kesimpulan
Sistem operasi berperan penting dalam mengelola seluruh sumber daya komputer agar dapat bekerja secara efisien dan terkoordinasi.

Melalui praktikum, pengguna dapat memahami cara kerja dasar manajemen proses, memori, dan file yang dilakukan oleh sistem operasi.

Pemahaman terhadap sistem operasi membantu dalam penggunaan komputer secara lebih efektif serta dalam pengembangan aplikasi yang kompatibel dengan lingkungan OS tertentu.

---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi.  
   **Jawaban:** Manajemen Proses (Process Management), Manajemen Memori (Memory Management), Manajemen Perangkat dan I/O (Device and I/O Management)  
2. Jelaskan perbedaan antara kernel mode dan user mode.  
   **Jawaban:**  Untuk kernel mode sendiri yaitu mode priviledged (berhak istimewa) di mana kernel sistem operasi (bagian inti OS seperti manajer memori, proses, dan driver perangkat) berjalan. Hanya kernel dan proses tepercaya yang bisa masuk ke mode ini. dan untuk user mode ini merupakan mode priviledged (berhak istimewa) di mana kernel sistem operasi (bagian inti OS seperti manajer memori, proses, dan driver perangkat) berjalan. Hanya kernel dan proses tepercaya yang bisa masuk ke mode ini.
3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel. 
   **Jawaban:**  untuk monolithic kernel contohnya yaitu Linux, Unix Tradisional, MS-DOS, AIX (versi awal) dan Solaris Awal. dan untuk microkernel sendiri contohnya Minix, QNX, Mach, Integrity dan L4

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
semuanya karena semua itu saya belum paham apa apa makannya saya bilang menantang semua.
- Bagaimana cara Anda mengatasinya?  
untuk diri pribadi saya cara mengatasinya tentu terus belajar dan belajar. 
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
