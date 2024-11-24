input_lvs = [
    {
        'X': (0, 10, 1), # km
        'name': 'Proximity to Center',  # Близькість до центру
        'terms': {
            'very close': ('trapmf', 0, 0, 1, 3),
            'moderately distant': ('trapmf', 2, 3, 4, 5),
            'far': ('trapmf', 4, 6, 7, 10),
        }
    },
    {
        'X': (0, 200, 1), # m^2
        'name': 'Area',  # Площа
        'terms': {
            'low': ('trapmf', 0, 0, 5, 35),
            'medium': ('trapmf', 30, 40, 55, 65),
            'high': ('trapmf', 60, 80, 150, 200),
        }
    },
    {
        'X': (1950, 2024, 1), # Build year
        'name': 'Modernity',  # Сучасність
        'terms': {
            'old': ('trapmf', 1950, 1950, 1980, 2005),
            'moderately outdated': ('trapmf', 2003, 2010, 2012, 2016),
            'new': ('trapmf', 2015, 2019, 2022, 2024),
        }
    }
]

output_lv = {
    'X': (10000, 1000000, 5000), # Price in USD
    'name': 'Cost',
    'terms': {
        'low': ('trapmf', 10000, 10000, 15000, 30000),
        'medium': ('trapmf', 20000, 40000, 60000, 90000),
        'high': ('trapmf', 80000, 120000, 200000, 500000),
        'extremely high': ('trapmf', 400000, 650000, 800000, 1000000),
    }
}

rule_base = [
    (('very close', 'high', 'new'), 'extremely high'),
    (('very close', 'medium', 'new'), 'high'),
    (('very close', 'low', 'new'), 'medium'),
    (('very close', 'high', 'moderately outdated'), 'extremely high'),
    (('very close', 'medium', 'moderately outdated'), 'high'),
    (('very close', 'low', 'moderately outdated'), 'medium'),
    (('very close', 'high', 'old'), 'high'),
    (('very close', 'medium', 'old'), 'medium'),
    (('very close', 'low', 'old'), 'low'),

    (('moderately distant', 'high', 'new'), 'extremely high'),
    (('moderately distant', 'medium', 'new'), 'high'),
    (('moderately distant', 'low', 'new'), 'medium'),
    (('moderately distant', 'high', 'moderately outdated'), 'high'),
    (('moderately distant', 'medium', 'moderately outdated'), 'medium'),
    (('moderately distant', 'low', 'moderately outdated'), 'low'),
    (('moderately distant', 'high', 'old'), 'medium'),
    (('moderately distant', 'medium', 'old'), 'medium'),
    (('moderately distant', 'low', 'old'), 'low'),

    (('far', 'high', 'new'), 'high'),
    (('far', 'medium', 'new'), 'medium'),
    (('far', 'low', 'new'), 'medium'),
    (('far', 'high', 'moderately outdated'), 'medium'),
    (('far', 'medium', 'moderately outdated'), 'medium'),
    (('far', 'low', 'moderately outdated'), 'low'),
    (('far', 'high', 'old'), 'medium'),
    (('far', 'medium', 'old'), 'low'),
    (('far', 'low', 'old'), 'low'),
]