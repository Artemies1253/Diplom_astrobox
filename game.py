# -*- coding: utf-8 -*-

from astrobox.space_field import SpaceField
from devastator import DevastatorDrone
from olshannikov_d_a import OlshannikovDron

NUMBER_OF_DRONES = 5


class DevastatorDrone2(DevastatorDrone):
    pass


class DevastatorDrone3(DevastatorDrone):
    pass


if __name__ == '__main__':
    scene = SpaceField(
        field=(1200, 1000),
        speed=5,
        asteroids_count=27,
        can_fight=True,
    )
    team_1 = [OlshannikovDron() for _ in range(NUMBER_OF_DRONES)]
    team_3 = [DevastatorDrone3() for _ in range(NUMBER_OF_DRONES)]
    team_2 = [DevastatorDrone2() for _ in range(NUMBER_OF_DRONES)]
    team_4 = [DevastatorDrone() for _ in range(NUMBER_OF_DRONES)]
    scene.go()
