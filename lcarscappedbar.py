##
## LCARS GUI Objects Library : Rectangular bar capped with semicircle(s)
##

from __future__ import division


import pygame


from LCARSGui import LCARSObject, LCARSText, TextAlign

class CapLocation:
	CAP_TOP = 1
	CAP_LEFT = 2
	CAP_RIGHT = 4
	CAP_BOTTOM = 8

class LCARSCappedBar(LCARSObject):

	def __init__(self, rect, caplocation, text, fg, bg, visible):
		LCARSObject.__init__(self, rect, fg, bg, visible)
		
		self.textString = text
		
		if len(text) > 0:
			if (self.rect.h > self.rect.w):
				#Portrait format
				texty = self.rect.bottom - self.rect.w
				textx = self.rect.right - (self.rect.w / 10)
				textw = self.PointSizeFromBarWidth()
			else:
				#Landscape
				texty = self.rect.centery
				textx = self.rect.right - (self.rect.h/2)
				textw = self.PointSizeFromBarHeight()
				
			self.text = LCARSText((textx, texty), text, textw, TextAlign.XALIGN_RIGHT, self.bg, self.fg, True) # Swap fg/bg text colours
		else:
			self.text = None
			
		self.caps = []
		if (caplocation & CapLocation.CAP_TOP):
			self.caps.append({'rect':pygame.Rect(0, 0, self.rect.w, self.rect.w), 'loc':CapLocation.CAP_TOP})
		if (caplocation & CapLocation.CAP_LEFT):
			self.caps.append({'rect':pygame.Rect(0, 0, self.rect.h, self.rect.h), 'loc':CapLocation.CAP_LEFT})
		if (caplocation & CapLocation.CAP_RIGHT):
			self.caps.append({'rect':pygame.Rect(self.rect.w - self.rect.h, 0, self.rect.h, self.rect.h), 'loc':CapLocation.CAP_RIGHT})
		if (caplocation & CapLocation.CAP_BOTTOM):
			self.caps.append({'rect':pygame.Rect(0, self.rect.h - self.rect.w, self.rect.w, self.rect.w), 'loc':CapLocation.CAP_BOTTOM})
			
	def PointSizeFromBarHeight(self):
		pointSizeAt50px = 24
		return int((self.rect.h / 50) * pointSizeAt50px)

	def PointSizeFromBarWidth(self):
		pointSizeAt50px = 24
		return int((self.rect.w / 50) * pointSizeAt50px)

	def setText(self, text):
		texty = self.rect.centery
		textx = self.rect.right - (self.rect.h/2)

		self.textString = text
		self.text = LCARSText((textx, texty), text, self.PointSizeFromBarHeight(), TextAlign.XALIGN_RIGHT, self.bg, self.fg, True) # Swap fg/bg text colours

	def getText(self):
		return self.textString
	
	def setWidth(self, newWidth):
	
		self.rect.width = newWidth
		# Make sure that text is correctly located
		self.setText(self.textString)
		
	def draw(self, window):
		
		if (self.visible):
			# Draw on a separate surface before blitting
			surf = pygame.Surface(self.rect.size)
				
			#Define the rectangle inside the endcaps			
			irect = self.rect.copy()
			irect.left = 0
			irect.top = 0
			
			# Draw each endcap
			for capDict in self.caps:
				cap = capDict['rect']
				loc = capDict['loc']
				# Remove rectangle enclosing cap before drawing
				if loc == CapLocation.CAP_RIGHT:
					irect.w -= cap.w/2
				if loc == CapLocation.CAP_LEFT:
					irect.w -= cap.w/2
					irect.left += cap.w/2
				if loc == CapLocation.CAP_BOTTOM:
					irect.h -= cap.w/2
				if loc == CapLocation.CAP_TOP:
					irect.h -= cap.w/2
					irect.top += cap.w/2
				
				# pygame doesn't do filled arcs well, so draw full circle
				pygame.draw.ellipse(surf, self.fg, cap, 0)

			surf.fill(self.fg, irect)
			surf.set_colorkey(self.bg)
			
			window.blit(surf, self.rect)
			
			# Draw text (if any)
			if not (self.text is None):
				self.text.draw(window)