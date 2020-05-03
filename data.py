import json

title = "Eldar Travel"
subtitle = "Для тех, кого отвлекают дома"
description = "Лучшие направления, где никто не будет вам мешать сидеть на берегу и изучать программирование, дизайн, разработку игр и управление продуктами"
departures = {"msk": "Из Москвы", "spb": "Из Петербурга", "nsk": "Из Новосибирска", "ekb": "Из Екатеринбурга",
              "kazan": "Из Казани"}

with open('data.json') as json_file:
    tours = [dict(v, **{'id': int(k)}) for k, v in json.load(json_file).items()]