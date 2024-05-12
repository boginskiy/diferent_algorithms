# 


if __name__ == '__main__':

    # Список штатов
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

    # Список станций из которых будет выбираться покрытие
    stations = {}
    stations["k_one"] = set(["id", "nv", "ut"])
    stations["k_two"] = set(["wa", "id", "mt"])
    stations["k_three"] = set(["or", "nv", "ca"])
    stations["k_four"] = set(["nv", "ut"])
    stations["k_five"] = set(["ca", "az"])

    # Итоговый набор станций
    final_stations = set()

    while states_needed:  # ["mt", "wa", "or", "ca", "az"]
        # Лучшая по покрытию станция
        best_station = None
        # Покрытые штаты
        states_covered = set()

        for station, states_for_station in stations.items():
            #
            covered = states_needed & states_for_station  #  ["id", "nv", "ut"]

            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        
        # Добавляем конечную лучшую станцию
        final_stations.add(best_station)
        # Удаляем из общего списка штатов, те что покрываются текущей станцией
        states_needed -= states_covered
    
    print(final_stations)
