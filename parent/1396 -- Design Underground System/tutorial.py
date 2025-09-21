class UndergroundSystem:

    def __init__(self):
        # these data structures basically solve the problem
        self.checkInMap = {}    # id -> (startStation: time)
        self.totalMap = {}      # (startStation, endStation) -> [totalTime, count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.checkInMap[id]
        route = (start, stationName)

        if route not in self.totalMap:
            self.totalMap[route]  = [0,0]
            
        self.totalMap[route][0] += t - time
        self.totalMap[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # print(self.times)
        total, count = self.totalMap[(startStation, endStation)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)