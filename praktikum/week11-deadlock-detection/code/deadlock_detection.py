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