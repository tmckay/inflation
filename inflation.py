#!/usr/local/bin/python
"""
Calculates inflation between two years
"""

import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('from_year')
    parser.add_argument('to_year')
    parser.add_argument('--dollar', default=1, type=int, required=False)
    return parser.parse_args()


def get_level(line: str) -> float:
    _, level = line.split(',')
    return float(level)


def get_inflation(from_year: str, to_year: str, dollar: int):
    from_level = to_level = None
    with open('CPIAUCNS.csv') as fh:
        for line in fh.readlines():
            if line.startswith(f'{from_year}'):
                from_level = get_level(line)
            if line.startswith(f'{to_year}'):
                to_level = get_level(line)

    if not from_level:
        exit(f'{from_year} is not available in data')

    if not to_level:
        exit(f'{to_year} is not available in data')

    inflation = (to_level - from_level) / from_level

    to_dollar = dollar * (1 + inflation)

    inflation = inflation * 100
    print(f'The value of a dollar has changed {inflation:.2f}% '
          f'from {from_year} to {to_year}')
    print(f'${dollar:,.2f} in {from_year} is ${to_dollar:,.2f} in {to_year}')


def main():
    args = get_args()
    get_inflation(args.from_year, args.to_year, args.dollar)


if __name__ == '__main__':
    main()
