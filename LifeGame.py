#!/usr/bin/env python
# -*- coding: utf8 -*-
# author		: Christux
# copyright	: Copyright 2015
# license	: GPL

import time
import signal
from GUI import GUI
from Cells import Cells


class life_game(GUI):

	# Init GUI
	def __init__(self,width,height,grid_element_size,time_step):
		
		# Init GUI
		GUI.__init__(self,width, height,grid_element_size)
		#super(self.__class__,self).__init__(width, height,grid_element_size)
		
		self.cells=Cells(width,height)
		self.state=0
		self.time_step=time_step
		
		# After build
		self.set_intro()
		self.update_grid()
		# Call the update() function after time step
		self.timer=self.root.after(self.time_step, self.update)
		#self.update()

	
	# Updates a cell
	def update_cell(self,i,j):
		
		color="white smoke"
		if self.cells.state_cell(i,j)==1:
			color="dark green"
			
		self.set_cell_color(i,j,color)
	
	# Updates all grid of cells
	def update_grid(self):
		for i in range(self.width):
			for j in range(self.height):
				self.update_cell(i,j)
	
	# Update game in accordance with pause parameter
	def update(self):
		
		# Update message
		if self.state==0:
			self.com.configure(text="Game in progress")
		else:
			self.com.configure(text="Game in pause")
	
		self.comIter.configure(text="Iteration: "+str(self.count).zfill(4))
	
		# Update game
		if self.state==0:
			
			# Pause game if no more living cells
			if self.cells.get_num_living()==0:
				self.pause()
			
			# Compute next iteration and update GUI
			self.cells.iteration()
			self.count=self.count+1
			#self.cells.finalize_iteration()
			self.update_grid()
			
	
		# Call the update() function after time step
		self.timer=self.root.after(self.time_step, self.update)
		
	# Kik actions
	def kik_left(self,event):
		coord=self.get_coord(event)
		self.cells.born_cell(coord[0],coord[1])
		self.update_cell(coord[0],coord[1])
		
	def kik_right(self,event):
		coord=self.get_coord(event)
		self.cells.kill_cell(coord[0],coord[1])
		self.update_cell(coord[0],coord[1])
	
	# Edit menu
	def set_intro(self):
		self.clear()
		self.cells.create_glider(0,1)
		self.cells.create_blinker(7,1)
		self.cells.create_beacon(2,10)
		self.update_grid()
	
	def set_copyright(self):
		self.clear()
		self.cells.create_copyright(2,0)
		self.update_grid()
		if self.state==0:
			self.pause()
		
	def pause(self):
		self.state = 1 - self.state
	
	def reset(self):
		self.clear()
		self.count=0
		self.update_grid()
		self.pause()
	
	def clear(self):
		self.cells.cells_clear()
		self.count=0
		
	# Oscillators menu
	def set_blinker(self):
		self.clear()
		self.cells.create_blinker(0,1)
		self.update_grid()
	
	def set_toad(self):
		self.clear()
		self.cells.create_toad(0,1)
		self.update_grid()
	
	def set_beacon(self):
		self.clear()
		self.cells.create_beacon(0,0)
		self.update_grid()
		
	def set_cross(self):
		self.clear()
		self.cells.create_cross(1,1)
		self.update_grid()
		
	def set_clock(self):
		self.clear()
		self.cells.create_clock(0,0)
		self.update_grid()
		
	def set_clock2(self):
		self.clear()
		self.cells.create_clock2(0,0)
		self.update_grid()
		
	def set_kok(self):
		self.clear()
		self.cells.create_kok(0,0)
		self.update_grid()
	
	# Starchips menu
	def set_glider(self):
		self.clear()
		self.cells.create_glider(0,0)
		self.update_grid()
		
	def set_LWSS(self):
		self.clear()
		self.cells.create_LWSS(2,0)
		self.update_grid()
	
	def set_MWSS(self):
		self.clear()
		self.cells.create_MWSS(2,0)
		self.update_grid()
		
	def set_HWSS(self):
		self.clear()
		self.cells.create_HWSS(1,0)
		self.update_grid()
		
# Main function
if __name__ == '__main__':
	life_game(14,16,40,200).mainloop()