from tabulate import tabulate

def solve_lru(file_path, capacity=3):
    print(f"\n[INFO] Menjalankan Memory Management (LRU) - Frame: {capacity}")
    
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            # Handle pemisah spasi atau koma
            pages = content.replace(',', ' ').split()
    except FileNotFoundError:
        print("Error: File dataset tidak ditemukan.")
        return

    frames = []
    page_faults = 0
    history = []

    for page in pages:
        status = ""
        
        if page not in frames:
            # MISS (Page Fault)
            status = "MISS"
            page_faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                # LRU Logic: Hapus elemen pertama (paling lama tidak dipakai)
                frames.pop(0)
                frames.append(page)
        else:
            # HIT
            status = "HIT"
            # Update posisi page ke paling belakang (recently used)
            frames.remove(page)
            frames.append(page)
        
        # Simpan state saat ini untuk tabel
        history.append([page, str(frames), status])

    # Hitung Rasio
    total_requests = len(pages)
    hit_ratio = ((total_requests - page_faults) / total_requests) * 100
    
    print(tabulate(history, headers=["Page Request", "Frame Content", "Status"], tablefmt="simple"))
    
    print(f"\n> Total Requests : {total_requests}")
    print(f"> Total Page Faults: {page_faults}")
    print(f"> Hit Ratio        : {hit_ratio:.2f}%")