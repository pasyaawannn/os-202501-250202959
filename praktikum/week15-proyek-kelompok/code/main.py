import sys
import os
from modules import cpu, memory, deadlock

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("==========================================")
        print("     OS SIMULATION TOOL - KELOMPOK        ")
        print("==========================================")
        print("1. CPU Scheduling (FCFS)")
        print("2. Memory Management (LRU)")
        print("3. Deadlock Detection (Banker's Algo)")
        print("4. Keluar")
        print("==========================================")
        
        choice = input("Pilih menu [1-4]: ")
        
        if choice == '1':
            cpu.solve_fcfs('data/cpu_data.csv')
        elif choice == '2':
            try:
                frames = int(input("Masukkan jumlah Frame RAM (misal: 3): "))
                memory.solve_lru('data/mem_data.txt', capacity=frames)
            except ValueError:
                print("Input harus angka!")
        elif choice == '3':
            deadlock.check_deadlock('data/deadlock_data.json')
        elif choice == '4':
            print("Terima kasih!")
            sys.exit()
        else:
            print("Pilihan tidak valid.")
        
        input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main_menu()