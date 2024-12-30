#841. Keys and Rooms
#Medium
#problem statement:   https://leetcode.com/problems/keys-and-rooms/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #final optimal and concise version without any comments
        self.unvisited = len(rooms)
        visted_room = set()

        def dfs(room):
            if room not in visted_room:
                visted_room.add(room)
                self.unvisited -= 1
                for j in range(len(rooms[room])):
                    dfs(rooms[room][j])
        dfs(0)
        return self.unvisited == 0

        
        #this time, realized that key_set was very unnecessary, the code can run without it and faster 
        '''
        self.unvisited = len(rooms)
        visted_room = set()
        #key_set = {0}

        def dfs(room):
            if room not in visted_room:
                #if room in key_set:
                visted_room.add(room)
                self.unvisited -= 1
                key_num = len(rooms[room])
                for j in range(key_num):
                    #key_set.add(rooms[room][j])
                    dfs(rooms[room][j])
        dfs(0)
        if self.unvisited > 0: return False
        else: return True
        '''

        #my inital unoptimized code that passed all the test cases are below
        '''
        self.unvisited = len(rooms)
        visted_room = set()
        key_set = {0}

        def dfs(room):
            if room not in visted_room:
                if room in key_set:
                    visted_room.add(room)
                    self.unvisited -= 1
                    #then now get the key that bring us to the room
                    key_num = len(rooms[room])
                    for j in range(key_num):
                        key_set.add(rooms[room][j])
                        dfs(rooms[room][j])
                #else: #then what: could create an want list, but it doens't really matter that we know which room we went through is unlocked yet, so just use unvisted math to make it easier
            #else do nothing
        #for i in range (self.unvisited):   # a better optimization is htat this line is not needed, which mean we do not need to loop through the input rooms, because for same reason, the room unvisited doens not matter in any way
        #   dfs(i)
        dfs(0)
        if self.unvisited > 0: return False
        else: return True
        '''
