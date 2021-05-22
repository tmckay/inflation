"""
Calculates inflation between two years
"""

import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('from_year')
    parser.add_argument('to_year')
    return parser.parse_args()


def get_level(line):
    _, level = line.split(',')
    return float(level)


def get_inflation(from_year, to_year):
    with open('CPIAUCNS.csv') as fh:
        for line in fh.readlines():
            if line.startswith(f'{from_year}'):
                from_level = get_level(line)
            if line.startswith(f'{to_year}'):
                to_level = get_level(line)

    inflation = (to_level - from_level) / from_level
    inflation = inflation * 100
    print(f'Inflation has grown {inflation:.2f}% '
          f'from {from_year} to {to_year}')



def main():
    args = get_args()
    get_inflation(args.from_year, args.to_year)


if __name__ == '__main__':
    main()
