# deadlock_detection.py
from datatest import processes, allocation, request, available
import time

def deadlock_detection(processes, allocation, request, available):
    n = len(processes)
    m = len(available)
    finish = [False] * n
    work = available[:]

    safe_seq = []

    print("=== Simulasi Eksekusi Deadlock Detection ===\n")
    while True:
        found = False
        for i in range(n):
            if not finish[i]:
                # cek apakah request[i] <= work
                if all(request[i][j] <= work[j] for j in range(m)):
                    print(f"{processes[i]}: request {request[i]} terpenuhi, proses berjalan...")
                    time.sleep(1)  # simulasi delay eksekusi
                    # proses selesai, release resource
                    for j in range(m):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_seq.append(processes[i])
                    print(f"{processes[i]}: selesai, resource dilepas -> available sekarang {work}\n")
                    found = True
        if not found:
            break

    deadlocked = [processes[i] for i in range(n) if not finish[i]]
    return safe_seq, deadlocked

# Jalankan deteksi
safe_seq, deadlocked = deadlock_detection(processes, allocation, request, available)

# Cetak hasil akhir dalam bentuk tabel
print("=== Hasil Akhir ===")
print("| Proses | Status Eksekusi | Keterangan |")
print("|--------|-----------------|------------|")
for p in processes:
    if p in safe_seq:
        print(f"| {p} | Selesai | Berhasil dieksekusi |")
    else:
        print(f"| {p} | Deadlock | Tidak dapat melanjutkan |")

print("\nSafe sequence:", safe_seq)
print("Deadlocked processes:", deadlocked)