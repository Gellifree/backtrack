#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#

from backtrack import table
from backtrack import error_handler
from backtrack import solver


def main():
    data = solver.Solver.solve()
    table.Table.draw(8, data)


if __name__ == "__main__":
    main()
