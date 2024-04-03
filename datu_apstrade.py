import csv

dati = []

with open('izglitojamoskprofesionalasizglprogr_pa_progr_01012024.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ';', quotechar='"')

    for row in file_reader:
        dati.append(row)

dati.pop(0)

def sort_dati(dati_izglitujoso_skaits):
    return int(dati_izglitujoso_skaits[15])
def dati_novads_sort(dati_novads):
    return dati_novads[0]

while True:
    print("\nData Sort Menu:")
    print("1. Rādīt visus datus pēc skolnieka skaits uz augšu")
    print("2. Rādīt visus datus pēc skolnieka skaits uz leju")
    print("3. Rādīt visus datus sakartotas pēc novada no A-Z")
    print("4. Rādīt visus datus sakartotas pēc novada no Z-A")
    print("5. Meklēt sarakstā iestādes nosaukumu")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        dati_izglitujoso_skaits=dati.copy()
        dati_izglitujoso_skaits.sort(key=sort_dati)
        print(dati_izglitujoso_skaits)
        pass
    if choice == "2":
        dati_izglitujoso_skaits=dati.copy()
        dati_izglitujoso_skaits.sort(key=sort_dati, reverse=True)
        print(dati_izglitujoso_skaits)
        pass
    elif choice == "3":
        dati_novads=dati.copy()
        dati_novads.sort(key=dati_novads_sort)
        print(dati_novads)
        pass
    elif choice == "4":
        dati_novads=dati.copy()
        dati_novads.sort(key=dati_novads_sort, reverse=True)
        print(dati_novads)
    elif choice == "5":
        text=input("input text ")
        dati_search=[x for x in dati if x[2].startswith(text)]
        print(dati_search)
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
