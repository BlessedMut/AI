a_star_graph = {
    'San_Diego': [('Los_Angeles', 120), ('Las_Vegas', 330), ('Phoenix', 354)],
    'Los_Angeles': [('Las_Vegas', 270)],
    'Las_Vegas': [('Gas_Station', 230)],
    'Gas_Station': [('Salt_Lake_City', 199), ('Denver', 526)],
    'Phoenix': [('Albuquerque', 421)],
    'Albuquerque': [('Denver', 445)]
}



H = {
            'Los_Angeles': 831,
            'Las_Vegas': 605,
            'Phoenix': 586,
            'Gas_Station': 423,
            'Salt_Lake_City': 371,
            'Albuquerque': 349,
            'Denver': 0
        }
