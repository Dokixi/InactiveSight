class Render():


	def __init__(self, pygame):
		self.pygame = pygame


	def render_text(self, app, content, centered = False):
			self.text = app.font.render(content, False, (0, 255, 0))

			if centered == True:
				self.text_x = self.width // 2 - self.text.get_width() // 2
				self.text_y = self.height // 2 - self.text.get_height() // 2
			else:
				self.text_x = 5
				self.text_y = 5
			
			app.display_surf.blit(self.text, (self.text_x, self.text_y))
			self.pygame.display.flip()