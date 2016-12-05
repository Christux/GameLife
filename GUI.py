#!/usr/bin/env python
# -*- coding: utf8 -*-
# author		: Christux
# copyright	: Copyright 2015
# license	: GPL

# 
try:
	import Tkinter as tk
	import tkMessageBox as tkMsgBox
except:
	import tkinter as tk
	import tkinter.messagebox as tkMsgBox

import signal

class GUI(object):

	# Init GUI
	def __init__(self, width, height,grid_element_size):
		
		# Grid properties
		self.width=width
		self.height=height
		self.grid_element_size=grid_element_size
		self.count=0
		
		# Build
		self.build()
		
		# Catch end signals
		signal.signal(signal.SIGINT, self.stop)
		signal.signal(signal.SIGTERM, self.stop)
	
	# Stop properly	
	def stop(self,sign,no):
		self.root.quit()
	
	# Main loop
	def mainloop(self):
		self.root.mainloop()
	
	# Build GUI
	def build(self):
		self.root = tk.Tk()
		self.root.wm_title("Game of Life")

		# Menu
		menubar = tk.Menu(self.root)
		menu1 = tk.Menu(menubar, tearoff=0)
		menu1.add_command(label="Intro", command=self.set_intro)
		menu1.add_command(label="Copyright", command=self.set_copyright)
		menu1.add_separator()
		menu1.add_command(label="Play/Pause", command=self.pause)
		menu1.add_command(label="Reset", command=self.reset)
		menu1.add_separator()
		menu1.add_command(label="Quit", command=self.root.quit)
		menubar.add_cascade(label="Game of Life", menu=menu1)
		
		menu2 = tk.Menu(menubar, tearoff=0)
		menu2.add_command(label="Blinker", command=self.set_blinker)
		menu2.add_command(label="Toad", command=self.set_toad)
		menu2.add_command(label="Beacon", command=self.set_beacon)
		menu2.add_command(label="Cross", command=self.set_cross)
		menu2.add_command(label="Clock", command=self.set_clock)
		menu2.add_command(label="Clock 2", command=self.set_clock2)
		menu2.add_command(label="Galaxy of Kok", command=self.set_kok)
		menubar.add_cascade(label="Oscillors", menu=menu2)
		
		menu3 = tk.Menu(menubar, tearoff=0)
		menu3.add_command(label="Glider", command=self.set_glider)
		menu3.add_command(label="LWSS", command=self.set_LWSS)
		menu3.add_command(label="MWSS", command=self.set_MWSS)
		menu3.add_command(label="HWSS", command=self.set_HWSS)
		menubar.add_cascade(label="Ships", menu=menu3)
		
		menu4 = tk.Menu(menubar, tearoff=0)
		menu4.add_command(label="About", command=self.propo)
		menubar.add_cascade(label="Help", menu=menu4)
		
		self.root.config(menu=menubar)

		# Cannevas
		self.can=tk.Canvas(self.root,width=self.height*self.grid_element_size,
			height=self.width*self.grid_element_size,bg ='white')
		self.can.bind("<Button-1>",self.kik_left)
		self.can.bind("<Button-2>",self.kik_right)
		self.can.bind("<Double-Button-1>",self.kik_right)
		self.can.pack(side=tk.TOP,padx=5,pady=5)
		
		# Grid of cells
		self.cell_table=[]
		for i in range(self.width):
			for j in range(self.height):
				cell=self.can.create_rectangle(j*self.grid_element_size+1,i*self.grid_element_size+1,
					(j+1)*self.grid_element_size,(i+1)*self.grid_element_size,outline = "white" ,fill="white smoke")
				self.cell_table.append(cell)
		

		# Label use for output
		p = tk.PanedWindow(self.root)
		p.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH)
		
		self.comIter=tk.Label(p)
		self.comIter.pack(side=tk.LEFT)
		self.com=tk.Label(p)
		self.com.pack()
		
		# Buttons
		startButton=tk.Button(self.root,text="Quit",command = self.root.quit)
		pauseButton=tk.Button(self.root,text="Play/Pause",command = self.pause)
		resetButton=tk.Button(self.root,text="Reset",command = self.reset)
		startButton.pack(side=tk.RIGHT,padx=3,pady=3)
		pauseButton.pack(side=tk.LEFT, padx=3,pady=3)
		resetButton.pack(side=tk.BOTTOM,padx=3,pady=3)


	# Sets cell color
	def set_cell_color(self,i,j,color):
		self.can.itemconfigure(self.cell_table[i*self.height+j],fill=color)
	
	# Gets coordinate
	def get_coord(self,event):
		coord=[0,0]
		if event.x >= self.grid_element_size*self.height :
			event.x = self.grid_element_size*self.height -1
		if event.y >= self.grid_element_size*self.width :
			event.y = self.grid_element_size*self.width -1
		coord[1]=(int(event.x /self.grid_element_size) % self.height)
		coord[0]=(int(event.y /self.grid_element_size) % self.width)
		return coord
		
	# Kik actions
	def kik_left(self,event):
		coord=self.get_coord(event)
		self.com.configure(text="("+str(coord[0])+","+str(coord[1])+")")
		self.set_cell_color(coord[0],coord[1],"pale green")
		self.count=self.count+1
		self.comIter.configure(text="Iteration: "+str(self.count))
		
	def kik_right(self,event):
		coord=self.get_coord(event)
		self.com.configure(text="("+str(coord[0])+","+str(coord[1])+")")
		self.set_cell_color(coord[0],coord[1],"light coral")
	
	# Edit menu
	def set_intro(self):
		self.com.configure(text="Intro")
		
	def set_copyright(self):
		self.com.configure(text="Copyright")
	
	def pause(self):
		self.com.configure(text="Pause")
		
	def reset(self):
		self.com.configure(text="Reset")
		
	# Help menu
	def propo(self):
		tkMsgBox.showinfo(title="About", message="Game of Life\n\nCopyleft Christux 2015",icon="info")
		
	# Oscillator menu
	def set_blinker(self):
		self.com.configure(text="Blinker")
		
	def set_toad(self):
		self.com.configure(text="Toad")
		
	def set_beacon(self):
		self.com.configure(text="Beacon")
		
	def set_cross(self):
		self.com.configure(text="Cross")
		
	def set_clock(self):
		self.com.configure(text="Clock")
		
	def set_clock2(self):
		self.com.configure(text="Clock 2")
		
	def set_kok(self):
		self.com.configure(text="Galaxy of Kok")
		
	# Starship menu
	def set_glider(self):
		self.com.configure(text="Glider")
		
	def set_LWSS(self):
		self.com.configure(text="LWSS")
		
	def set_MWSS(self):
		self.com.configure(text="MWSS")
		
	def set_HWSS(self):
		self.com.configure(text="HWSS")
		
# Main function for tests	
if __name__ == '__main__':
	gui=GUI(8,12,50)
	
	# Disp cell
	for i in range(gui.width):
		for j in range(gui.height):
			if (i%2 == j%2):
				color="black"
			else:
				color="#e6c66f"
			#gui.set_cell_color(i,j,color)
	
	gui.mainloop()