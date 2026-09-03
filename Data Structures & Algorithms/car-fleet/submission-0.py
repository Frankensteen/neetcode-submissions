class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create pairs of (position, speed) and sort by position in descending order
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)  # Sort by position (closest to target first)
        
        fleets = 0
        prev_time = 0  # Time of the previous fleet
        
        # Process cars from closest to farthest from target
        for pos, spd in cars:
            # Calculate time for this car to reach target
            time = (target - pos) / spd
            
            # If this car takes longer than previous fleet, it forms a new fleet
            if time > prev_time:
                fleets += 1
                prev_time = time  # Update previous fleet time
        
        return fleets
        # as cars can not pass each other, the car which is at max position will  reach first. we have to find if cars before it can catch up until it reaches destination. once first fleet reaches we have to do same for next set of cars.
        
        #make position speed pair. sort by position in descending order
        #find time for first car to reach destination. if position + speed*time for other cars behind>= target, keep adding in stack
        # else result+=1, i.e first fleet is done, do for nexr fleet.
        #return the result


        