from django.db import models
from django.db.models.signals import pre_save
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


def validate_control(sender, instance, **kwargs):
    """
    Used to validate Control Model as Follow:
    Name must not be null or empty
    Type should be within defined choices
    Maximum Rabi Rate must have a value between 0 and 100
    Polar Angle must have a value between 0 and 1
    """

    if not instance.name:
        raise ValidationError('Control must have a name')

    if instance.type.lower() not in Control.TYPE:
        raise ValidationError('Control type must be: Primitive, CORPSE, Gaussian, CinBB or CinSK')

    if not (0 <= instance.max_rabi_rate <= 100):
        raise ValidationError('Maximum Rabi Rate value must be between 0 and 100')

    if not (0 <= instance.polar_angle <= 1):
        raise ValidationError('Polar Angle value must be between 0 and 1')


class Control(models.Model):
    """Defines a Control Model"""

    # The following represents types of Control
    PRIMITIVE = 'Primitive'
    CORPSE = 'CORPSE'
    GAUSSIAN = 'GAUSSIAN'
    CINBB = 'CinBB'
    CINSK = 'CinSK'
    # Used for choices shown in form
    TYPE_CHOICES = [
        (PRIMITIVE, 'Primitive'),
        (CORPSE, 'CORPSE'),
        (GAUSSIAN, 'Gaussian'),
        (CINBB, 'CinBB'),
        (CINSK, 'CinSK'),
    ]
    # A list used for validation
    TYPE = [value[0].lower() for value in TYPE_CHOICES]

    # Name of the control
    name = models.CharField(max_length=255)

    # Control Type. Limited to several choices (See above)
    type = models.CharField(max_length=9, choices=TYPE_CHOICES)

    # maximum achievable angular frequency of the Rabi cycle for a driven quantum transition.
    # Must be between 0 and 100
    max_rabi_rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    # An angle measured from the z-axis on the Bloch sphere. Must be between 0 and 1 (units of pi)
    polar_angle = models.DecimalField(max_digits=6, decimal_places=5, validators=[MinValueValidator(0),
                                                                                  MaxValueValidator(1)])

    def __str__(self):
        """Returns a string representation of the Control"""

        return self.name


pre_save.connect(validate_control, sender=Control)
