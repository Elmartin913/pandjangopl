import re
from django.core.exceptions import ValidationError



def phone_validator(value):
    v = re.match('^[0-9\+]{8,13}$', value)
    if v is None:
        raise ValidationError('Tylko cyfry (min.9) np.111222333')
    return True
