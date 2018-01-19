import pygame
from pygame.locals import *
from lib.render import *


text_on_screen = """
	Velkommen til Romskjekk på SKAP! \n
	Dette spillet går ut på at du skal huske oppgavene på romsjekk, \n
	og ikke minst gjøre dem.\n\n

	Hvis du ikke greier å gjøre alle oppgavene før romsjekken klokken 15:00\n
	taper du spillet og kan ikke fortsette...\n\n

	Lykke til!
""" #tekst som skal vises på skjermen


class App(): #klassen til vinduet som spillet foregår i


	def __init__(self): #setter noen variabler når klassen lages
		self.running = True
		self.display_surf = None
		self.size = self.width, self.height = 640, 400 #skjermens bredde/høyde

		pygame.init()
		self.display_surf = pygame.display.set_mode(self.size)
		pygame.display.set_caption("Test")
		self.running = True
		self.font = pygame.font.SysFont("arial", 16)
		self.clock = pygame.time.Clock()


	def on_event(self, event):
		if event.type == pygame.QUIT:
			self.running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				self.running = False


	def on_loop(self):
		self.clock.tick(30)
		renderer.render_text(self, text_on_screen, True)


	def on_cleanup(self):
		pygame.quit()


	def on_execute(self):
		while self.running:
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
		self.on_cleanup()


if __name__ == "__main__":
	theApp = App()
	renderer = Render(pygame)
	theApp.on_execute()