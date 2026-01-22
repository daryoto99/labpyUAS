class Mahasiswa:
    def __init__(self, nama, uts, uas):
        self.nama = nama
        self.uts = uts
        self.uas = uas
        self.nilai_akhir = 0
        self.status = ""
class NilaiProcess:
    def hitung_nilai_akhir(self, mahasiswa):
        mahasiswa.nilai_akhir = (mahasiswa.uts * 0.4) + (mahasiswa.uas * 0.6)
        return mahasiswa.nilai_akhir

    def tentukan_status(self, mahasiswa):
        if mahasiswa.nilai_akhir >= 60:
            mahasiswa.status = "Lulus"
        else:
            mahasiswa.status = "Tidak Lulus"
        return mahasiswa.status
class NilaiView:
    def tampilkan_tabel(self, mahasiswa):
        print("\nHASIL NILAI AKHIR MAHASISWA")
        print("+----------------+-----+-----+-------------+-------------+")
        print("| Nama           | UTS | UAS | Nilai Akhir | Status      |")
        print("+----------------+-----+-----+-------------+-------------+")
        print(f"| {mahasiswa.nama:<14} | {mahasiswa.uts:<3} | {mahasiswa.uas:<3} | {mahasiswa.nilai_akhir:<11.2f} | {mahasiswa.status:<11} |")
        print("+----------------+-----+-----+-------------+-------------+")
def main():
    try:
        nama = input("Masukkan nama mahasiswa: ")
        if nama.strip() == "":
            raise ValueError("Nama tidak boleh kosong")

        uts = int(input("Masukkan nilai UTS (0-100): "))
        uas = int(input("Masukkan nilai UAS (0-100): "))

        if uts < 0 or uts > 100 or uas < 0 or uas > 100:
            raise ValueError("Nilai harus antara 0 sampai 100")

        mahasiswa = Mahasiswa(nama, uts, uas)

        proses = NilaiProcess()
        proses.hitung_nilai_akhir(mahasiswa)
        proses.tentukan_status(mahasiswa)

        view = NilaiView()
        view.tampilkan_tabel(mahasiswa)

    except ValueError as e:
        print("Error:", e)


main()
