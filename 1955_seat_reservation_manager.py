import heapq

class SeatManager:

    def __init__(self, n: int):
        self.available = list(range(1, (n+1)))
        heapq.heapify(self.available)
        

    def reserve(self) -> int:
        return heapq.heappop(self.available)
        

    def unreserve(self, seatNumber: int) -> None:
        return heapq.heappush(self.available, seatNumber)

        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)


# import heapq

# class SeatManager:

#     def __init__(self, n: int):
#         self.available = list(range(1, (n+1)))
#         heapq.heapify(self.available)

#     def reserve(self) -> int:
#         return heapq.heappop(self.available)

        
#     def unreserve(self, seatNumber: int) -> None:
#         return heapq.heappush(self.available, seatNumber)
        

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

# Brute Force - O(n)

# class SeatManager:

#     def __init__(self, n: int):
#         self.seats = [-1] * (n+1)

#     def reserve(self) -> int:
#         for seat in range(1, len(self.seats)):
#             if self.seats[seat] == -1:
#                 self.seats[seat] = 1
#                 return seat

#     def unreserve(self, seatNumber: int) -> None:
#         self.seats[seatNumber] = -1