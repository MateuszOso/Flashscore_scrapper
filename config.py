config = {
    "flashscore" : {
        "base_url": "https://www.flashscore.pl",
        "matches_endpoint": "/pilka-nozna/polska/pko-bp-ekstraklasa/wyniki/",
        "odds_endpoint": "/mecz/{match_id}/#/zestawienie-kursow/kursy-1x2/koniec-meczu",
        "players_endpoint": "/mecz/{match_id}/#/szczegoly-meczu/sklady",
        "dynamic_class_names": {
            "basic_round": "event__round",
            "rounds": "event__round--static",
            "matches": "event__match",
            "odds": "oddsCell__odd",
            "home_players": "event__participant--home",
            "away_players": "event__participant--away",
            "score_home": "event__score--home",
            "score_away": "event__score--away",
            "time": "event__time",
            "section_title": "section__title--center",
            "home_participants": ".lf__participant",
            "away_participants": ".lf__isReversed"},
        "titles": {
            "starting_lineup": "Składy wyjściowe"
        }
    }
}



