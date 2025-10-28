
def validate_input(min: int, max: int):

    user_input = input(f'Seleccione una opcion: [{min} - {max}]: ')

    if not user_input.isdigit() or not (min <= int(user_input) <= max):
        print(f'Error, seleccione entre {min} - {max}')
        user_input = validate_input(min, max)
    return int(user_input)