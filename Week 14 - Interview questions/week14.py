
"""
Total Logical Ordering

4 -> 
     0 -> 1 -> 3 -> 2 -> 0
5 -> 

Process 0 depends on process 1 to finish
Process 1 depends on process 3 to finish
Process 3 depends on process 2 to finish
Process 2 depends on process 0 to finish
Process 4 depends on process 0 to finish
Process 5 depends on process 0 to finish

4 -> 
     0 -> 1 -> 3 -> 2
5 ->   -> 2

TO list: [2, 3, 1, 0, 4, 5] or [2, 3, 1, 0, 5, 4]
Can do either because it doesn't matter if 4 or 5 comes first
Total combination of process need not be unique

Pre-requisite list ordering: [2, 3, 1, 0, 4, 5]
Course 2 has a pre-requisite of None
Course 3 has a pre-requisite of 2
Course 1 has a pre-requisite of 3
Course 0 has a pre-requisite of 1 and 2
Course 4 has a pre-requisite of 0
Course 5 has a pre-requisite of 0

pRL = [[0,1], [0, 2], [1, 3], [3, 2], [4, 0], [5, 0]]
n = 6

Adjacency List:
AL = 0 -> [1, 2]
        1 -> [3]
        2 -> []
        3 -> [2]
        4 -> [0]
        5 -> [0]
        
Need two hash sets for visiting and visited states: visiting = set(), visited = set()

Start at 0, add 0 to visiting,
go to 1, add 1 to visiting
go to 3, add 3 to visiting
go to 2, add 2 to visiting
go back, add 3 to visited, etc.

AL = {i: [] for i in range(n)}
for i, j in pRL:
    AL[j].append(i)
    
visited = set()
TO = []
visiting = set()

def dfs(crs):
    if crs in visiting:
        return False
    if crs in visited:
        return True
    visiting.add(crs)
    for i in AL[crs]:
        if not dfs(i):
            return False
    visiting.remove(crs)
    visited.add(crs)
    TO.append(crs)
    return True
    
for i in range(n):
    if not dfs(j):
        return []
        
Time Complexity: O(V + E)
Space Complexity: O(V)
"""

n = 6
pRL = [[0,1], [0, 2], [1, 3], [3, 2], [4, 0], [5, 0]]

AL = {i: [] for i in range(n)}
for i, j in pRL:
    AL[j].append(i)

visited = set()
TO = []
visiting = set()

def dfs(crs):
    if crs in visiting:
        return False
    if crs in visited:
        return True
    visiting.add(crs)
    for i in AL[crs]:
        if not dfs(i):
            return False
    visiting.remove(crs)
    visited.add(crs)
    TO.append(crs)
    return True

for i in range(n):
    if not dfs(j):
        print([])
        break
    
print(TO)

""" 
4/17/2024

Internship:
The interview in these jobs are not interviews, they're tests.
The tests are looking to see if you can solve the problems they give you.

Structure way to prepare for an interview:
1. CTCI - Cracking the Coding Interview (Beginner Friendly)
2. EPI - Elements of Programming Interviews (Not Beginner Friendly) Most Realistic set of questions for Big Tech
3. LeetCode

Course Recommendation:
1. Data Structures and Algorithms, System Level Programming, Computer Org
2. Programming Language Concepts, Algorithms, Operating Systems

Specialize Courses:
1. Cyber Security (Good at Linux and C)
2. Machine Learning (Python and Data Strcuture | Linear Algebra 2, Mathematical Statistics 1 & 2, Optimization)
3. Network Security (Good at Linux and C)
4. Data Security (Good at Linux and C)
5. 
"""