import csv

with open("csv/inmet_diario_original.csv", "r") as f:
    
    header = f.readline().strip()    
    
    lines = f.readlines()

    inmet_formatado = open("csv/inmet_diario_formatado.csv", "w")
    inmet_formatado.write(header + "\n")
    
    wr = csv.writer(inmet_formatado, quoting=csv.QUOTE_NONE)

    contador = 0
    while contador < len(lines):            
        linha1 = lines[contador].strip().split(',')
        linha2 = lines[contador+1].strip().split(',')

        if linha1[1] == linha2[1]:        
            linha_final = linha1[:3]
            linha_final.append(linha2[3])
            linha_final.append(linha1[4])
            linha_final.append(linha2[5])
            linha_final.extend(linha1[6:])
            contador += 2
        else:            
            linha_final = linha1
            contador += 1

        wr.writerow(linha_final)
        

    inmet_formatado.close() 
