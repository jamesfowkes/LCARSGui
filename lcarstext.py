# #
# # LCARS GUI Objects Library : Text Object in "Star Trek" font
# #

import pygame

from lcarsobject import LCARSObject

font = "swiss911ultracompressed"

def getHeight(text, size):
	(w, h) = pygame.font.SysFont(font, size).size(text)
	return w
	
class TextAlign:
	XALIGN_CENTRE = 0
	XALIGN_LEFT = 1
	XALIGN_RIGHT = 2
	
class LCARSText(LCARSObject):

	def __init__(self, alignpoint, text, size, xalign, fg, bg, show):
	
		(x, y) = alignpoint
		
		self.font = pygame.font.SysFont(font, size)
		self.text = self.font.render(text, 1, fg, bg)
		
		# Define enclosing rectangle based on alignment point and align choice		
		top = y - (self.text.get_height() / 2)
		if (xalign == TextAlign.XALIGN_CENTRE):
			left = x - (self.text.get_width() / 2)
		elif (xalign == TextAlign.XALIGN_RIGHT):
			left = x - self.text.get_width()
		elif (xalign == TextAlign.XALIGN_LEFT):
			left = x
		
		rect = pygame.Rect(left, top, self.text.get_width(), self.text.get_height())
		
		LCARSObject.__init__(self, rect, fg, bg, show)
		
	def draw(self, window):
		window.blit(self.text, self.rect)
