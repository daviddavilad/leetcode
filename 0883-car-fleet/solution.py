class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        cars = list(zip(position, speed))
        cars.sort()
        count = 0

        for p,s in reversed(cars):
            current_time = (target - p) / s
            if not time:
                time.append(current_time)
                count += 1
                continue
            if current_time <= time[-1]:
                continue
            else:
                time.append(current_time)
                count += 1

        return count
