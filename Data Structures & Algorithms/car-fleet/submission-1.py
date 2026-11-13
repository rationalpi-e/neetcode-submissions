class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        fleet = 0
        time = 0

        for pos,  spd in cars:
            cur_time = (target - pos)/spd
            if cur_time > time:
                fleet += 1
                time = cur_time

        return fleet