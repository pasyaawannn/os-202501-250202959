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