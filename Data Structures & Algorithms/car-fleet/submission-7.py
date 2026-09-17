class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # x - position of car ; y - speed of car ; z - time
        # position of car at a given time is x + zy
        # go through the cars right to left (position) and compare their speed and we can form fleet if there is a car on
        # the right much slower than the car on the left

        # if there is a slower car on the left (that is a new fleet) --> each fleet is a stack

        n = len(position)

        car_dict = {}
        for i in range(n):
            car_dict[position[i]] = speed[i]
        
        sorted_car_dict = sorted(car_dict.items(),reverse = 1)

        stack = []
        fleets = 0
        car_in_front_time = 0
        for pos,s in sorted_car_dict:
            curr_car_time = (target - pos)/s
            # print(curr_car_time, car_in_front_time)
            if car_in_front_time == 0:
                car_in_front_time = curr_car_time
                fleets += 1
            else:
                if curr_car_time > car_in_front_time:
                    fleets += 1
                    car_in_front_time = curr_car_time


        return fleets
