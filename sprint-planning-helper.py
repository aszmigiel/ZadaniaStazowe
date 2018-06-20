import csv
import sys

class Task:
 '''Task class contains all info about task'''
 def __init__(self,task_id,story_points,ksp):
  '''Simple class constructor'''
  self.id=int(task_id)
  self.points=int(story_points)
  self.ksp=int(ksp)
  self.ratio=float(float(ksp)/float(story_points))

 def display(self):
  '''Prints info about task'''
  sys.stdout.write('Id '+str(self.id) + ' KSP '+str(self.ksp)+' Ratio ' +str(self.ratio))

def getRatio(task):
 return task.ratio

file_name = str(sys.argv[1])
velocity=int(sys.argv[2])
tasks=[]

with open(file_name) as f:
 reader = csv.DictReader(f)
 for row in reader:
  tasks.append(Task(row['task_id'],row['story_points'],row['KSP']))
'''Used algorithm is called greedy algorithm'''
tasks.sort(key=getRatio,reverse=True)
selected_tasks=[]
actual_size=0
for task in tasks:
 if(actual_size+task.points<velocity):
  selected_tasks.append(str(task.id))


sys.stdout.write(",".join(selected_tasks))
sys.stdout.write("\n")




    
