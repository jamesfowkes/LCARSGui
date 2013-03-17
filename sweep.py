##
## LCARS GUI Objects Library : "Sweep" with corner at top-left
##

from __future__ import division

import pygame

from LCARSGui import LCARSObject
import math

class LCARSSweep(LCARSObject):

	def __init__(self, rect, corner, xthick, ythick, fg, bg, show):
	
		LCARSObject.__init__(self, rect, fg, bg, show)
		
		minl = min(xthick, ythick)
		ycorrection = ythick - (minl * 2/3)
		xcorrection = xthick + (minl * 2/3)
		
		self.yrect = pygame.Rect(self.rect.left, self.rect.top + ycorrection, xthick, self.rect.h - ycorrection)
		self.xrect = pygame.Rect(self.rect.left + xcorrection, self.rect.top, self.rect.w - xcorrection, ythick)
		
		self.outersweepdraw = pygame.Rect(self.rect.left, self.rect.top, minl * 3, minl * 3)
		self.outersweepmask = pygame.Rect(self.rect.left + xthick, self.rect.top + ythick, minl * 3, minl * 3)
		self.innersweepdraw = pygame.Rect(self.rect.left + xthick, self.rect.top + ythick, minl, minl)
		self.innersweepmask = pygame.Rect(self.rect.left + xthick, self.rect.top + ythick, minl * 2, minl * 2)
	
	def collidepoint(self, pos):
		collide = self.yrect.collidepoint(pos)
		collide = collide or self.xrect.collidepoint(pos) 
		collide = collide or (self.pointInsideEllipse(self.outersweepdraw, pos) and (not self.outersweepmask.collidepoint(pos)))
		collide = collide or ((not self.pointInsideEllipse(self.innersweepmask, pos)) and (self.innersweepdraw.collidepoint(pos)))
		return collide
	
	def pointInsideEllipse(self, rect, pos):
		## No point testing for inside circle
		## if outside enclosing rect
		collide = False
		if rect.collidepoint(pos):
			x, y = pos
			x = x - rect.centerx
			y = y - rect.centery
			
			rx = rect.w / 2
			ry = rect.h / 2
			
			rxx = rx*rx
			ryy = ry * ry
			xx = x*x
			yy = y*y
			
			res = (xx/rxx) + (yy/ryy)
			
			collide = res <	 1
		
		return collide
		
	def l(self):
		return self.xrect.left
		
	def draw(self, window):
	
		# Vertical and horizontal bars
		pygame.draw.rect(window, self.fg, self.yrect, 0)
		pygame.draw.rect(window, self.fg, self.xrect, 0)
		
		#Sweep - big ellipse (foreground) and rectangle (background)
		pygame.draw.ellipse(window, self.fg, self.outersweepdraw, 0)
		pygame.draw.rect(window, self.bg, self.outersweepmask, 0)
		
		#Sweep - small ellipse (background) and rectangle (foreground)
		pygame.draw.rect(window, self.fg, self.innersweepdraw, 0)
		pygame.draw.ellipse(window, self.bg, self.innersweepmask, 0)
