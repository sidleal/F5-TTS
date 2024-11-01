print("teste")

import csv
import shutil

destination_path = "/home/sidleal/sources/F5-TTS/data/nurc_min"
source_path = "/home/sidleal/sources/nurc_minimo"

def process_file(filepath):
    seen_chars = set()
    fm = open(destination_path+ "/metadata.csv", 'w')
    fm.write("audio_file|text\n")
    try:
        with open(filepath, 'r', newline='') as csvfile: 
            reader = csv.reader(csvfile)

            next(reader, None) 

            for row in reader:
                fpath = row[0]
                ftext = row[5]
                if ftext.strip() == '':
                    continue
                print(fpath, ftext)
                wav_name = "wavs/" + fpath.split('/')[-1]
                shutil.copy2(source_path + fpath[16:], destination_path + "/" + wav_name)
                fm.write(wav_name + "|" + ftext + "\n")
                for char in ftext:
                    seen_chars.add(char)

        sorted_list = sorted(list(seen_chars))
        print(sorted_list) 
        with open(destination_path + "/vocab.txt", "w", encoding="utf-8") as f:
            for item in sorted_list:
                f.write(item + "\n")
    
        fm.close()
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
    except Exception as e:  
        print(f"An error occurred: {e}")

filepath = '/home/sidleal/sources/nurc_minimo/segmented_audios_time_no_intersection.csv'

process_file(filepath)
