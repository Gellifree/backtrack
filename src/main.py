#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#

from backtrack.table import Table
from backtrack.error_handler import ErrorHandler
from backtrack.solver import Solver


def main():
    data = Solver.solve()
    Table.draw(8, data)


if __name__ == "__main__":
    main()
