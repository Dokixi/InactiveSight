import pygame
from pygame.locals import *


text_on_screen = "Lorem ipsum"


class App():


	def __init__(self):
		self.running = True
		self.display_surf = None
		self.size = self.width, self.height = 640, 400


	def on_init(self):
		pygame.init()
		self.display_surf = pygame.display.set_mode(self.size)
		self.running = True
		self.font = pygame.font.SysFont("comicsansms", 16)


	def on_event(self, event):
		if event.type == pygame.QUIT:
			self.running = False


	def on_loop(self):
		pass


	def on_render(self, content, centered = False):
		self.text = self.font.render(content, False, (0, 255, 0))

		if centered == True:
			self.text_x = self.width // 2 - self.text.get_width() // 2
			self.text_y = self.height // 2 - self.text.get_height() // 2
		else:
			self.text_x = 5
			self.text_y = 5
		
		self.display_surf.blit(self.text, (self.text_x, self.text_y))
		pygame.display.flip()


	def on_cleanup(self):
		pygame.quit()


	def on_execute(self):
		if self.on_init() == False:
			self.running = False

		while self.running:
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render(text_on_screen)
		self.on_cleanup()


if __name__ == "__main__":
	theApp = App()
	theApp.on_execute()