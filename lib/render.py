class Render():


	def __init__(self, pygame): #init-funksjon som kjører når klassen genereres
		self.pygame = pygame #gjør at vi kan bruke pygame i render.py


	def render_text(self, app, content, color, centered = False):
		#deler opp strengen content og splitter den hver gang det står "<br>"
		content_split = content.split("<br>")

		if centered == True: #stemmer hvis teksten er satt til å være midtstilt
			self.line0 = content_split[0] #innholdet på første linje

			#rendrer teksten først en gang for å finne linjehøyden
			self.text = app.font.render(self.line0, False, color)
			self.line_height = self.text.get_height()

			#finner så høyden på all teksten som skal vises
			self.text_height = self.line_height * len(content_split)

			#finner x- og y-verdien til første linje og viser den
			self.line_x = app.width / 2 - self.text.get_width() / 2
			self.line_y = app.height / 2 - (self.text_height / 2)
			app.display_surf.blit(self.text, (self.line_x, self.line_y))

			#for-løkke som går gjennom hver linje i content_split
			i = 0
			for line in content_split:

				#hopper over første runde i løkken ettersom første linje
				#allerede er rendret
				if i == 0:
					i += 1
					continue

				self.text = app.font.render(line, False, color)
				self.line_x = app.width / 2 - self.text.get_width() / 2
				self.line_y += self.line_height
				app.display_surf.blit(self.text, (self.line_x, self.line_y))
				i += 1

		else:
			self.line_x = 5
			self.line_y = 5
			for line in content_split:
				self.text = app.font.render(line, False, color)
				app.display_surf.blit(self.text, (self.line_x, self.line_y))
				self.line_y += self.text.get_height()

		self.pygame.display.flip()
