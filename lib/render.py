class Render():


	def __init__(self, pygame):
		self.pygame = pygame
		self.test_var = 0


	def render_text(self, app, content, centered = False):

			content_split = content.split("<br>")
			if self.test_var == 0:
				print(content_split)
				self.test_var = 1

			if centered == True:
				#innholdet på første linje
				self.line0 = content_split[0]

				#rendrer teksten først en gang for å finne linjehøyden
				self.text = app.font.render(self.line0, False, (0, 255, 0))
				self.line_height = self.text.get_height()

				#finner så høyden på all teksten som skal vises
				self.text_height = self.line_height * len(content_split)

				#finner x- og y-verdien til første linje og viser den
				self.line_x = app.width / 2 - self.text.get_width() / 2
				self.line_y = app.height / 2 - (self.text_height / 2)
				app.display_surf.blit(self.text, (self.line_x, self.line_y))

				#self.text_y = app.height / 2 - self.text.get_height() / 2

				#løkke som går gjennom hver linje
				i = 0
				for line in content_split:
					if i == 0:
						i += 1
						continue
					self.text = app.font.render(line, False, (0, 255, 0))
					self.line_x = app.width / 2 - self.text.get_width() / 2
					self.line_y += self.line_height
					app.display_surf.blit(self.text, (self.line_x, self.line_y))
					i += 1


			else:
				self.line_x = 5
				self.line_y = 5
				for line in content_split:
					self.text = app.font.render(line, False, (0, 255, 0))
					app.display_surf.blit(self.text, (self.line_x, self.line_y))
					self.line_y += self.text.get_height()
			
			self.pygame.display.flip()