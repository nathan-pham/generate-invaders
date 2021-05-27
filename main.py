import PIL as pillow
import random
from PIL import Image, ImageDraw

r = lambda: random.randint(50, 215)
gen_color = lambda: (r(), r(), r())

s_list = []

def create_pixel(border, draw, rand_color, element, size):
	if(element == int(size / 2)):
		draw.rectangle(border, rand_color)
	elif(len(s_list) == element + 1):
		draw.rectangle(border, s_list.pop())
	else:
		s_list.append(rand_color)
		draw.rectangle(border, rand_color)

def create_invader(border, draw, size):
	x0, y0, x1, y1 = border
	square_size = (x1 - x0) / size
	rand_colors = [gen_color(), gen_color(), gen_color(), (0, 0, 0), (0, 0 ,0), (0, 0, 0)]

	i = 1
	for y in range(0, size):
		i *= -1
		element = 0
		for x in range(0, size): 
			left_x = x * square_size + x0
			left_y = y * square_size + y0
			right_x = left_x + square_size
			right_y = left_y + square_size
			
			create_pixel((left_x, left_y, right_x, right_y), draw, random.choice(rand_colors), element, size)
			if(element == int(size / 2) or element == 0):
				i *= -1
			element += i

def main(size, invaders, image_size):
	dimensions = image_size
	image = Image.new('RGB', (dimensions, dimensions))
	draw = ImageDraw.Draw(image)

	invader_size = dimensions/invaders
	padding = invader_size/size
	for x in range(0, invaders):
		for y in range(0, invaders):
			left_x = x * invader_size + padding / 2
			left_y = y * invader_size + padding / 2
			right_x = left_x + invader_size - padding
			right_y = left_y + invader_size - padding
			create_invader((left_x, left_y, right_x, right_y), draw, size)
	
	image.save('sprites' + str(size) + 'x' + str(invaders) + '-' + str(dimensions) + '.png')

main(15, 1, 512)
