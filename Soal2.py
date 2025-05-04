def main():
    nama_file = 'soal.txt'
    print(f"nama file1: {nama_file}")

    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            for baris in file:
                if '||' in baris:
                    soal, jawaban_benar = baris.strip().split('||')
                    soal = soal.strip()
                    jawaban_benar = jawaban_benar.strip()

                    print(soal)
                    jawaban_user = input("Jawab: ").strip()

                    if jawaban_user.lower() == jawaban_benar.lower():
                        print("Jawaban benar!")
                    else:
                        print("Jawaban salah!")

    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")

if __name__ == "__main__":
    main()
