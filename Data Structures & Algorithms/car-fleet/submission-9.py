class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # x - position of car ; y - speed of car ; z - time
        # position of car at a given time is x + zy
        # go through the cars right to left (position) and compare their speed and we can form fleet if there is a car on
        # the right much slower than the car on the left

        # if there is a slower car on the left (that is a new fleet) --> each fleet is a stack

        n = len(position)

        car_ls = []
        for i in range(n):
            car_ls.append((position[i],speed[i]))
        
        car_ls_sorted = sorted(car_ls, reverse = 1)

        fleets = 1
        car_in_front_time = (target - car_ls_sorted[0][0])/car_ls_sorted[0][1]
        for pos,s in car_ls_sorted[1:]:
            curr_car_time = (target - pos)/s
            if curr_car_time > car_in_front_time:
                fleets += 1
                car_in_front_time = curr_car_time


        return fleets
