def bandingkan_file(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            baris1 = f1.read().splitlines()
            baris2 = f2.read().splitlines()

            max_baris = max(len(baris1), len(baris2))

            print("Perbedaan antar kedua file:\n")
            ada_perbedaan = False
            for i in range(max_baris):
                teks1 = baris1[i] if i < len(baris1) else ""
                teks2 = baris2[i] if i < len(baris2) else ""

                tampil1 = teks1 if teks1.strip() != "" else "(baris tidak ada)"
                tampil2 = teks2 if teks2.strip() != "" else "(baris tidak ada)"

                print(f"Baris {i+1}:")
                print(f"  File 1: {tampil1}")
                print(f"  File 2: {tampil2}\n")

    except FileNotFoundError as e:
        print(f"File tidak ditemukan: {e.filename}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

file1 = 'file1.txt'
file2 = 'file2.txt'
bandingkan_file(file1, file2)
