class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = (sorted(zip(position,speed))[::-1])
        fleetCount = 1
        lastFleetTime = (target-pair[0][0])/pair[0][1]
        for p,s in pair:
            currentTime = (target-p)/s
            if currentTime > lastFleetTime:
                fleetCount += 1
                lastFleetTime = currentTime
        return fleetCount
            
           

        