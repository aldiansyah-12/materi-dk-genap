#program uutuk menghitung  nilai akhir

nilai_tugas=int(input("masukan nilai tugas: "))
nilai_uts=int(input("masukan nilai uts: "))
nilai_uas=int(input("masukan nilai uas: "))

nilai_akhir=30/100 * nilai_uts+50/100*nilai_uas+20/100*nilai_tugas

print("Nilai Akhir:",nilai_akhir)