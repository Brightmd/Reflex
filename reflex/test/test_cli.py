#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from reflex.cli import validate_upgrade
from reflex.error import InvalidUpgradePath


def test_validate_upgrade():
    can_upgrade = [
        ('1.0.0', '1.0.1'),
        ('1.0.0', '1.1.0'),
        ('1.0.0', '2.0.0'),
        ('1.0.0', '3.2.1'),
        ('0.0.0', '1.2.3'),
        ('1.2.5', '1.9.1'),
        ('1.11.1', '1.12.3'),
        ('1.11.1', '2.0.0'),
    ]
    fails_upgrade = [
        ('1.0.0', '1.0.0'),
        ('1.0.1', '1.0.0'),
        ('1.1.0', '1.0.0'),
        ('2.0.0', '1.0.0'),
        ('3.2.1', '1.0.0'),
        ('1.2.3', '0.0.0'),
        ('1.9.5', '1.8.9'),
        ('1.19.3', '1.13.1'),
        ('2.0.0', '1.13.1'),
    ]

    for path in can_upgrade:
        assert validate_upgrade(*path)

    for path in fails_upgrade:
        with pytest.raises(InvalidUpgradePath):
            validate_upgrade(*path)
