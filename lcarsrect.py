##
## LCARS GUI Objects Library : Simple Rectangle Object with text
##

import pygame

from lcarstext import LCARSText

class LCARSRect(LCARSText):

	def __init__(self, rect, text, size, xalign, fg, bg):
		
#		self, alignpoint, text, size, xalign, fg, bg, show):
		
		self.LCARSText.__init__(self, rect, text, size, xalign, fg, bg, True)
		
	def draw(self, window):
		pygame.draw.rect(window, SS_FG, self.rect, 0)
		