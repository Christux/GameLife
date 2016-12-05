#!/usr/bin/env python
# -*- coding: utf8 -*-
# author		: Christux
# copyright	: Copyright 2015
# license	: GPL

class Cells():
	
	# Init cells grid	
	def __init__(self, width, height):
		self.width=width
		self.height=height
		self.ncells=self.width*self.height
		self.table=[0]*self.width*self.height
	
	# Gets number of living cells
	def get_num_living(self):
		count=0
		for i in range(self.width*self.height):
			count=count+self.table[i]
		return count
	
	# Kills cell	
	def kill_cell(self,i,j):
		self.table[i*self.height+j]=0
	
	# Creates new cell	
	def born_cell(self,i,j):
		self.table[i*self.height+j]=1
	
	# Checks cell state
	def state_cell(self,i,j):
		return self.table[i*self.height+j]
	
	# Checks cell state with index out of range support
	def state_cell_protected(self,i,j):
		if i<0 or j< 0 or i>=self.width or j>=self.height:
			return 0
		else:
			return self.state_cell(i,j)
	
	# Counts neighboring living cells
	def count_neighboring_living_cells(self,i,j):
		count=0
				
		# Loop on neighboring cells
		for m in range(3):
			for n in range(3):
				count=count+self.state_cell_protected(i+m-1,j+n-1)
				
		# Substracts self cell
		count=count-self.state_cell(i,j)
		
		return count
	
	# Calculate new table
	def iteration(self):
		nextable=[0]*self.width*self.height
		
		# Loop on cells
		for i in range(self.width):
			for j in range(self.height):
				count=self.count_neighboring_living_cells(i,j)
				
				#nextable[i*self.height+j]=count
				
				# Construct new table with life game rules (http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
				if (self.state_cell(i,j)==0 and count==3):
					nextable[i*self.height+j]=1
				
				if (self.state_cell(i,j)==1 and (count==2 or count==3)):
					nextable[i*self.height+j]=1

		
		# Replace table with new one
		self.table=nextable
			
	# Prints cell table	
	def disp(self):
		for i in range(self.width):
			line=""
			for j in range(self.height):
				if self.state_cell(i,j)==0:
					char="·" # alt+shit+f
				else:
					char="#"
				
				line=line+char+" "
			print(line)
		print("")
	
	# Clear table	
	def cells_clear(self):
		self.table=[0]*self.width*self.height
	
	# Horizontal line
	def create_hline(self,i,j,size):
		if i<self.width and j+size-1<self.height:
			for k in range(size):
				self.born_cell(i,j+k)
	
	# Vertical line
	def create_vline(self,i,j,size):
		if i+size-1<self.width and j<self.height:
			for k in range(size):
				self.born_cell(i+k,j)
	
	# Block
	def create_block(self,i,j):
		if i+1<self.width and j+1<self.height:
			self.create_hline(i,j,2)
			self.create_hline(i+1,j,2)	
		
	# Blinker oscillator
	def create_blinker(self,i,j):
		if i+2<self.width and j<self.height:
			self.create_vline(i,j,3)
	
	# Toad oscillator
	def create_toad(self,i,j):
		if i+3<self.width and j+1<self.height:
			self.create_vline(i+1,j,3)
			self.create_vline(i,j+1,3)
	
	# Beacon oscillator	
	def create_beacon(self,i,j):
		if i+3<self.width and j+3<self.height:
			self.create_block(i,j)
			self.create_block(i+2,j+2)
	
	# Cross oscillator
	def create_cross(self,i,j):
		if i+7<self.width and j+7<self.height:
			self.create_hline(i,j+2,4)
			self.create_hline(i+2,j,3)
			self.create_hline(i+2,j+5,3)
			self.create_hline(i+5,j,3)
			self.create_hline(i+5,j+5,3)
			self.create_hline(i+7,j+2,4)
			self.create_vline(i+3,j,2)
			self.create_vline(i+3,j+7,2)
			self.born_cell(i+1,j+2)
			self.born_cell(i+1,j+5)
			self.born_cell(i+6,j+2)
			self.born_cell(i+6,j+5)
	
	# Clock oscillator
	def create_base_clock(self,i,j):
		self.create_block(i,j+6)
		self.create_block(i+4,j)
		self.create_block(i+10,j+4)
		self.create_block(i+6,j+10)
		self.create_hline(i+3,j+4,4)
		self.create_hline(i+8,j+4,4)
		self.create_vline(i+4,j+3,4)
		self.create_vline(i+4,j+8,4)
			
	def create_clock(self,i,j):
		if i+11<self.width and j+11<self.height:
			self.create_base_clock(i,j)
			self.create_hline(i+5,j+5,2)
			self.born_cell(i+6,j+7)
			
	def create_clock2(self,i,j):
		if i+11<self.width and j+11<self.height:
			self.create_base_clock(i,j)
			self.born_cell(i+5,j+6)
			self.born_cell(i+6,j+7)
			self.born_cell(i+7,j+5)
			
	# Kok galaxy
	def create_kok(self,i,j):
		if i+12<self.width and j+12<self.height:
			self.create_vline(i+2,j+2,6)
			self.create_vline(i+2,j+3,6)
			self.create_vline(i+5,j+9,6)
			self.create_vline(i+5,j+10,6)
			self.create_hline(i+2,j+5,6)
			self.create_hline(i+3,j+5,6)
			self.create_hline(i+9,j+2,6)
			self.create_hline(i+10,j+2,6)
	
	# Glider spaceship
	def create_glider(self,i,j):
		if i+2<self.width and j+2<self.height:
			self.born_cell(i,j+1)
			self.born_cell(i+1,j+2)
			self.create_hline(i+2,j,3)
			
	# LWSS spaceship
	def create_LWSS(self,i,j):
		if i+3<self.width and j+4<self.height:
			self.create_hline(i+3,j+1,4)
			self.create_vline(i+1,j+4,2)
			self.born_cell(i,j)
			self.born_cell(i+2,j)
			self.born_cell(i,j+3)
			
	# LWSS spaceship
	def create_MWSS(self,i,j):
		if i+4<self.width and j+5<self.height:
			self.create_hline(i+4,j+1,5)
			self.create_vline(i+2,j+5,2)
			self.born_cell(i+1,j)
			self.born_cell(i+3,j)
			self.born_cell(i+1,j+4)
			self.born_cell(i,j+2)		
	
	# HWSS spaceship
	def create_HWSS(self,i,j):
		if i+4<self.width and j+6<self.height:
			self.create_hline(i+4,j+1,6)
			self.create_vline(i+2,j+6,2)
			self.born_cell(i+1,j)
			self.born_cell(i+3,j)
			self.born_cell(i+1,j+5)
			self.create_hline(i,j+2,2)	
	
	# Copyright
	def create_copyright(self,i,j):
		if i+8<self.width and j+14<self.height:
			# C
			self.create_vline(i,j,4)
			self.born_cell(i,j+1)
			self.born_cell(i+3,j+1)
			# H
			self.create_vline(i,j+3,4)
			self.create_vline(i,j+5,4)
			self.born_cell(i+2,j+4)
			# R
			self.create_vline(i,j+7,4)
			self.create_vline(i,j+9,2)
			self.born_cell(i,j+8)
			self.born_cell(i+2,j+8)
			self.born_cell(i+3,j+9)
			# I
			self.create_vline(i,j+11,4)
			# S
			self.create_block(i,j+13)
			self.create_hline(i+3,j+13,3)
			self.born_cell(i,j+15)
			self.born_cell(i+2,j+15)
			# T
			self.create_vline(i+6,j+3,4)
			self.create_hline(i+6,j+2,3)
			# U
			self.create_vline(i+6,j+6,4)
			self.create_vline(i+6,j+8,4)
			self.born_cell(i+9,j+7)
			# X
			self.create_block(i+7,j+11)
			self.born_cell(i+6,j+10)
			self.born_cell(i+6,j+13)
			self.born_cell(i+9,j+10)
			self.born_cell(i+9,j+13)
			
			
