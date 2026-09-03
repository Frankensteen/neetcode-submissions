class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair cars and sort by position (descending)
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        current_fleet_time = 0
        
        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            
            # If this car takes longer, it must form a new fleet
            if time_to_target > current_fleet_time:
                fleets += 1
                current_fleet_time = time_to_target
        
        return fleets
        # as cars can not pass each other, the car which is at max position will  reach first. we have to find if cars before it can catch up until it reaches destination. once first fleet reaches we have to do same for next set of cars.
        
        #make position speed pair. sort by position in descending order
        #find time for first car to reach destination. if position + speed*time for other cars behind>= target, keep adding in stack
        # else result+=1, i.e first fleet is done, do for nexr fleet.
        #return the result


        