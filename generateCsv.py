import csv


def fileCsv(name,lasName,n1,n2,n3,total):
        with open('data_nuevo.csv','a+',newline='') as newcsv:
                    archivo_salida = csv.writer(newcsv,delimiter=',')
                    archivo_salida.writerow(['Nombre','Apellido','Nota Uno','Nota Dos','Nota Tres','definitiva'])
                    archivo_salida.writerow([name,lasName,n1,n2,n3,total]) 