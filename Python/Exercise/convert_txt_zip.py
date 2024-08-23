import os
import time
import pyzipper
import subprocess

def change_file_dates(file_path, target_date_str):
    date_format = "%d/%m/%y %H:%M"
    
    if os.path.exists(file_path):
        # Converti la data di destinazione in un timestamp
        target_timestamp = int(time.mktime(time.strptime(target_date_str, date_format)))

        # Data di creazione (1 ora prima della data di destinazione)
        creation_timestamp = target_timestamp - 3600

        # Cambia le date di accesso e modifica
        os.utime(file_path, (target_timestamp, target_timestamp))

        # Cambia la data di creazione (solo copiando il file)
        new_file_path = file_path + ".tmp"
        subprocess.run(['cp', file_path, new_file_path])
        os.utime(new_file_path, (creation_timestamp, creation_timestamp))

        # Sostituisci il file originale con il nuovo file per mantenere il nome
        os.replace(new_file_path, file_path)
    else:
        print("File non trovato")

def create_zip_with_dates(file_path, zip_path, target_date_str):
    change_file_dates(file_path, target_date_str)

    # Ottieni le date di modifica e accesso
    stat_info = os.stat(file_path)
    mod_time = time.localtime(stat_info.st_mtime)
    mod_time_zip = (mod_time.tm_year, mod_time.tm_mon, mod_time.tm_mday, 
                    mod_time.tm_hour, mod_time.tm_min, mod_time.tm_sec)

    # Crea l'archivio ZIP
    with pyzipper.AESZipFile(zip_path, 'w', compression=pyzipper.ZIP_DEFLATED) as zipf:
        # Aggiungi il file mantenendo le date
        zipf.write(file_path, arcname=os.path.basename(file_path))
        # Modifica la data di modifica del file all'interno dello ZIP
        zip_info = zipf.getinfo(os.path.basename(file_path))
        zip_info.date_time = mod_time_zip

# Esempio di utilizzo
file_path = "/home/Dokjolly/Desktop/Alex/Learn/Python/Exercise/WhatsApp Chat - +44 7951 553369.txt"
zip_path = "/home/Dokjolly/Desktop/Alex/Learn/Python/Exercise/WhatsApp_Chat.zip"
target_date_str = "09/04/24 11:48"

create_zip_with_dates(file_path, zip_path, target_date_str)
