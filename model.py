input_lvs = [
    {
        'X': (0, 40, 1), # Celsius
        'name': 'Temperature', 
        'terms': {
            'low': ('trapmf', 0, 0, 10, 21),
            'comfortable': ('trapmf', 20, 22, 25, 27),
            'high': ('trapmf', 26, 28, 30, 40),
        }
    },
    {
        'X': (0, 100, 1), # in %
        'name': 'Humidity', 
        'terms': {
            'low': ('trapmf', 0, 0, 20, 40),
            'medium': ('trapmf', 39, 45, 60, 75),
            'high': ('trapmf', 70, 80, 90, 100),
        }
    },
    {
        'X': (0, 900, 1), # lx
        'name': 'Lighting',  
        'terms': {
            'dark': ('trapmf', 0, 0, 100, 301),
            'comfortable': ('trapmf', 300, 400, 500, 601),
            'too bright': ('trapmf', 600, 700, 800, 900),
        }
    }
]

output_lv = {
    'X': (0, 1, 0.1),
    'name': 'Comfort level',
    'terms': {
        'low': ('trapmf', 0, 0, 0.2, 0.35),
        'medium': ('trapmf', 0.3, 0.4, 0.5, 0.65),
        'high': ('trapmf', 0.6, 0.7, 0.8, 1),
    }
}

rule_base = [
    (('low', 'low', 'dark'), 'low'),
    (('low', 'low', 'comfortable'), 'low'),
    (('low', 'low', 'too bright'), 'low'),
    (('low', 'medium', 'dark'), 'low'),
    (('low', 'medium', 'comfortable'), 'medium'),
    (('low', 'medium', 'too bright'), 'low'),
    (('low', 'high', 'dark'), 'low'),
    (('low', 'high', 'comfortable'), 'medium'),
    (('low', 'high', 'too bright'), 'low'),

    (('comfortable', 'low', 'dark'), 'medium'),
    (('comfortable', 'low', 'comfortable'), 'high'),
    (('comfortable', 'low', 'too bright'), 'medium'),
    (('comfortable', 'medium', 'dark'), 'high'),
    (('comfortable', 'medium', 'comfortable'), 'high'),
    (('comfortable', 'medium', 'too bright'), 'high'),
    (('comfortable', 'high', 'dark'), 'medium'),
    (('comfortable', 'high', 'comfortable'), 'high'),
    (('comfortable', 'high', 'too bright'), 'high'),

    (('high', 'low', 'dark'), 'low'),
    (('high', 'low', 'comfortable'), 'low'),
    (('high', 'low', 'too bright'), 'low'),
    (('high', 'medium', 'dark'), 'low'),
    (('high', 'medium', 'comfortable'), 'medium'),
    (('high', 'medium', 'too bright'), 'medium'),
    (('high', 'high', 'dark'), 'low'),
    (('high', 'high', 'comfortable'), 'medium'),
    (('high', 'high', 'too bright'), 'medium'),
]