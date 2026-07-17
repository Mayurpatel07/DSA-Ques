class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque

class Solution:
    def countStudents(self, students, sandwiches):
        q = deque(students)
        i = 0                  # Current sandwich
        rotation = 0           # Students moved to back without eating

        while q and rotation < len(q):

            if q[0] == sandwiches[i]:
                q.popleft()    # Student takes sandwich
                i += 1         # Next sandwich
                rotation = 0   # Reset because someone ate

            else:
                q.append(q.popleft())   # Move student to back
                rotation += 1

        return len(q)