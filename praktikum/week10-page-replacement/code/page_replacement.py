# ==========================================
# Page Replacement Simulation: FIFO & LRU
# Dataset sudah ditentukan
# ==========================================

reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3


def fifo(reference, frames_count):
    frames = []
    page_fault = 0

    print("\n=== FIFO ===")
    print("Page | Frames | Status")
    print("-" * 30)

    for page in reference:
        if page in frames:
            status = "Hit"
        else:
            page_fault += 1
            status = "Fault"
            if len(frames) < frames_count:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)

        print(f"{page:>4} | {str(frames):<15} | {status}")

    print(f"\nTotal Page Fault FIFO: {page_fault}")
    return page_fault


def lru(reference, frames_count):
    frames = []
    recent = []
    page_fault = 0

    print("\n=== LRU ===")
    print("Page | Frames | Status")
    print("-" * 30)

    for page in reference:
        if page in frames:
            status = "Hit"
            recent.remove(page)
            recent.append(page)
        else:
            page_fault += 1
            status = "Fault"
            if len(frames) < frames_count:
                frames.append(page)
                recent.append(page)
            else:
                lru_page = recent.pop(0)
                frames.remove(lru_page)
                frames.append(page)
                recent.append(page)

        print(f"{page:>4} | {str(frames):<15} | {status}")

    print(f"\nTotal Page Fault LRU: {page_fault}")
    return page_fault


if __name__ == "__main__":
    fifo_fault = fifo(reference_string, frame_size)
    lru_fault = lru(reference_string, frame_size)

    print("\n=== PERBANDINGAN ===")
    print("Algoritma | Page Fault")
    print("----------------------")
    print(f"FIFO      | {fifo_fault}")
    print(f"LRU       | {lru_fault}")
