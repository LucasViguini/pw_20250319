def string_contem_somente_numeros(s):
    return all(c.isdigit() or c.isspace() for c in s) 