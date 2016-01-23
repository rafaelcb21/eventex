from django.core.exceptions import ValidationError


def cpf_bool(cpf, n=0, count=10, digit_str=''):
    """cpf_bool function validates cpf returning True or False"""

    list_1 = []
    for num in cpf[:9 + n]:
        var = int(num) * count
        list_1.append(var)
        count -= 1

    digit = sum(list_1) % 11
    digit = 0 if digit < 2 else 11 - digit

    digits = digit_str + str(digit)

    if len(digits) < 2:
        return cpf_bool(cpf, 1, 11, digits)

    return True if cpf[:9] + digits == cpf else False


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números.', 'length')

    if cpf_bool(value) is False:
        raise ValidationError('CPF inválido', 'valid')