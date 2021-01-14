import random
from typing import Iterable, Any, List


class City(object):

    def __init__(self, name: str, x: int, y: int, elevation: int) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.elevation = elevation

    def __str__(self) -> str:
        return f'{self.name},{self.x},{self.y},{self.elevation}'

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, City):
            return self.x == other.x and self.y == other.y and self.elevation == other.elevation
        else:
            return False

    def __ne__(self, o: object) -> bool:
        return not (self == o)

    def __hash__(self) -> int:
        return 3 * self.x + 5 * self.y + 7 * self.elevation


def create_country(result_file: str,
                   distance_constant: int,
                   elevation_constant: int,
                   city_names: [Iterable[Any]],
                   min_x: int, max_x: int,
                   min_y: int, max_y: int,
                   min_elevation: int, max_elevation: int):
    cities = set()
    for name in city_names:
        while True:
            city = City(str(name),
                        random.randint(min_x, max_x),
                        random.randint(min_y, max_y),
                        random.randint(min_elevation, max_elevation))
            if city not in cities:
                break
        cities.add(city)

    with open(result_file, 'w') as road_file:
        road_file.write(f'{distance_constant}\n')
        road_file.write(f'{elevation_constant}\n')
        road_file.write('\n'.join((str(city) for city in cities)))


def main():
    # replace the values below to create a different random country
    cities = ['Davis', 'Sacramento', 'LA', 'Tahoe', 'San Francisco']
    create_country('test_countries/California.txt',
                   2, 1,
                   cities,
                   -10000, 10000,
                   -500, 500,
                   0, 2000)


if __name__ == '__main__':
    main()
