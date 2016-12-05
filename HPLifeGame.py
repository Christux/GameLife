#!/usr/bin/env python
# -*- coding: utf8 -*-
# author	: Christux
# copyright	: Copyright 2015
# license	: GPL

import time
from GUI import GUI
from LifeGame import life_game
from HPCells import HPCells

class HPlife_game(life_game):

	# Init GUI
	def __init__(self,width,height,grid_element_size,time_step):
		
		# Init GUI
		GUI.__init__(self,width, height,grid_element_size)
		
		self.cells=HPCells(width,height)
		self.state=0
		self.oldstate=0
		self.old_cell_state=[0]*self.cells.ncells
		self.count=0
		self.skipframe=1
		self.time_step=time_step
		
		# After build
		self.set_intro()
		self.update_grid()
		# Call the update() function after time step
		self.timer=self.root.after(self.time_step, self.update)
		
	# Updates all grid of cells
	def update_grid(self):
		i=0
		while i<self.width:
			j=0
			while j<self.height:
				
				# Updates cell only if changes
				if self.cells.table[i*self.height+j]!=self.old_cell_state[i*self.height+j]:
					self.update_cell(i,j)
				j=j+1
			i=i+1
		#self.can.update_idletasks()
		
		# Update old table
		k=0
		while k<self.cells.ncells:
			self.old_cell_state[k]=self.cells.table[k]
			k=k+1

	
	# Updates a cell
	def update_cell(self,i,j):
		
		color="white smoke"
		if self.cells.table[i*self.height+j]==1:
			color="dark green"
			
		self.set_cell_color(i,j,color)
	
	# Kik actions
	def kik_left(self,event):
		coord=self.get_coord(event)
		i=coord[0]
		j=coord[1]
		self.cells.born_cell(i,j)
		self.update_cell(i,j)
		self.old_cell_state[i*self.height+j]=1
		
	def kik_right(self,event):
		coord=self.get_coord(event)
		i=coord[0]
		j=coord[1]
		self.cells.kill_cell(i,j)
		self.update_cell(i,j)
		self.old_cell_state[i*self.height+j]=0

	# Update game in accordance with pause parameter
	def update(self):
		
		# Update message
		if self.state==0 and self.oldstate==1:
			self.com.configure(text="Game in progress")
		elif self.state==1 and self.oldstate==0:
			self.com.configure(text="Game in pause")

		# Update game
		if self.state==0:
			
			# Pause game if no more living cells
			#if self.cells.get_num_living()==0:
			#	self.pause()
			
			# Compute next iteration and update GUI
			i=0
			while i<self.skipframe:
				self.cells.iteration()
				i=i+1
			self.count=self.count+self.skipframe
		
		self.update_grid()
		self.comIter.configure(text="Iteration: "+str(self.count).zfill(4))
		self.comIter.update()
	
		# Call the update() function after time step
		self.timer=self.root.after(self.time_step, self.update)
			
	# Edit menu
	def pause(self):
		self.oldstate=self.state
		self.state = 1 - self.state
					
# Main function
if __name__ == '__main__':
	#HPlife_game(14,16,40,200).mainloop()
	
	
	lg=HPlife_game(100,180,6,50)
	lg.pause()
	lg.clear()

	# Build pentomino 5 Mathusalem
	lg.cells.create_vline(60,100,3)
	lg.cells.born_cell(62,99)
	lg.cells.born_cell(61,101)
	
	lg.update_grid()
	lg.mainloop()
	