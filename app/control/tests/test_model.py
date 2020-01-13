# Created by: Aymen Al-Quaiti
# For QCTRL Backend Challenge
# January  2020

from django.test import TestCase
from django.core.exceptions import ValidationError
from control.models import Control


class ControlModelTests(TestCase):
    """Used to test Control"""

    def test_create_control(self):
        """Test that a control was created"""

        control = Control.objects.create(name='Single-Qubit Driven', type=Control.PRIMITIVE, maximum_rabi_rate=65,
                                         polar_angle=0.5)

        self.assertEqual(str(control), control.name)

    def test_create_control_type_failed(self):
        """Test that a control with type not within defined choices would raise a validation error"""

        with self.assertRaises(ValidationError):
            control = Control.objects.create(name='Single-Qubit Driven', type='prim', maximum_rabi_rate=100,
                                             polar_angle=0.5)

    def test_create_control_rabi_rate_failed(self):
        """Test that a control with maximum rabi rate not within allowed range"""

        with self.assertRaises(ValidationError):
            control = Control.objects.create(name='Single-Qubit Driven', type='Primitive', maximum_rabi_rate=101,
                                             polar_angle=0.5)

    def test_create_control_polar_angle_failed(self):
        """Test that a control with polar angle rate not within allowed range"""

        with self.assertRaises(ValidationError):
            control = Control.objects.create(name='Single-Qubit Driven', type='Primitive', maximum_rabi_rate=101,
                                             polar_angle=-1)