import pygame
from lib.render import *


text_on_screen = "Heisann<br>Hva gjør du nå?<br><br>Vi har det bra!" #tekst som skal vises på skjermen
colors = {
	"red": (255, 0, 0),
	"green": (0, 255, 0),
	"blue": (0, 0, 255)
}


class App(): #klassen til vinduet som spillet foregår i


	def __init__(self): #setter noen variabler når klassen lages
		self.running = True
		self.display_surf = None
		self.size = self.width, self.height = 640, 400 #skjermens bredde/høyde

		pygame.init() #initierer pygame slik at det kan brukes

		#lager en overflate hvor man kan rendre ting
		self.display_surf = pygame.display.set_mode(self.size)
		pygame.display.set_caption("Test")
		self.running = True #bool som sier om spillet skal kjøre eller ikke
		self.font = pygame.font.SysFont("arial", 16) #tekstens font

		#starter en klokke som teller oppover.
		#Brukes bl. a. for å definere framerate
		self.clock = pygame.time.Clock()


	def on_event(self, event): #metode som kjører hver gang et event skjer
		if event.type == pygame.QUIT: #avslutter hvis spillet krysses ut
			self.running = False
		elif event.type == pygame.KEYDOWN: #kjører hvis en knapp trykkes ned
			if event.key == pygame.K_ESCAPE: #avslutter spillet når esc trykkes
				self.running = False


	def on_loop(self): #metode som kjører hver frame
		self.clock.tick(30) #setter framerate til 30 fps
		#viser tekst på skjermen
		renderer.render_text(self, text_on_screen, colors["green"], True)


	def on_cleanup(self): #metode som kjører når programmet avsluttes
		pygame.quit()


	def on_execute(self): #metode som kjører når programmet starter
		#while-løkke som kjører så lenge self.running er True
		while self.running:
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
		self.on_cleanup()


if __name__ == "__main__":
	theApp = App()
	renderer = Render(pygame)
	theApp.on_execute()
