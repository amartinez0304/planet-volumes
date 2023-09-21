#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:08:13 2023

@author: arnulfomartinez
"""

import numpy as np


radii = np.random.randint(1,1000,1000000)

volumes = 4/3 * np.pi * radii ** 3
print(volumes)
