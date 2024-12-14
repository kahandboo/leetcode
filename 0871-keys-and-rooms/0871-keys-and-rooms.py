class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self._rooms = rooms
        self._seen = set()

        self._canVisitAllRooms(0)

        if len(self._rooms) == len(self._seen):
            return True
        else:
            return False

    def _canVisitAllRooms(self, room_idx:int):
        self._seen.add(room_idx)
        keys = self._rooms[room_idx]

        for key in keys:
            if key not in self._seen:
                self._canVisitAllRooms(key)
