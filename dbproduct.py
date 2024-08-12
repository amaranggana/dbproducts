import os
if __name__ == "__main__":
    sistem_operasi = os.name
    while(True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PRODUCT")
        print("=========================")

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data")

        user_option = input("Masukkan opsi 1-4: ")
        if user_option not in ["1", "2", "3", "4"]:
            print("\nInput tidak valid!\nHarap masukkan opsi antara 1 hingga 4.\n")

        print("\n=========================\n")

        match user_option:
            case "1": print("Read Data")
            case "2": print("Create Data")
            case "3": print("Update Data")
            case "4": print("Delete Data")
        print("\n=========================\n")
        is_done = input("Apakah selesai (y/n)?:")
        if is_done == "y" or is_done == "Y":
            break
        print("Program berakhir. Terima kasih")