class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)

        stack = []
        time = 0

        for pos, speed in cars:
            t = (target - pos)/speed
            stack.append(t)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)



        