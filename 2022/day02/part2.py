import os

INPUT = os.path.join(os.path.dirname(__file__), 'data.in')


def day02_2(filename=INPUT) -> int:
    points = {
        'draw': 3,
        'win': 6,
        'lose': 0
    }

    def strategy_map(r):
        shape_lut = {
            'X': 1,
            'Y': 2,
            'Z': 3
        }

        lut = {
            'AX': points['lose'] + shape_lut['Z'],
            'BY': points['draw'] + shape_lut['Y'],
            'CZ': points['win'] + shape_lut['X'],
            'AY': points['draw'] + shape_lut['X'],
            'AZ': points['win'] + shape_lut['Y'],
            'BX': points['lose'] + shape_lut['X'],
            'BZ': points['win'] + shape_lut['Z'],
            'CX': points['lose'] + shape_lut['Y'],
            'CY': points['draw'] + shape_lut['Z']
        }

        return lut[r]

    return sum(map(strategy_map, [l.rstrip().replace(' ', '') for l in open(filename).readlines()]))


if __name__ == '__main__':
    print(day02_2())
