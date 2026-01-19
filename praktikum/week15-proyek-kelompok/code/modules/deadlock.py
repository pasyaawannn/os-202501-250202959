import json
from tabulate import tabulate

def check_deadlock(file_path):
    print(f"\n[INFO] Menjalankan Deadlock Detection (Banker's Algorithm)")
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error membaca file JSON: {e}")
        return

    # Ambil data matriks
    processes = data['processes']
    avail = data['available']
    alloc = data['allocation']
    max_res = data['max']
    
    num_proc = len(processes)
    num_res = len(avail)
    
    # Hitung Need Matrix (Need = Max - Allocation)
    need = [[max_res[i][j] - alloc[i][j] for j in range(num_res)] for i in range(num_proc)]
    
    # Tampilkan Tabel Need
    print("\n--- Need Matrix ---")
    need_display = [[processes[i]] + need[i] for i in range(num_proc)]
    print(tabulate(need_display, headers=["Proc"] + [f"R{j}" for j in range(num_res)], tablefmt="grid"))

    # Algoritma Safety
    finish = [False] * num_proc
    safe_seq = []
    work = avail[:] # Copy available
    
    while len(safe_seq) < num_proc:
        found = False
        for i in range(num_proc):
            if not finish[i]:
                # Cek apakah Need <= Work
                if all(need[i][j] <= work[j] for j in range(num_res)):
                    # Alokasikan, lalu return resource
                    for j in range(num_res):
                        work[j] += alloc[i][j]
                    
                    finish[i] = True
                    safe_seq.append(processes[i])
                    found = True
        
        if not found:
            break
            
    if len(safe_seq) == num_proc:
        print(f"\n[RESULT] SISTEM AMAN (Safe State).")
        print(f"> Safe Sequence: {' -> '.join(safe_seq)}")
    else:
        print(f"\n[RESULT] DEADLOCK TERDETEKSI!")
        print(f"> Proses yang menyebabkan deadlock/tidak bisa jalan: {[processes[i] for i in range(num_proc) if not finish[i]]}")