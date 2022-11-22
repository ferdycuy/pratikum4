file =[]
while True :
     nama   = input      ("nama : ")
     nim    = input      ("Nim  : ")
     tugas  = int(input  ("Tugas: "))
     uts    = int(input  ("Nilai UTS :"))
     uas    = int(input  ("Nilai UAS :"))
     nilaiakhir = float(tugas)*30/100+(uts)*35/100+(uas)*35/100
     file.append([nama,nim,tugas,uts,uas,nilaiakhir])
     data = input("Tambah data (y/t)?")
     if data.lower() =="t":
         break


print("====================================================================");
print("| No |   Nama   |   NIM   |  TUGAS  |  UTS  |  UAS  |  Nilai Akhir |");
print("====================================================================");
i=0
for x in file:
    i+=1
    print(" | {6:2d}| {0:9s} | {1:6s}  | {2:6d} | {3:4d}| {4:5d}| {5:13.2f}|"\
          .format(x[0][:9] , x[1][:6] , x[2] , x[3] , x[4] , x[5] ,i))