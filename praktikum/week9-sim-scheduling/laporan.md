
# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan CPU

---

## Identitas
- **Nama**  : Pasya Awan Rizky Saputro
- **NIM**   : 250202959
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.
4. Menjelaskan hasil simulasi secara tertulis.
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan **mengimplementasikan program simulasi sederhana algoritma penjadwalan CPU,** khususnya **FCFS dan SJF**.
Berbeda dengan Minggu 5–6 yang berfokus pada perhitungan manual, pada minggu ini mahasiswa mulai **mengotomatisasi perhitungan menggunakan program**, menjalankan dataset uji, serta menyajikan hasil dalam bentuk tabel atau grafik.

Praktikum ini menjadi jembatan antara **pemahaman konseptual** dan **implementasi komputasional** algoritma sistem operasi.

---

## Ketentuan Teknis
- Bahasa pemrograman **bebas** (Python / C / Java / lainnya).
- Tidak wajib GUI, cukup **program berbasis terminal**.
- Fokus penilaian pada **logika algoritma dan keakuratan hasil**, bukan kompleksitas bahasa.

Struktur folder (sesuaikan dengan template repo):
```bash
praktikum/week9-sim-scheduling/
├─ code/
│  ├─ scheduling_simulation.*
│  └─ dataset.csv
├─ screenshots/
│  └─ hasil_simulasi.png
└─ laporan.md
```

---

## Langkah Praktikum
1. **Menyiapkan Dataset**  
     Buat dataset proses minimal berisi:

     | Proses | Arrival Time (AT) | Burst Time (BT) |
     | ------ | ----------------- | --------------- |
     | P1     | 0                 | 6               |
     | P2     | 1                 | 8               |
     | P3     | 2                 | 7               |
     | P4     | 3                 | 3               |

2. **Implementasi Algoritma**   
Program harus:  
   - Menghitung _waiting time_ dan _turnaround time_.
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**  
   - Jalankan program menggunakan dataset uji.
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**  
   - Jelaskan alur program.
   - Bandingkan hasil simulasi dengan perhitungan manual.
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
import csv
import os

# Konfigurasi nama file dataset
FILENAME = 'dataset.csv'

def calculate_fcfs(processes):
    """
    Menghitung scheduling menggunakan algoritma FCFS.
    """
    # 1. Urutkan berdasarkan Arrival Time
    processes.sort(key=lambda x: x['arrival_time'])

    current_time = 0
    
    for p in processes:
        # Cek jika CPU idle (waktu sekarang < waktu kedatangan proses)
        if current_time < p['arrival_time']:
            current_time = p['arrival_time']

        # Hitung waktu
        start_time = current_time
        completion_time = start_time + p['burst_time']
        turnaround_time = completion_time - p['arrival_time']
        waiting_time = turnaround_time - p['burst_time']

        # Simpan hasil ke dictionary proses
        p['completion_time'] = completion_time
        p['turnaround_time'] = turnaround_time
        p['waiting_time'] = waiting_time

        # Update waktu sekarang
        current_time = completion_time
    
    return processes

def print_table(data):
    """
    Mencetak tabel hasil simulasi ke terminal.
    """
    print("\n" + "="*85)
    print(f"{'Proses':<10} | {'Arrival':<10} | {'Burst':<10} | {'Completion':<12} | {'Turnaround':<12} | {'Waiting':<10}")
    print("-" * 85)

    total_tat = 0
    total_wt = 0

    for p in data:
        print(f"{p['id']:<10} | {p['arrival_time']:<10} | {p['burst_time']:<10} | "
              f"{p['completion_time']:<12} | {p['turnaround_time']:<12} | {p['waiting_time']:<10}")
        total_tat += p['turnaround_time']
        total_wt += p['waiting_time']

    # Hitung Rata-rata
    avg_tat = total_tat / len(data)
    avg_wt = total_wt / len(data)

    print("-" * 85)
    print(f"Rata-rata Turnaround Time : {avg_tat:.2f} ms")
    print(f"Rata-rata Waiting Time    : {avg_wt:.2f} ms")
    print("="*85 + "\n")

def main():
    print("--- Simulasi CPU Scheduling (FCFS) ---")
    
    # Cek apakah file ada di direktori yang sama
    if not os.path.exists(FILENAME):
        print(f"\n[ERROR] File '{FILENAME}' tidak ditemukan!")
        print("Silakan buat file dataset.csv terlebih dahulu sesuai format.")
        return

    try:
        # Membaca file CSV
        raw_data = []
        with open(FILENAME, mode='r') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                raw_data.append({
                    'id': row['Proses'],
                    'arrival_time': int(row['Arrival Time']),
                    'burst_time': int(row['Burst Time'])
                })

        # Jalankan Algoritma
        if not raw_data:
            print("[INFO] Dataset kosong.")
        else:
            result_data = calculate_fcfs(raw_data)
            print_table(result_data)

    except KeyError as e:
        print(f"\n[ERROR] Format Header CSV salah. Kolom {e} tidak ditemukan.")
        print("Pastikan header: Proses, Arrival Time, Burst Time")
    except ValueError:
        print("\n[ERROR] Data dalam CSV harus berupa angka untuk Arrival dan Burst Time.")

