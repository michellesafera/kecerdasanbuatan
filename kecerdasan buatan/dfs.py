setmap =  {'UDINUS':set(['TUGUMUDA','PONCOL']),
         'TUGUMUDA':set(['SIMPANGLIMA','KARYADI','UDINUS']),
         'KARYADI':set(['TUGUMUDA','UDINUS','SAMPOKONG','AKPOL','ELISABETH']),
         'PONCOL':set(['UDINUS','TUGUMUDA','TANAH MAS','PEMUDA'])}

def bfs(graf, awal, akhir):
    tempat = [[awal]]
    visited = set()

    while tempat:
        laju = len(tempat)-1
        jalur = tempat.pop(laju) 
        state = jalur[-1] 
        if state == akhir:
            print("Jalur yang di tempuh adalah: ")
            return jalur
            
        elif state not in visited:
            for cabang in graf.get(state, []): 
                jalur_baru = list(jalur) 
                jalur_baru.append(cabang) 
                tempat.append(jalur_baru) 
                print(tempat)
                

            visited.add(state)
            print("Visited : ",state)

        isi = len(tempat)
        if isi == 0:
            print("Tidak ditemukan")


awal = input("Masukkan titik awal: ")
akhir = input("Masukkan akhir tujuan: ")
print(bfs(setmap,awal,akhir))

