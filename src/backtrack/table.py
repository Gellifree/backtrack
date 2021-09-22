#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#

class Table(object):
    @staticmethod
    def draw(n = 4, data = []):
        print(f'\n A(z) {n}*{n} táblázat kirajzolása:')
        print()
        for i in range(n):
            print(' ', end='')
            for j in range(n):
                if(len(data) > 0):
                    if(data[i][j] == 0):
                        print("[ ]", end='')
                    else:
                        print(f"[{data[j][i]}]", end='')
                else:
                    print("[ ]", end='')
            print()
        print()
