import analytics as a
import dsa_tracker as d

d.add_problem("Arrays", "Two Sum", "Solved")
d.add_problem("DP", "Knapsack", "Solved")
d.add_problem("Graphs", "BFS", "Unsolved")

print("Topic Analysis:")
print(a.dsa_topic_analysis())

print("Completion Rate:")
print(a.completion_rate())