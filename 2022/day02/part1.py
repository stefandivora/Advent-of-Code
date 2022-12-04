import os

INPUT = os.path.join(os.path.dirname(__file__), 'data.in')


def day02_1(filename=INPUT) -> int:
    points = {
        'draw': 3,
        'win': 6,
        'lose': 0
    }

    lut = {
        'AX': points['draw'],
        'BY': points['draw'],
        'CZ': points['draw'],
        'AY': points['win'],
        'AZ': points['lose'],
        'BX': points['lose'],
        'BZ': points['win'],
        'CX': points['win'],
        'CY': points['lose']
    }

    shape_lut = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    return sum([lut[l.rstrip().replace(' ', '')] + shape_lut[l.rstrip().replace(' ', '')[1]] for l in
                open(filename).readlines()])


if __name__ == '__main__':
    print(day02_1())