if __name__ == "__main__":
    main()
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/output.png)

---

## Analisis
1. **Jelaskan Alur Program.**  
 Program dimulai dengan membaca data proses dari file ``dataset.csv``. Setiap baris data disimpan dalam struktur list berisi informasi ID proses, arrival time, dan burst time. Data proses kemudian diurutkan berdasarkan arrival time untuk menerapkan prinsip First Come First Served (FCFS). Selanjutnya, program mensimulasikan waktu kerja CPU secara berurutan dengan menghitung completion time, turnaround time, dan waiting time untuk setiap proses tanpa adanya interupsi antar proses. Setelah seluruh proses selesai dieksekusi, hasil simulasi ditampilkan dalam bentuk tabel beserta nilai rata-rata turnaround time dan waiting time.  
2. **Bandingkan hasil simulasi dengan perhitungan manual.**  
Berdasarkan perhitungan manual algoritma FCFS, proses P1 dijalankan lebih dahulu karena memiliki arrival time paling kecil, diikuti oleh P2, P3, dan P4. Nilai completion time, turnaround time, dan waiting time yang dihasilkan program sama dengan hasil perhitungan manual. Rata-rata waiting time yang diperoleh adalah 8,75 ms dan rata-rata turnaround time sebesar 14,75 ms. Hal ini menunjukkan bahwa simulasi yang dibuat telah mengimplementasikan algoritma FCFS dengan benar.  
3. **Kelebihan dan Keterbatasan Simulasi**
   - **Kelebihan**:  
Simulasi ini mudah dipahami karena menggunakan algoritma yang sederhana. Program mampu menghitung parameter penjadwalan secara otomatis dan memberikan hasil yang konsisten dengan perhitungan manual, sehingga cocok digunakan sebagai media pembelajaran konsep dasar penjadwalan CPU.

    - **Keterbatasan**:  
Simulasi hanya menerapkan satu algoritma penjadwalan, yaitu FCFS, sehingga belum dapat digunakan untuk membandingkan dengan algoritma lain. Selain itu, program belum menyediakan visualisasi proses seperti diagram Gantt dan tidak mempertimbangkan faktor lain seperti prioritas atau preemption.  

---

## Kesimpulan
- **Implementasi algoritma FCFS berhasil dilakukan**.  
Program mampu membaca dataset, mengurutkan proses berdasarkan arrival time, dan mengeksekusi proses secara berurutan tanpa interupsi sesuai konsep FCFS.

- **Hasil simulasi valid dan akurat**.  
Nilai waiting time dan turnaround time yang dihasilkan program sama dengan hasil perhitungan manual, sehingga logika dan perhitungan dalam program dapat dinyatakan benar.

- **Simulasi efektif untuk pengujian algoritma scheduling**.  
Simulasi mempermudah pengujian dan analisis algoritma penjadwalan, terutama untuk dataset besar, meskipun algoritma FCFS memiliki keterbatasan dalam efisiensi waktu tunggu.

---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?  
   **Jawaban:**  
   Simulasi diperlukan untuk mempermudah pengujian algoritma scheduling karena memungkinkan perhitungan waiting time dan turnaround time dilakukan secara otomatis dan konsisten. Dengan simulasi, algoritma dapat diuji menggunakan berbagai dataset tanpa harus melakukan perhitungan manual yang memakan waktu dan berpotensi menimbulkan kesalahan, sehingga hasil yang diperoleh lebih akurat dan efisien. 
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?  
   **Jawaban:**  
   Pada dataset kecil, hasil simulasi dan perhitungan manual umumnya sama. Namun, pada dataset yang besar, perhitungan manual menjadi tidak praktis dan rawan kesalahan, sedangkan simulasi tetap dapat menghasilkan hasil yang cepat dan akurat. Perbedaannya terletak pada efisiensi dan ketelitian, bukan pada nilai hasil perhitungannya. 
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.  
   **Jawaban:**  
   Algoritma First Come First Served (FCFS) lebih mudah diimplementasikan dibandingkan algoritma lain karena hanya membutuhkan pengurutan proses berdasarkan arrival time dan eksekusi secara berurutan tanpa interupsi. Logika yang sederhana ini membuat FCFS mudah dipahami dan cocok digunakan sebagai algoritma dasar dalam pembelajaran penjadwalan CPU.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
  - Dari kemarin ga di up" keteter dong pak 
- Bagaimana cara Anda mengatasinya?  
   - Sistem kebut

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
