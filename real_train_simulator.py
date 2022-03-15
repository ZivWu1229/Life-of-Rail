from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from json import load
import tkinter as tk

scenes = []
loco_datas = []
settings = []

class Rail(Mesh):
	def __init__():
		pass

app = Ursina()

def input(key):
	global pause_menu
	if key == 'shift':
		player.speed = player.speed * 10
	elif key == 'shift up':
		player.speed = player.speed / 10
	if key == 'r':
		player.position = (0,0,0)
	if key == 'escape':
		pause_menu = Button(text='continue',ignore_paused=True)
		pause_menu.on_click = uppaused()
		application.paused = True
		mouse.visible = True
		mouse.locked = False

def uppaused():
	if application.paused:
		application.paused = False
		mouse.visible = False
		mouse.locked = True
		destroy(pause_menu)

floor = Entity(parent=scene,model='plane',collision = True,collider = 'plane',scale_x=100,scale_z=100,texture='heightmap_1')
player = FirstPersonController(position_y=20)

window.show_ursina_splash = True
window.title = 'Life Of Rail'
Sky()
app.run()
while True:
	pass
