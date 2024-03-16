from csv_saver import CsvSaver

def main():
    '''
    Ogólnie dobra robota, jest progres, który widać gołym okiem!
    W nastepnym branchu nanieś poprawki zgodnie z komentarzami w plikach
    Niestety nie mogę na ten moment tego odpalić, pponieważ nie mam zainstalowanego odpowiedniego sterownika bo mam nowego Maca i sie go jeszcze uczę|
    Jak dodasz obiekt konfiguracyjny to dodaj jeszcze jeden/dwa serwisy bukmacherskie, będzie to dobry wstę do abstrakcji :)
    '''
    csv_test = CsvSaver()
    csv_test.saver()

if __name__ == "__main__":
    main()
