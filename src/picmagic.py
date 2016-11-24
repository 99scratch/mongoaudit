# -*- coding: utf-8 -*-

import urwid

def read(path, width=76, align='left'):

    def line_process(line):
        return urwid.AttrMap(urwid.Text(map(pixel_process, line), wrap='clip', align=align), 'pic')

    def pixel_process(color):
        attr = urwid.AttrSpec(color, color, 256)
        return (attr, ' ')

    def round_compo(compo):
        dec = ord(compo)
        return hex(dec)[2]

    with open(path, 'r') as f:
        bytes = f.read()
    blength = len(bytes)
    line_size = width*3
    height = len(bytes)/line_size
    clength = width*height*3
    pic = []
    for i in range(blength-clength, blength, line_size):
        raw_line = bytes[i:i+line_size]
        row = []
        for j in range(0, line_size, 3):
            raw_pixel = raw_line[j:j+3][::-1]
            color = '#' + ''.join(map(round_compo, raw_pixel))
            row.append(color)
        pic.append(row)
    w = urwid.Pile(map(line_process, pic[::-1]))
    return w



