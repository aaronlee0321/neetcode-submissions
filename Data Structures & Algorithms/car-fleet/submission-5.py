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
        for pos,s in sorted_car_dict:
            time = (target - pos)/s
            stack.append(time)

        car_in_front_time = stack[0]
        for idx,time in enumerate(stack[1:]):
            curr_car_time = time
            if curr_car_time <= car_in_front_time:
                stack.remove(time)
            else:
                car_in_front_time = curr_car_time

        return len(stack)
