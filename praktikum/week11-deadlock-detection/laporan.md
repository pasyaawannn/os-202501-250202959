
# Laporan Praktikum Minggu 11
Topik:  Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Pasya Awan Rizky Saputro  
- **NIM**   : 250202959  
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program sederhana untuk mendeteksi deadlock.
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.
4. Memberikan interpretasi hasil uji secara logis dan sistematis.
5. Menyusun laporan praktikum sesuai format yang ditentukan.

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari **mekanisme deteksi deadlock** dalam sistem operasi.
Berbeda dengan Minggu 7 yang berfokus pada pencegahan dan penghindaran deadlock, pada minggu ini mahasiswa diarahkan untuk **mendeteksi deadlock yang telah terjadi** menggunakan pendekatan algoritmik.

Mahasiswa akan membuat **program simulasi sederhana deteksi deadlock**, menjalankan dataset uji, serta menyajikan hasil analisis dalam bentuk tabel dan interpretasi logis.

---

## Ketentuan Teknis
- Bahasa pemrograman **bebas** (Python / C / Java / lainnya).
- Program berbasis **terminal**, tidak memerlukan GUI.
- Fokus penilaian pada **logika algoritma deteksi deadlock**, bukan kompleksitas bahasa.  
Struktur folder (sesuaikan dengan template repo):
  ```bash
  praktikum/week11-deadlock-detection/
  ├─ code/
  │  ├─ deadlock_detection.*
  │  └─ dataset_deadlock.csv
  ├─ screenshots/
  │  └─ hasil_deteksi.png
  └─ laporan.md
  ```

---

## Langkah Praktikum
1. **Menyiapkan Dataset**
Gunakan dataset sederhana yang berisi:
   - Daftar proses
   - Resource Allocation
   - Resource Request / Need

   Contoh tabel:
   |    Proses    | Allocation | Request |
   |    ------    | ---------- | ------- |
   |   Process1   | R1         | R2      |
   |   Process2   | R2         | R3      |
   |   Process3   | R3         | R1      |
  
2. **Implementasi Algoritma Deteksi Deadlock**
Program minimal harus:
   - Membaca data proses dan resource.
   - Menentukan apakah sistem berada dalam kondisi deadlock.
   - Menampilkan proses mana saja yang terlibat deadlock.  
3. **Eksekusi & Validasi**
   - Jalankan program dengan dataset uji.
   - Validasi hasil deteksi dengan analisis manual/logis.
   - Simpan hasil eksekusi dalam bentuk screenshot.  
4. **Analisis Hasil**
   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.
   - Kaitkan hasil dengan teori deadlock (empat kondisi).
5. **Commit & Push**
      ```bash
      git add .
      git commit -m "Minggu 11 - Deadlock Detection"
     git push origin main
      ```


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
import csv
import os

# ===============================
# Path aman ke file CSV
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "dataset_deadlock.csv")

# Cek file CSV
if not os.path.exists(CSV_FILE):
    print("ERROR: dataset_deadlock.csv tidak ditemukan!")
    print("Lokasi yang dicari:", CSV_FILE)
    exit()

# ===============================
# Membaca dataset dari CSV
# ===============================
processes = {}

with open(CSV_FILE, newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        processes[row["Process"]] = {
            "allocation": row["Allocation"],
            "request": row["Request"]
        }

# ===============================
# Membentuk Wait-For Graph
# ===============================
wait_for = {}

for p, data in processes.items():
    for other_p, other_data in processes.items():
        if data["request"] == other_data["allocation"]:
            wait_for[p] = other_p

# ===============================
# Deteksi Deadlock (Cycle)
# ===============================
deadlock = set()

def find_cycle(proc, path):
    if proc in path:
        return path[path.index(proc):]
    if proc not in wait_for:
        return None
    path.append(proc)
    return find_cycle(wait_for[proc], path)

for p in processes:
    cycle = find_cycle(p, [])
    if cycle:
        deadlock.update(cycle)

# ===============================
# Output
# ===============================
print("\n=== HASIL DETEKSI DEADLOCK ===")

if deadlock:
    print("Deadlock TERDETEKSI")
    print("Proses yang terlibat:")
    for p in sorted(deadlock):
        print("-", p)
else:
    print("Tidak terjadi deadlock")

print("\n=== STATUS PROSES ===")
for p in processes:
    status = "Deadlock" if p in deadlock else "Tidak Deadlock"
    print(f"{p} : {status}")
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/hasil_deteksi.png)

