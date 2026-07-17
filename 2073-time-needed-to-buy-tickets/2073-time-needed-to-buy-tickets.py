from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets, k):

        # Step 1: Create the queue
        q = deque()

        # Store (person_index, remaining_tickets)
        for i in range(len(tickets)):
            q.append((i, tickets[i]))

        # Time starts at 0
        time = 0

        # Step 2: Keep processing until we return
        while q:

            # Front person comes
            idx, rem = q.popleft()

            # He buys one ticket
            rem -= 1
            time += 1

            # If this is person k and he just finished
            if idx == k and rem == 0:
                return time

            # If he still needs tickets,
            # send him to the back
            if rem > 0:
                q.append((idx, rem))