# Main function for tests	
if __name__ == '__main__':
	cells=Cells(6,4)
	cells.disp()
	
	# V line
	print("Vertical line:")
	cells.create_vline(0,2,6)
	cells.disp()
	
	# H line
	cells.cells_clear()
	print("Horizontal line:")
	cells.create_hline(3,1,3)
	cells.disp()
	
	# Block
	print("Block:")
	cells.cells_clear()
	cells.create_block(3,1)
	cells.disp()
	print("There are "+str(cells.get_num_living())+" living cells")
	
	cells.iteration()
	cells.disp()
	
	# Blinker oscillator
	print("Blinker oscillator:")
	cells.cells_clear()
	cells.create_blinker(1,2)
	cells.disp()
	
	cells.iteration()
	cells.disp()
	
	cells.iteration()
	cells.disp()
	
	# Toad oscillator
	print("Toad oscillator:")
	cells.cells_clear()
	cells.create_toad(1,1)
	cells.disp()
	
	cells.iteration()
	cells.disp()
	
	cells.iteration()
	cells.disp()
	
	# Beacon oscillator
	print("Beacon oscillator:")
	cells.cells_clear()
	cells.create_beacon(1,0)
	cells.disp()
	
	cells.iteration()
	cells.disp()
	
	cells.iteration()
	cells.disp()
	
	# Glider spaceship
	print("Glider spaceship:")
	cells.cells_clear()
	cells.create_glider(1,0)
	cells.disp()
	
	cells.iteration()
	cells.disp()
	
	cells.iteration()
	cells.disp()
	
	cells.iteration()
	cells.disp()
	
	cells.iteration()
	cells.disp()
	
	# Cross oscillator
	print("Cross oscillator:")
	cells=Cells(8,8)
	cells.create_cross(0,0)
	cells.disp()
	
	# Clock oscillator
	print("Clock oscillator:")
	cells=Cells(12,12)
	cells.create_clock(0,0)
	cells.disp()
	
	print("Clock oscillator 2:")
	cells.cells_clear()
	cells.create_clock2(0,0)
	cells.disp()

	# Kok galaxy
	print("Kok galaxy:")
	cells=Cells(13,13)
	cells.create_kok(0,0)
	cells.disp()

	# LWSS spaceship
	print("LWSS spaceship:")
	cells=Cells(8,8)
	cells.create_LWSS(1,1)
	cells.disp()

	# MWSS spaceship
	print("MWSS spaceship:")
	cells.cells_clear()
	cells.create_MWSS(1,1)
	cells.disp()
	
	# MWSS spaceship
	print("HWSS spaceship:")
	cells.cells_clear()
	cells.create_HWSS(1,1)
	cells.disp()
	
	# Copyright
	print("Copyright:")
	cells=Cells(10,18)
	cells.create_copyright(0,0)
	cells.disp()