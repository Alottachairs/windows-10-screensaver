from ursina import *
import random as r

app = Ursina(title= 'Visual')

window.fullscreen = True
window.color = color.black
mouse.visible = False
window.exit_button.enabled = False
window.fps_counter.enabled = False
#counter = Text( text=' ', 
#				y=.25, z=-1, 
#				scale=1, 
#				origin=(-.4,-.4), 
#				background=False,
#				visible=False)

count = 0
limit = 200

def place_cube(value=.1, interval=0.15):
	global limit
	global count
	count += 1
	#counter.text = str(count) + " Entitys"
	#counter.color = color.random_color()
	e = Sprite( model = 'quad',
				color = color.random_color(), 
			   	x = r.randint(-80,80),
			   	y = r.randint(-80,80),
			   	z = r.randint(300,305),
			   	texture = 'windows_icon2',
			   	scale = .5,
			   	ignore = True,)
	e.animate_z(-10, loop=True, delay=.1, duration=2,)
	if count < limit:
		invoke(place_cube, value, delay=interval,)
		destroy(e, delay=4)
		count -= 1

place_cube()

def input(key):
	if key:
		application.quit()

#EditorCamera()
app.run()