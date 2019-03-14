import __main__
try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk
	
from tkinter import *
import scoring

remaining = 0

def snooze ():
  """
  Snoozes for the given number of seconds. During the snooze, a progress
  dialog is launched notifying the 
  """
  secs=10
  global remaining
  root = Tk()
  prompt = 'hello'
  label1 = tk.Label(root, text=prompt, width=len(prompt))
  label1.pack()

  remaining = secs
  
  def decrement_label ():
    global remaining
    text = "Snoozing %d sec(s)" % remaining
    remaining -= 1
    label1.config(text=text, width=100)
    label1.update_idletasks()

  for i in range(1, secs + 1):
    root.after(i * 1000, decrement_label )

  root.after((i+1) * 1000, lambda : root.destroy())
  root.mainloop()


weight = 0
def changeNode(array_text):
	"""
	Snoozes for the given number of seconds. During the snooze, a progress
	dialog is launched notifying the 
	"""
	root = Tk()
	prompt = array_text
	array = tk.Label(root, text=prompt, width=len(prompt))
	array.pack()
			
	def update():	
		global weight
		text = "array is %d " % weight
		weight += 1
		array.config(text=text, width=100)
		array.update_idletasks()

	for i in range(100):
		root.after(i * 1000, update)
	
	root.mainloop()

		
def doStuff(method):
	root = tk.Tk()
	frame = tk.Frame(root)
	frame.pack()

	button = tk.Button(frame, text="QUIT", fg="red", command=quit)
	button.pack(side=tk.LEFT)
	slogan = tk.Button(frame, text="Main", command=method)
	slogan.pack(side=tk.LEFT)
	anotherOne = tk.Button(frame, text="Score", command=scoring.Scoring)
	anotherOne.pack(side=tk.LEFT)

	root.mainloop()