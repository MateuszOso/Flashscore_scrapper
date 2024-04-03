from csv_saver import CsvSaver
'''
TODO, clean-code
 Porozdzielac odpowiedzialnosc 
    - osobny serwis do pobierania i formatowania do encji  (do niego podajesz config, tam uruchamiasz selenium i scrappera)
    - osobny serwis do zapisywania do CSV
    - * wynajdź najkorzystniejszą różnicę w scoringu
    -- ** podkreśl najkorzystniejszy scoring w excelu na czerwono
'''
def main():

    csv_test = CsvSaver()
    csv_test.saver()

if __name__ == "__main__":
    main()