---

## Analisis
1. **Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).**  
Berdasarkan hasil eksekusi program deteksi deadlock menggunakan dataset dataset_deadlock.csv, diperoleh hasil sebagai berikut:

   | No | Proses   | Status   |
   | -- | -------- | -------- |
   | 1  | Process1 | Deadlock |
   | 2  | Process2 | Deadlock |
   | 3  | Process3 | Deadlock |
   Seluruh proses terdeteksi berada dalam kondisi deadlock karena masing-masing proses:
   - Menahan satu resource (allocation)
   - Menunggu resource lain yang sedang dipegang oleh proses berbeda

   Kondisi ini membentuk circular wait, sehingga tidak ada proses yang dapat melanjutkan eksekusi.
2. **Jelaskan mengapa deadlock terjadi atau tidak terjadi**.  
Deadlock terjadi karena setiap proses memegang satu resource dan menunggu resource lain yang dipegang proses lain, sehingga terbentuk circular wait
3. **Kaitkan hasil dengan teori deadlock (empat kondisi)**.  
Deadlock terjadi karena sistem memenuhi keempat kondisi deadlock (Coffman Conditions) secara bersamaan, yaitu:
   1. **Mutual Exclusion**  
     Setiap resource hanya dapat digunakan oleh satu proses pada satu waktu.
Pada kasus ini, resource R1, R2, dan R3 masing-masing hanya dipegang oleh satu proses, sehingga proses lain tidak dapat menggunakannya secara bersamaan.

   2. **Hold and Wait**  
Setiap proses menahan satu resource sambil menunggu resource lain.
      - Process1 menahan R1 dan menunggu R2
      - Process2 menahan R2 dan menunggu R3
      - Process3 menahan R3 dan menunggu R1
   3. **No Preemption**  
      Resource yang sudah dialokasikan tidak dapat diambil secara paksa oleh sistem.
      Resource hanya dapat dilepaskan jika proses yang memegangnya selesai atau melepasnya sendiri.
   4. **Circular Wait**  
Terjadi siklus ketergantungan antar proses:
      - Process1 → menunggu Process2
      - Process2 → menunggu Process3
      - Process3 → menunggu Process1  

      Siklus ini menyebabkan tidak ada proses yang dapat melanjutkan eksekusi.

---

## Kesimpulan
1. Deadlock dapat terjadi ketika proses saling menunggu resource sehingga membentuk circular wait, dan kondisi ini dapat diidentifikasi melalui simulasi dan algoritma deteksi deadlock.

2. Implementasi algoritma deteksi deadlock membantu sistem mengenali proses-proses yang terlibat deadlock tanpa harus membatasi alokasi resource sejak awal.

3. Praktikum ini menunjukkan bahwa deteksi deadlock penting untuk menjaga keandalan sistem operasi, terutama pada lingkungan dengan penggunaan resource yang dinamis.

---

## Quiz
1. Apa perbedaan antara deadlock prevention, avoidance, dan detection?  
   **Jawaban:**  
   - **Deadlock prevention**: Mencegah deadlock dengan menghilangkan salah satu dari empat kondisi deadlock (misalnya melarang hold and wait).
   - **Deadlock avoidance**: Menghindari deadlock dengan mengatur alokasi resource agar sistem selalu berada pada kondisi aman, contohnya menggunakan Banker’s Algorithm.  
   - **Deadlock detection**: Membiarkan deadlock terjadi, lalu mendeteksinya dan melakukan pemulihan (recovery).
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  
   **Jawaban:**  
   Deteksi deadlock diperlukan karena tidak semua sistem dapat mencegah atau menghindari deadlock secara efisien, terutama pada sistem dengan banyak proses dan resource dinamis. Dengan deteksi deadlock, sistem tetap fleksibel dan dapat menangani deadlock saat benar-benar terjadi.
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?
   **Jawaban:**  
   Kelebihan:
    - Lebih fleksibel dalam penggunaan resource
    - Tidak membatasi perilaku proses
    - Cocok untuk sistem dengan resource dinamis 

    Kekurangan:
    - Deadlock tetap bisa terjadi
    - Membutuhkan overhead untuk proses deteksi
    - Diperlukan mekanisme recovery (misalnya menghentikan proses)

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
 Belum sangat paham" betul materi ini
- Bagaimana cara Anda mengatasinya?  
  Jelasin Ulang Dongs Pakkk

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
