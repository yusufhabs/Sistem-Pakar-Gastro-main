def val(b):
    return 1.0 if b else 0.0

def proses_diagnosis(u):
    """
    Menghitung kemungkinan penyakit berdasarkan input gejala (u)
    u: list of boolean (True/False) sepanjang 19 elemen
    """

    # Menghitung Node Menengah (Intermediate Conditions)
    n20 = (val(u[0]) + val(u[1]) + val(u[3]) + val(u[4])) / 4.0
    n21 = (val(u[3]) + val(u[4]) + val(u[5])) / 3.0
    n22 = (val(u[3]) + val(u[6])) / 2.0
    n23 = (val(u[3]) + val(u[7]) + val(u[8])) / 3.0
    n24 = (val(u[7]) + val(u[9])) / 2.0
    n25 = (val(u[3]) + val(u[4]) + val(u[10])) / 3.0
    n26 = (val(u[3]) + val(u[7]) + val(u[10]) + val(u[11])) / 4.0
    n27 = (val(u[3]) + val(u[12])) / 2.0
    n28 = (val(u[0]) + val(u[1]) + val(u[2]) + val(u[3]) + val(u[4])) / 5.0
    n29 = (val(u[13]) + val(u[14])) / 2.0
    n30 = (val(u[13]) + val(u[15])) / 2.0
    n31 = (val(u[13]) + val(u[16])) / 2.0
    n32 = (val(u[17]) + val(u[18])) / 2.0

    # Menghitung Final Penyakit (Persentase)
    hasil = {
        "Staphylococcus aureus": ((n20 + n21 + n22 + n23 + n29) / 5.0) * 100,
        "Jamur beracun": ((n20 + n21 + n22 + n24 + n30) / 5.0) * 100,
        "Salmonellae": ((n20 + n21 + n22 + n25 + n26 + n29) / 6.0) * 100,
        "Clostridium botulinum": ((n21 + n27 + n31) / 3.0) * 100,
        "Campylobacter": ((n28 + n22 + n25 + n32) / 4.0) * 100
    }
    return hasil

def main():
    print("=== SISTEM PAKAR INFEKSI GASTRO USUS ===")
    print("Jawablah pertanyaan berikut dengan (y/n):\n")

    daftar_pertanyaan = [
        "Apakah anda sering mengalami buang air besar (>2x)?",
        "Apakah anda mengalami berak encer?",
        "Apakah anda mengalami berak berdarah?",
        "Apakah anda merasa lesu dan tidak bergairah?",
        "Apakah anda tidak selera makan?",
        "Apakah anda merasa mual dan sering muntah (>1x)?",
        "Apakah anda merasa sakit di bagian perut?",
        "Apakah tekanan darah anda rendah?",
        "Apakah anda merasa pusing?",
        "Apakah anda mengalami pingsan?",
        "Apakah suhu badan anda tinggi?",
        "Apakah anda mengalami luka di bagian tertentu?",
        "Apakah anda tidak dapat menggerakkan anggota badan tertentu?",
        "Apakah anda pernah memakan sesuatu?",
        "Apakah anda memakan daging?",
        "Apakah anda memakan jamur?",
        "Apakah anda memakan makanan kaleng?",
        "Apakah anda membeli susu?",
        "Apakah anda meminum susu?"
    ]

    # Mengumpulkan input user
    input_user = []
    for q in daftar_pertanyaan:
        jawab = input(f"{q} (y/n): ").lower()
        input_user.append(True if jawab == 'y' else False)

    # Proses perhitungan
    hasil_diagnosis = proses_diagnosis(input_user)

    # Input Threshold
    try:
        threshold = float(input("\nMasukkan nilai Threshold (%) [Default 80]: ") or 80)
    except ValueError:
        threshold = 80.0

    # Menampilkan Hasil
    print("\n" + "="*30)
    print("HASIL ANALISIS PERHITUNGAN:")
    print("="*30)
    
    kesimpulan = "Gejala di bawah Threshold"
    max_persen = 0

    for penyakit, persen in hasil_diagnosis.items():
        print(f"{penyakit:25} : {persen:.2f}%")
        if persen >= threshold and persen > max_persen:
            max_persen = persen
            kesimpulan = penyakit

    print("-" * 30)
    print(f"KESIMPULAN: Anda kemungkinan terkena {kesimpulan}")
    print("="*30)

if __name__ == "__main__":
    main()