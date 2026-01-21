# code/app.py
import time
import sys
import os

def memory_stress_test(limit_mb=100):
    print(f"--- MEMORY STRESS TEST (Target: ~{limit_mb}MB) ---")
    dummy_data = []
    chunk_size_mb = 10
    
    try:
        for i in range(1, (limit_mb // chunk_size_mb) + 5):
            # Alokasi string sekitar 10MB
            print(f"Mengalokasikan {i * chunk_size_mb} MB memori...")
            dummy_data.append(' ' * (chunk_size_mb * 1024 * 1024))
            time.sleep(1) # Jeda agar terlihat di stats
        print("Memory test selesai tanpa crash.")
    except MemoryError:
        print("Error: Memory Limit Terlampaui (Python MemoryError)!")
    except Exception as e:
        print(f"Error tidak terduga: {e}")

def cpu_stress_test(n=50000):
    print(f"\n--- CPU STRESS TEST (Menghitung Faktorial {n}) ---")
    start_time = time.time()
    
    # Komputasi berat
    result = 1
    for i in range(1, n + 1):
        result = i * i 
    
    end_time = time.time()
    duration = end_time - start_time
    print(f"Selesai dalam waktu: {duration:.4f} detik")

if __name__ == "__main__":
    print(f"Process ID: {os.getpid()}")
    
    # 1. Jalankan tes CPU
    cpu_stress_test(30000000) # Angka besar agar butuh waktu
    
    # 2. Jalankan tes Memori
    # Kita coba alokasikan total 200MB secara bertahap
    memory_stress_test(limit_mb=200)