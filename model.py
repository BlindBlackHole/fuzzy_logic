input_lvs = [
    {
        'X': (0, 1, 0.01),
        'name': 'Distance',
        'terms': {
            'z1': ('trapmf', 0, 0, 0.15, 0.25),
            'z2': ('trapmf', 0.2, 0.3, 0.5, 0.7),
            'z3': ('trapmf', 0.4, 0.55, 1, 1),
        }
    },

    {
        'X': (0, 1, 0.1),
        'name': 'State',
        'terms': {
            'without_repair': ('trapmf', 0, 0, 0.2, 0.4),
            'satisfied': ('trapmf', 0.35, 0.45, 0.55, 0.65),
            'with_repair': ('trapmf', 0.5, 0.7, 1, 1),
        }
    },

    {
        'X': (0, 1, 0.01),
        'name': 'S',
        'terms': {
            'small': ('trapmf', 0, 0, 0.3, 0.45),
            'average': ('trapmf', 0.3, 0.5, 0.6, 0.75),
            'extra': ('trapmf', 0.6, 0.75, 1, 1),
        }
    },
]

output_lv = {
    'X': (0, 1, 0.01),
    'name': 'Class',
    'terms': {
        'none to very little': ('trapmf', 0, 0, 0.05, 0.1),
        'very low': ('trimf', 0, 0.2, 0.3),
        'low': ('trapmf', 0.2, 0.3, 0.4, 0.5),
        'medium': ('trimf', 0.4, 0.5, 0.6),
        'above medium': ('trimf', 0.5, 0.6, 0.7),
        'high': ('trapmf', 0.6, 0.7, 0.8, 0.9),
        'extremely high': ('trapmf', 0.7, 0.9, 1, 1),
    }
}


rule_base = [
    (('z1', 'without_repair', 'small'), 'medium'),
    (('z1', 'without_repair', 'average'), 'medium'),
    (('z1', 'without_repair', 'extra'), 'medium'),
    (('z1', 'satisfied', 'small'), 'medium'),
    (('z1', 'satisfied', 'average'), 'high'),
    (('z1', 'satisfied', 'extra'), 'high'),
    (('z1', 'with_repair', 'small'), 'low'),
    (('z1', 'with_repair', 'average'), 'low'),
    (('z1', 'with_repair', 'extra'), 'low'),
    (('z2', 'without_repair', 'small'), 'medium'),
    (('z2', 'without_repair', 'average'), 'medium'),
    (('z2', 'without_repair', 'extra'), 'medium'),
    (('z2', 'satisfied', 'small'), 'medium'),
    (('z2', 'satisfied', 'average'), 'medium'),
    (('z2', 'satisfied', 'extra'), 'medium'),
    (('z2', 'with_repair', 'small'), 'medium'),
    (('z2', 'with_repair', 'average'), 'medium'),
    (('z2', 'with_repair', 'extra'), 'medium'),
    (('z3', 'without_repair', 'small'), 'medium'),
    (('z3', 'without_repair', 'average'), 'medium'),
    (('z3', 'without_repair', 'extra'), 'medium'),
    (('z3', 'satisfied', 'small'), 'medium'),
    (('z3', 'satisfied', 'average'), 'medium'),
    (('z3', 'satisfied', 'extra'), 'medium'),
    (('z3', 'with_repair', 'small'), 'medium'),
    (('z3', 'with_repair', 'average'), 'medium'),
    (('z3', 'with_repair', 'extra'), 'medium'),
]