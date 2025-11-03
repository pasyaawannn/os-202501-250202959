
# Laporan Praktikum Minggu 4
Topik: Proses User

---

## Identitas
- **Nama**  : Pasya Awan Rizky Saputro  
- **NIM**   : 250202959  
- **Kelas** : 1IKRB

---

## Tujuan
1. Mampu menjelaskan konsep proses dan user dalam sistem operasi Linux.
2. Mampu menampilkan daftar proses yang sedang berjalan dan statusnya.
3. Mampu menggunakan perintah untuk membuat dan mengelola user.
4. Mampu menghentikan atau mengontrol proses tertentu menggunakan PID.
5. Mampu menjelaskan kaitan antara manajemen user dan keamanan sistem.

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari **konsep proses dan manajemen user dalam sistem operasi Linux**.
Mahasiswa akan memahami bagaimana sistem operasi:

- Membuat dan mengatur proses (process management).
- Mengelola user, group, serta hak akses pengguna.
- Menampilkan, menghentikan, dan mengontrol proses yang sedang berjalan.
- Menghubungkan konsep user management dengan keamanan sistem operasi.

Eksperimen dilakukan melalui penggunaan perintah dasar seperti ```ps```, ```top```, ```kill```, ```adduser```, ```passwd```, ```id```, dan ```groups```.

---

## Langkah Praktikum
1. **Setup Environment**

   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan Anda sudah login sebagai user non-root.
   - Siapkan folder kerja.
     ```bash
     praktikum/week4-proses-user/
     ```
2. **Eksperimen 1 – Identitas User** Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.
3. **Eksperimen 2 – Monitoring Proses** Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
    - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.
    - Simpan tangkapan layar ```top``` ke:
      ```bash
      praktikum/week4-proses-user/screenshots/top.png
      ```
4. **Eksperimen 3 – Kontrol Proses**

   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses ```sleep```.
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan ```ps aux | grep sleep```.
5. **Eksperimen 4 – Analisis Hierarki Proses** Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (```init/systemd```).
   - Catat hasilnya dalam laporan.
6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
whoami
id
groups
sudo adduser praktikan
sudo passwd praktikan
ps aux | head -10
top -n 1
sleep 1000 &
ps aux | grep sleep
kill <PID>
pstree -p | head -20
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
1. Apa fungsi dari proses ```init``` atau ```systemd``` dalam sistem Linux?  
   **Jawaban:**  
2. Apa perbedaan antara ```kill``` dan ```killall```?
   **Jawaban:**  
3. Mengapa user ```root``` memiliki hak istimewa di sistem Linux? 
   **Jawaban:**  


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
