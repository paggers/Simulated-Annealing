original = ("20","35","50")
for i in range(10):
    for j in range(3):
        try:
            f = open("outputs/input" + original[j] + "_" + str(i) + ".out")
            f2 = open("outputs/output" + original[j] + "_" + str(i) + ".out", "w")
            f.readline()
            f2.write(f.readline())
            f.close()
            f2.close()
        except:
            pass
            
for i in range(18):
    try:
        f = open("outputs/input" + str(60 + i * 20) + "_0.out")
        f2 = open("outputs/staff_" + str(60 + i * 20) + ".out", "w")
        f.readline()
        f2.write(f.readline())
        f.close()
        f2.close()
    except:
        pass