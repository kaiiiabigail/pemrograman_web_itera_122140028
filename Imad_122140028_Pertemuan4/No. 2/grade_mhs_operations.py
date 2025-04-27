def manajemen_nilai_mahasiswa():
    print("=== SISTEM MANAJEMEN NILAI MAHASISWA ===")
    print("----------------------------------------")
    
    # Daftar mahasiswa dengan data: nama, nim, nilai UTS, UAS, dan tugas
    daftar_mahasiswa = [
        {"nama": "Zefanya Danovanta", "nim": "122140101", "nilai_uts": 85, "nilai_uas": 90, "nilai_tugas": 88},
        {"nama": "Imad Aqil", "nim": "122140028", "nilai_uts": 88, "nilai_uas": 82, "nilai_tugas": 70},
        {"nama": "Ferdana Al-Hakim", "nim": "122140012", "nilai_uts": 65, "nilai_uas": 70, "nilai_tugas": 75},
        {"nama": "Tresnawan", "nim": "122140178", "nilai_uts": 75, "nilai_uas": 55, "nilai_tugas": 82},
        {"nama": "Yasir Ahmad", "nim": "122140142", "nilai_uts": 45, "nilai_uas": 55, "nilai_tugas": 60}
    ]
    
    # Proses menghitung nilai akhir dan menentukan grade
    for mahasiswa in daftar_mahasiswa:
        nilai_akhir = (0.3 * mahasiswa["nilai_uts"]) + (0.4 * mahasiswa["nilai_uas"]) + (0.3 * mahasiswa["nilai_tugas"])
        mahasiswa["nilai_akhir"] = nilai_akhir

        if nilai_akhir >= 80:
            mahasiswa["grade"] = "A"
        elif nilai_akhir >= 70:
            mahasiswa["grade"] = "B"
        elif nilai_akhir >= 60:
            mahasiswa["grade"] = "C"
        elif nilai_akhir >= 50:
            mahasiswa["grade"] = "D"
        else:
            mahasiswa["grade"] = "E"
    
    # Menampilkan data mahasiswa dalam bentuk tabel
    print("\nDATA NILAI MAHASISWA")
    print("-" * 85)
    print(f"{'NO':<3} | {'NIM':<10} | {'NAMA':<20} | {'UTS':^5} | {'UAS':^5} | {'TUGAS':^5} | {'AKHIR':^6} | {'GRADE':^5}")
    print("-" * 85)

    for idx, mahasiswa in enumerate(daftar_mahasiswa, start=1):
        print(f"{idx:<3} | {mahasiswa['nim']:<10} | {mahasiswa['nama']:<20} | "
              f"{mahasiswa['nilai_uts']:^5} | {mahasiswa['nilai_uas']:^5} | {mahasiswa['nilai_tugas']:^5} | "
              f"{mahasiswa['nilai_akhir']:^6.2f} | {mahasiswa['grade']:^5}")
    
    print("-" * 85)
    
    # Menentukan mahasiswa dengan nilai tertinggi dan terendah
    mahasiswa_terbaik = max(daftar_mahasiswa, key=lambda m: m["nilai_akhir"])
    mahasiswa_terburuk = min(daftar_mahasiswa, key=lambda m: m["nilai_akhir"])

    # Tampilkan hasil
    print("\nMAHASISWA NILAI TERTINGGI")
    print(f"Nama        : {mahasiswa_terbaik['nama']}")
    print(f"NIM         : {mahasiswa_terbaik['nim']}")
    print(f"Nilai Akhir : {mahasiswa_terbaik['nilai_akhir']:.2f}")
    print(f"Grade       : {mahasiswa_terbaik['grade']}")

    print("\nMAHASISWA NILAI TERENDAH")
    print(f"Nama        : {mahasiswa_terburuk['nama']}")
    print(f"NIM         : {mahasiswa_terburuk['nim']}")
    print(f"Nilai Akhir : {mahasiswa_terburuk['nilai_akhir']:.2f}")
    print(f"Grade       : {mahasiswa_terburuk['grade']}")

# Program utama
if __name__ == "__main__":
    manajemen_nilai_mahasiswa()
