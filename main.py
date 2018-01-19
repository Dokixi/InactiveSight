import pygame
from pygame.locals import *
from lib.render import *


text_on_screen = "Hello world" #tekst som skal vises på skjermen


class App(): #klassen til vinduet som spillet foregår i


	def __init__(self): #setter noen variabler når klassen lages
		self.running = True
		self.display_surf = None
		self.size = self.width, self.height = 640, 400 #skjermens bredde/høyde

		pygame.init()
		self.display_surf = pygame.display.set_mode(self.size)
		pygame.display.set_caption("Test")
		self.running = True
		self.font = pygame.font.SysFont("comicsansms", 16)


	def on_event(self, event):
		if event.type == pygame.QUIT:
			self.running = False
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			self.running = False


	def on_loop(self):
		pass		


	def on_cleanup(self):
		pygame.quit()


	def on_execute(self):
		while self.running:
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			renderer.render_text(self, text_on_screen, False)
		self.on_cleanup()


if __name__ == "__main__":
	theApp = App()
	renderer = Render(pygame)
	theApp.on_execute()