import random
import numpy as np

anggotaLiqo = ["Sami", "Fawwaz", "Azzam", "Faiz", "Rifki"]
tugasLiqo = ["MC", "Tilawah", "Doa", "Materi Duniawi/Islami"]

log = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
jumlahMinggu = 100
rekap =[]

print(log)

def main():
    countUlang = 0
    countUlang2 = 0
    count_minggu = 0
    hasil1 = random.choice(anggotaLiqo)
    log[anggotaLiqo.index(hasil1)][tugasLiqo.index(random.choice(tugasLiqo))] += 1
    
    try:
        for i in range(jumlahMinggu):
            for j in tugasLiqo:
                
                ketemu = False
                
                while ketemu == False:
                    
                    result = random.choice(anggotaLiqo)
                    
                    if(result in rekap):
                        if(len(rekap) == len(tugasLiqo)):
                            rekap.clear()
                        elif(len(rekap) > len(tugasLiqo)):
                            rekap.pop()
                        else:
                            # print("2")
                            countUlang += 1
                            if countUlang > 10000:
                                countUlang = 0
                                ketemu = True
                                rekap.append(result)
                                log[anggotaLiqo.index(result)][tugasLiqo.index(j)] += 1
                            else:
                                continue
                        # rekap.clear()
                    elif((count_minggu % 4) == 0): #Menghindari blocking saat semua sudah dapat nilai max
                            ketemu = True
                            rekap.append(result)
                            log[anggotaLiqo.index(result)][tugasLiqo.index(j)] += 1
                    else:
                        if np.amax(log) > log[anggotaLiqo.index(result)][tugasLiqo.index(j)]:
                            ketemu = True
                            rekap.append(result)
                            log[anggotaLiqo.index(result)][tugasLiqo.index(j)] += 1
                        else:
                            countUlang2 += 1
                            if countUlang2 > 10000:
                                countUlang2 = 0
                                ketemu = True
                                rekap.append(result)
                                log[anggotaLiqo.index(result)][tugasLiqo.index(j)] += 1
                            else:
                                continue

            print("Minggu ke " + str(i) + " :")

            print(tugasLiqo[0] +" : " + str(rekap[0]))
            print(tugasLiqo[1] +" : " + str(rekap[1]))
            print(tugasLiqo[2] +" : " + str(rekap[2]))
            print(tugasLiqo[3] +" : " + str(rekap[3]))
            count_minggu += 1

    except:
        print()
        print("Stop disini")
        print("Minggu ke" + str(i))
        print(rekap)
        print(log)
    
    # print(log)
    
if __name__ == "__main__":
    main()