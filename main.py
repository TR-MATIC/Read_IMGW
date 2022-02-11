import requests

def check_temperatures(station_id_list: list) -> dict:
    imgw_url = "https://danepubliczne.imgw.pl/api/data/synop/id/"
    temperatures = {}
    for station in station_id_list:
        imgw_uri = imgw_url + station
        new_data = requests.get(imgw_uri, timeout=1.000).json()
        temperatures.update({"godzina": new_data["godzina_pomiaru"] + ":00",
                             new_data["stacja"]: new_data["temperatura"]})
    return temperatures


if __name__ == '__main__':
    temperatures = check_temperatures(["12195", "12155", "12120", "12135", "12625", "12650", "12510"])
    for key in temperatures:
        if key == "godzina":
            print("{} {}".format(key, temperatures[key]))
        else:
            if round(float(temperatures[key])) >= 0:
                bargraph = " " * 29 + "|" + "#" * round(float(temperatures[key]))
            else:
                bargraph = " " * (29 + round(float(temperatures[key]))) + "#" * abs(round(float(temperatures[key]))) + "|"
            print("{:16} {:>6}   {}".format(key, temperatures[key], bargraph))
    print("                         |         |         |         |         |         |         |\n"
          "                        -30       -20       -10        0         10        20        30")
