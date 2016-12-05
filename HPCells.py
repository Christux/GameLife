#!/usr/bin/env python
# -*- coding: utf8 -*-
# author	: Christux
# copyright	: Copyright 2015
# license	: GPL

from Cells import Cells

class HPCells(Cells):
	
	# Init cells grid	
	def __init__(self, width, height):
		Cells.__init__(self,width, height)
		self.count=[0]*self.ncells

	# Gets number of living cells
	def get_num_living(self):
		i=0
		count=0
		while i<self.ncells:
			count=count+self.table[i]
			i=i+1
		return count

	# Subroutine for counting
	def count_no_borders(self):
	# Avoid borders for better performances
		i=1
		while i<self.width-1:
			j=1
			while j<self.height-1:
				self.count[i*self.height+j]=self.table[(i-1)*self.height+j-1]+self.table[(i-1)*self.height+j]+\
					self.table[(i-1)*self.height+j+1]+self.table[i*self.height+j-1]+self.table[i*self.height+j+1]+\
					self.table[(i+1)*self.height+j-1]+self.table[(i+1)*self.height+j]+self.table[(i+1)*self.height+j+1]
				j=j+1
			i=i+1


	# Calculate new table
	def iteration(self):
		
		# Init counting table (usefull for UHPCells)
		self.count=[0]*self.ncells
		
		# Counts neighboring living cells
		self.count_no_borders()

		# First line without borders
		i=0
		j=1
		while j<self.height-1:
			self.count[i*self.height+j]=self.table[i*self.height+j-1]+self.table[i*self.height+j+1]+\
				self.table[(i+1)*self.height+j-1]+self.table[(i+1)*self.height+j]+self.table[(i+1)*self.height+j+1]
			j=j+1

		# Last line without borders
		i=self.width-1
		j=1
		while j<self.height-1:
			self.count[i*self.height+j]=self.table[i*self.height+j-1]+self.table[i*self.height+j+1]+\
				self.table[(i-1)*self.height+j-1]+self.table[(i-1)*self.height+j]+self.table[(i-1)*self.height+j+1]
			j=j+1

		# First column without borders
		i=1
		j=0
		while i<self.width-1:
			self.count[i*self.height+j]=self.table[(i-1)*self.height+j]+\
					self.table[(i-1)*self.height+j+1]+self.table[i*self.height+j+1]+\
					self.table[(i+1)*self.height+j]+self.table[(i+1)*self.height+j+1]
			i=i+1
		
		# Last column without borders
		i=1
		j=self.height-1
		while i<self.width-1:
			self.count[i*self.height+j]=self.table[(i-1)*self.height+j]+\
				self.table[(i-1)*self.height+j-1]+self.table[i*self.height+j-1]+\
				self.table[(i+1)*self.height+j]+self.table[(i+1)*self.height+j-1]
			i=i+1	

		# Corners
		# (0,0)
		self.count[0]=self.table[1]+self.table[self.height]+self.table[self.height+1]

		# (0,Y)
		self.count[self.height-1]=self.table[self.height-2]+self.table[2*self.height-2]+self.table[2*self.height-1]

		# (X,0)
		self.count[(self.width-1)*self.height]=self.table[(self.width-2)*self.height]+\
			self.table[(self.width-2)*self.height+1]+self.table[(self.width-1)*self.height+1]

		# (X,Y)
		self.count[(self.width-1)*self.height+self.height-1]=self.table[(self.width-2)*self.height+self.height-2]+\
			self.table[(self.width-2)*self.height+self.height-1]+self.table[(self.width-1)*self.height+self.height-2]

	
		# Construct new table with life game rules (http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
		i=0
		while i<self.ncells:
			
			state=self.table[i]
			ncells=self.count[i]
			
			if (state==0 and ncells==3):
				self.table[i]=1
				
			elif (state==1 and (ncells==2 or ncells==3)):
				self.table[i]=1
				
			elif (state==1):
				self.table[i]=0

			i=i+1
	
		

# Main function for tests	
if __name__ == '__main__':
	cells=HPCells(6,4)
	
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
	
	cells.iteration()
	cells.disp()
	
	cells.iteration()
	cells.disp()
	
	cells.iteration()
	cells.disp()
	
	cells.iteration()
	cells.disp()
	
	cells.iteration()
	cells.disp()
	
	cells.iteration()
	cells.disp()
	
	cells.iteration()
	cells.disp()