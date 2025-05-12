import sys


class FrameNode():

    def __init__(self, frame_count: int, roll1: str, roll2: str, roll3: str):
        self.frame_count = frame_count
        self.roll1 = roll1
        self.roll2 = roll2
        self.roll3 = roll3
        self.score = 0

        self.next = None
        self.prev = None

    def __repr__(self):
        return f'roll 1: {self.roll1}, roll 2: {self.roll2}'


##### HELPER METHODS #####
def roll_value(roll: str, prev: int = 0) -> int:
        if roll == 'X':
            return 10
        if roll == '/':
            return 10 - prev
        return int(roll)



class Game():               # linked list used for frames

    def __init__(self): 
        """ initialises doubly linked list to hold FrameNodes to track each frame's score """
        self.head = None
        self.tail = None
        self._size = 1
        self.running_total = 0

    def __repr__(self):
        """ MISTAKE: focused on self causing me to use self.frame_count to access var, how
         ever remember it is the POINTER current which accesses var as current.frame_count """
        frames = []

        current = self.head
        while current:
            # [Frame 1: <8> </> ]-[Frame 2: <X> <> ]-[Frame`

            # Frame 10 - 3 rolls
            if self._size == 10:
                frames.append(f'[Frame {current.frame_count}: <{current.roll1}> <{current.roll2}> <{current.roll3}> ]')
                
            # Frames 1 - 9
            else:
                frames.append(f'[Frame {current.frame_count}: <{current.roll1}> <{current.roll2}> ]')
            
            current = current.next
        return "-".join(frames)
        
    def print_frames(self):
        frames = []
        running_total = self.get_running_total()
        index = 0
        current = self.head
        while current:
            # print frames 1 - 9
            if current.frame_count == 10:
                frames.append(f'[Frame {current.frame_count}: <{current.roll1}> <{current.roll2}> <{current.roll3}> Score: {running_total[index]}]')
            # frame 10
            else:
                frames.append(f'[Frame {current.frame_count}: <{current.roll1}> <{current.roll2}> Score: {running_total[index]}]')
            index += 1
            current = current.next
        return "-".join(frames)

    def get_running_total(self):
        frame_totals = []
        running_total = 0
        current = self.head
        while current:
            running_total += current.score
            frame_totals.append(running_total)
            current = current.next
        return frame_totals

    def append(self, roll1: str, roll2: str, roll3="") -> FrameNode:

        new_frame = FrameNode(self._size, roll1, roll2, roll3)
        
        # empty list, first node
        if self.head == None:
            # new_frame.next = self.head  OMIT THIS 
            self.head = new_frame
            self.tail = new_frame       # attach tail and head to first node
        # list with more than one node
        else:
            new_frame.prev = self.tail
            # not new_frame.prev, use SELF.HEAD.PREV
            self.tail.next = new_frame
            self.tail = new_frame

        self._size += 1
    
    def load_scores(self, scores_string: str) -> str:
        scores = scores_string.split(" ")
        for score in scores:
            rolls = [c for c in score]
            if len(rolls) > 2:
                roll1, roll2, roll3 = rolls[0], rolls[1], rolls[2]
                self.append(roll1, roll2, roll3)
            elif len(rolls) > 1:
                roll1, roll2 = rolls[0], rolls[1]
                self.append(roll1, roll2)
            # strike = r1: X r2: ""
            elif rolls[0] == 'X':
                self.append(rolls[0], "")

    def open_frame(roll1, roll2, roll3):
        pass

    def score_tenth_frame(self,  r1: str, r2: str, r3: str = '') -> int:
        """ returns a score for the tenth frame """
        # build the list of rolls, skipping any empty third roll
        rolls = [r1, r2] + ([r3] if r3 else [])
        frame_score = 0
        prev = 0

        for roll in rolls:
            roll_score = roll_value(roll, prev)
            frame_score += roll_score
            prev = roll_score

        return frame_score
        
    def get_score(self, frame_count: int, roll1: str, roll2: str, roll3: str) -> int:
        # add roll3 of frame 10 if applicable
        if frame_count == 10:
            return self.score_tenth_frame(roll1, roll2, roll3)
        else:
            return 10 if roll1 == 'X' or roll2 == '/' else int(roll1) + int(roll2)

    def adjust_previous_frame_score(self, current_frame: FrameNode, previous_frame: FrameNode):
        if previous_frame.roll1 == 'X':
            previous_frame.score += current_frame.score # the previous frame's strike captures both roll1 and roll2 scores in current frame
        
        elif previous_frame.roll2 == '/':
            previous_frame.score += 10 if current_frame.roll1 == 'X' else int(current_frame.roll1)  # the previous frame's SPARE captures ONLY roll1 score in current frame
            
    def bonus_score(self, current_frame):
        # bonus refers to a striker or spare
        previous_frame = current_frame.prev

        if current_frame.frame_count != 10:
            # previous frame bonus score check for frames 1-9
            self.adjust_previous_frame_score(current_frame, previous_frame)
            
            # previous previous frame bonus score check
            if current_frame.frame_count > 2:
                previous_previous_frame = current_frame.prev.prev

                if previous_previous_frame.roll1 == 'X' and previous_frame.roll1 == 'X':
                    # awards 10 pts for 3rd strike in a row; or r1 pts
                    previous_previous_frame.score += 10 if current_frame.roll1 == 'X' else int(current_frame.roll1)

        # 10th frame bonus score check
        else:       # Turkey -> Frame 9: X, Frame 10: X(R1) X(R2)
            previous_previous_frame = current_frame.prev.prev
            
            if previous_previous_frame.roll1 == 'X' and previous_frame.roll1 == 'X' and current_frame.roll1 == 'X':
                # awards 10 pts for 3rd strike in a row; or r1 pts
                previous_previous_frame.score += 10 if current_frame.roll1 == 'X' else int(current_frame.roll1)

            # 10th frame double strike
            if previous_frame.roll1 == 'X' and current_frame.roll1 == 'X' and current_frame.roll2 == 'X':
                previous_frame.score += 10 + 10
            
            # SPARES 
            elif previous_frame.roll2 == '/':
                previous_frame.score += 10 if current_frame.roll1 == 'X' else int(current_frame.roll1) 

    def calculate_score(self):
        """ returns the total of each frame's score  """
        current = self.head

        while current:
            # score current frame
            current.score = self.get_score(
                current.frame_count, 
                current.roll1, 
                current.roll2, 
                current.roll3
            )
            
            # check Bonus score from frame 2 onwards
            # if current.frame_count > 1 and (current.roll1 == 'X' or current.roll2 =='/'):
            if current.frame_count > 1:
                self.bonus_score(current)

            current = current.next


# uncomment below before running in the command line
# if __name__ == "__main__":
#     game = Game()
#     score_input = sys.argv[1]
#     game.load_scores(score_input)
#     game.calculate_score()
#     print(game.print_frames())



    


    



        











