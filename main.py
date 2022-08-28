from ursina import *
import random as r

app = Ursina(title= 'Visual')

window.fullscreen = True
window.color = color.black
mouse.visible = False
counter = Text( text=' ', 
				y=.25, z=-1, 
				scale=1, 
				origin=(-.4,-.4), 
				background=False,
				visible=False)

window.exit_button.enabled = False
window.fps_counter.enabled = False

count = 0
cooldown = False

def place_cube(value=1, interval=0.2):
	global count
	count += 1
	counter.text = str(count) + " Spheres :)"
	#counter.color = color.random_color()
	e = Sprite( color = color.random_color(), 
			   	x = r.randint(-80,80),
			   	y = r.randint(-80,80),
			   	z = r.randint(200,205),
			   	texture = 'windows_icon2',
			   	scale = .3,
			   	ignore = True,)
	e.animate_z(-10, loop=True, delay=.2, duration=2,)
	if count < 200:
		invoke(place_cube, value, delay=interval)

place_cube()

EditorCamera()
app.run()