from datetime import date

# Germany
germany_start_date = date(2020, 2, 15)
germany_cases = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 18, 26, 48, 74, 79, 130, 165, 203, 262, 545, 670, 800, 1040,
                 1224, 1565, 1966, 2745, 3675, 4599, 5813, 7272, 9367, 12327, 15309]
germany = ["Germany", germany_start_date, germany_cases]

# SouthKorea
southkorea_start_date = date(2020, 2, 15)
southkorea_cases = [28, 29, 30, 31, 58, 111, 209, 436, 602, 833, 977, 1261, 1766, 2337, 3150, 3736, 4335, 5186, 5621,
                    6284, 6593, 7041, 7313, 7478, 7513, 7755, 7869, 7979, 8086, 8162, 8236, 8320, 8565]
southkorea = ["South Korea", southkorea_start_date, southkorea_cases]

# Italy
italy_start_date = date(2020, 2, 15)
italy_cases = [3, 3, 3, 3, 3, 4, 21, 79, 157, 229, 323, 470, 655, 889, 1128, 1701, 2036, 2502, 3089, 3858, 4636, 5883,
               7375, 9172, 10149, 12462, 15113, 17660, 21157, 24747, 27980, 31506, 35713, 41035]
italy = ["Italy", italy_start_date, italy_cases]

# USA
usaStartDate = date(2020, 2, 15)
usaCases = [15, 15, 15, 15, 15, 15, 35, 35, 35, 53, 57, 60, 60, 63, 68, 75, 100, 124, 158, 221, 319, 435, 541, 704, 994,
            1301, 1697, 2247, 2943, 3680, 4663, 6411, 9259, 11432]
usa = ["USA", usaStartDate, usaCases]

spain_start_date = date(2020, 2, 15)
spain_cases = [2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 9, 13, 25, 33, 58, 84, 120, 165, 228, 282, 401, 525, 674, 1231, 1695, 2277, 3146, 5232, 6391, 7988, 9942, 11826, 14769, 17963]
spain = ["Spain", spain_start_date, spain_cases]


class Country:
    USA = usa
    SOUTH_KOREA = southkorea
    GERMANY = germany
    ITALY = italy
    SPAIN = spain
