from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import os

app = Ursina()
rail = []

class Circles(Mesh):
    def __init__(self, radius=.5, rotate=True, mode='line', angle=360, **kwargs):
        origin = Entity()
        point = Entity(parent=origin)
        point.y = radius

        self.vertices = list()
        for i in range(int(angle)):
            origin.rotation_z -= 1
            self.vertices.append(point.world_position)

        if mode != 'line':  # add the first point to make the circle whole
            self.vertices.append(origin.world_position)
        destroy(origin)
        super().__init__(vertices=self.vertices, mode=mode, **kwargs)

"""class Rail():
    def __init__(self,data={'mode':'straight','start':[(1.5,0.1,-100),(-1.5,0.1,-100)],'end':[(1.5,0.1,100),(-1.5,0.1,100)],'rotation':(0,0,0)}):
        if data['mode'] == 'straight':
            self.rail1 = Entity(parent=scene,model=Mesh(vertices=[data['start'][0],data['end'][0]],mode='line',thickness=50),rotation=data['rotation'],color=rgb(70, 42, 42))
            self.rail2 = Entity(parent=scene,model=Mesh(vertic0es=[data['start'][1],data['end'][1]],mode='line',thickness=50),rotation=data['rotation'],color=rgb(70, 42, 42))
        elif data['mode'] == 'turn':
            self.rail1 = Entity(Circles(radius=data['radius'][0]+1.5,angle=data['angle']),rotation=data['rotation'],position=data['position'][0])
            self.rail2 = Entity(Circles(radius=data['radius'][1]+1.5,angle=data['angle']),rotation=data['rotation'],position=data['position'][1])"""

class Rail():
    def __init__(self,data={'position':(5,0,0),'heading':0,'length':50}):
        self.middle= Entity(position=data['position'],rotation=(0,data['heading'],0),)
        self.rail1 = Entity(parent=self.middle,x=-1.5,z=data['position'][2]+(data['length']/2),model='cube',scale=(0.25,0.25,data['length']),collision=True,collider='box',color=color.rgb(128,64,0))
        self.rail2 = Entity(parent=self.middle,x= 1.5,z=data['position'][2]+(data['length']/2),model='cube',scale=(0.25,0.25,data['length']),collision=True,collider='box',color=color.rgb(128,64,0))

class Train(Entity):
    def __init__(self):
        super().__init__(
            model='\\assets\\train\\Amtrak\\model\\f59phi\\f59phi.obj',
            texture='\\assets\\texture\\train.png',
            color=rgb(100,100,100)
        )

floor = Entity(model='plane', scale=(1000,5,1000), color=color.rgb(0,100,0),collision = True,collider='plane')
player = FirstPersonController(height=20)
train = Train()

class Continue_button(Button):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            text = 'continue',
            ignore_paused = True
        )
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                application.paused = False
                mouse.visible = False
                mouse.locked = True
                destroy(self)

def input(key):
    if key == 'escape':
        application.paused = True
        mouse.visible = True
        mouse.locked = False
        continue_button = Continue_button()
    if held_keys['shift']:
        player.speed = 25
    else:
        player.speed = 5
    if held_keys['control'] and key == 'r':
        player.position = (0,0,0)
 
rail.append(Rail())
#rail.append(Rail(data={'mode':'turn','position':[(1.5,0.5,0),(-1.5,.5,0)],'rotation':(0,0,0),'radius':[61.5,58.5],'angle':90}))

app.run()