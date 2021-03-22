from dataclasses import dataclass

@dataclass
class Trip:
    begin: int = None
    end: int = None
    start: str = None
    stop: str = None

class UndergroundSystem:
    # this problem makes a lot more sense with a DB
    # we could solve it without a DB, but there's a lot of relationships between the different 'tables'

    def __init__(self):
        self.customers = dict()
        # self.trips = []
        self.trips = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        trip = Trip(begin=t, start=stationName)
        self.customers[id] = trip

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        trip = self.customers[id]
        trip.end = t
        trip.stop = stationName

        pair = (trip.start, trip.stop)
        if pair not in self.trips:
            self.trips[pair] = []

        # self.trips.append(trip)
        self.trips[pair].append(trip)
        self.customers[id] = None

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        pair = (startStation, endStation)
        if pair not in self.trips:
            self.trips[pair] = []

        lengths = [trip.end - trip.begin for trip in self.trips[pair]]
        # lengths = [trip.end - trip.begin for trip in self.trips if trip.start == startStation and trip.stop == endStation]
        # print(lengths, sum(lengths), len(lengths))

        return sum(lengths) / len(lengths)