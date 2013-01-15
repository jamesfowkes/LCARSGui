##
## LCARS GUI Objects Library : Simple Rectangle Object with text
##

import pygame

from lcarstext import LCARSText

class LCARSRect(LCARSText):

	def __init__(self, rect, text, size, xalign, fg, bg):
		SSText.__init__(self, rect, text, size, xalign, fg, bg):
		
	def draw(self, window):
		pygame.draw.rect(window, SS_FG, self.rect, 0)
		