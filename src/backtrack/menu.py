#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#

class Menu(object):
    def draw(self, data):
        for i in range(len(data)):
            print(f" [{i}] {data[i]}")


def up():
    print('up')

def down():
    print('down')

def main():
    list = ['Első', 'Második', 'Harmadik']
    mn = Menu()
    mn.draw(list)
    import enquiries

    options = ['Első', 'Második', 'Harmadik', 'Negyedik']
    choice = enquiries.choose('Choose one of these options: ', options, multi=True)

    print(choice)

    if enquiries.confirm('Do you want to write something?'):
        text = enquiries.freetext('Write something interesting: ')
        print(text)


if __name__ == '__main__':
    main()
