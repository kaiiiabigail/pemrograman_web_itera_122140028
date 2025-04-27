def kalkulator_bmi():
    print("=== KALKULATOR BMI ===")
    print("----------------------")

    try:
        # Input berat badan dan tinggi badan
        berat_badan = float(input("Input berat badan (kg): "))
        tinggi_badan = float(input("Input tinggi badan (m): "))

        # Cek validitas input
        if berat_badan <= 0 or tinggi_badan <= 0:
            print("Error: Berat dan tinggi harus lebih dari nol!")
            return

        # Perhitungan BMI
        bmi = berat_badan / (tinggi_badan ** 2)

        # Menentukan kategori berdasarkan BMI
        if bmi < 18.5:
            kategori = "Berat badan kurang"
        elif bmi < 25:
            kategori = "Berat badan normal"
        elif bmi < 30:
            kategori = "Berat badan berlebih"
        else:
            kategori = "Obesitas"

        # Menampilkan hasil
        print("\n=== Hasil Perhitungan ===")
        print(f"Nilai BMI: {bmi:.2f}")
        print(f"Kategori: {kategori}")

    except ValueError:
        print("Error: Harap masukkan nilai angka yang valid!")

# Program Utama
if __name__ == "__main__":
    kalkulator_bmi()
