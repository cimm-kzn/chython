# -*- coding: utf-8 -*-
#
#  Copyright 2022-2024 Ramil Nugmanov <nougmanoff@protonmail.com>
#  Copyright 2023 Timur Gimadiev <timur.gimadiev@gmail.com>
#  This file is part of chython.
#
#  chython is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, see <https://www.gnu.org/licenses/>.
#


template = {
    'name': 'Sulfoamination reaction ',
    'description': 'Sulfoamination reaction, S-N coupling reaction',
    'templates': [
        {
            'A': [
                # RS(=O)(=O)X
                '[S;D4;x3;z3:1]([O,F,Cl,Br,I;D1:2])(=[O;M])(=[O;M])[C;M]'
            ],
            'B': [
                # Ar-NH2
                '[N;D1;x0;z1:3][C;a;M]',
                # Alk-NH2
                '[N;D1;x0;z1:3][C;z1;x1;M]',
                # Ar-NH-Ar
                '[N;D2;x0;z1:3]([C;a;M])[C;a;M]',
                # Alk-NH-Ar
                '[N;D2;x0;z1:3]([C;a;M])[C;z1;x1;M]',
                # Alk2NH
                '[N;D2;x0;z1:3]([C;z1;x1;M])[C;z1;x1;M]'
            ],
            'product': '[A:1]-[A:3]',
            'alerts': [],
            'ufe': {
                'A': 2,
                'B': '[A:3][U;M]'
            }
        },
    ],
    'alerts': []
}
