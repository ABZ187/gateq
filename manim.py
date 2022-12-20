from manim import *

x1=1

      # Note the difference from the manual!!!
class d3(ThreeDScene):
    def construct(self,x=x1):
        axes = ThreeDAxes()
        circle=Circle(radius=5.0, color=WHITE, fill_opacity = x)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES, gamma=None,zoom=0.5, focal_distance=None, )
#############################
#############################
#---------------------All Lenses and cubes!!!
#(lens0 - lens off the x axis)        
        
        #self.add(circle,axes)
        self.add(axes)
        source = Cube(side_length=0.5, fill_opacity=1, fill_color=YELLOW_E).move_to([9, 0, 0])
        self.add(source)

        cube1 = Cube(side_length=1, fill_opacity=0.7, fill_color=PINK).move_to([-2, 0, 0])
        #cube1.shift(2*RIGHT)

        lens0 = Cylinder(radius=0.5, height=0.1, direction=[0., 1., 0.]).move_to([-2,-2,0])
        self.add(lens0)


        cylinder1 = Cylinder(radius=0.5, height=0.1, direction=[1., 0., 0.]).move_to([1,0,0])
        self.add(cylinder1)

        cylinder2 = Cylinder(radius=0.5, height=0.2, direction=[1., 0., 0.]).move_to([4,0,0])
        self.add(cylinder2)

        cylinder3 = Cylinder(radius=0.5, height=0.1, direction=[1., 1., 0.]).move_to([7,0,0])
        self.add(cylinder3)

        sink0 = Cube(side_length=0.5, fill_opacity=1, fill_color=YELLOW_E).move_to([7, -2, 0])
        self.add(sink0)

        lens0 = Cylinder(radius=0.5, height=0.1, direction=[0., 1., 0.]).move_to([-7,2,0])
        self.add(lens0)

        cylinder1 = Cylinder(radius=0.5, height=0.1, direction=[1., 0., 0.]).move_to([-11,3,0])
        self.add(cylinder1)

        cube2 = Cube(side_length=1, fill_opacity=0.7, fill_color=PINK).move_to([-13, 3, 0])
        self.add(cube2)

        cube2 = Cube(side_length=1, fill_opacity=0.7, fill_color=PINK).move_to([-17, -3, 0])
        self.add(cube2)

        cube2 = Cube(side_length=1, fill_opacity=0.7, fill_color=PINK).move_to([-20, -8, 0])
        self.add(cube2)
        cylinder1 = Cylinder(radius=0.5, height=0.1, direction=[0., 1., 0.]).move_to([-20,-9,0])
        self.add(cylinder1)
        cylinder1 = Cylinder(radius=0.5, height=0.1, direction=[0., 1., 0.]).move_to([-20,-10,0])
        self.add(cylinder1)
        end = Cube(side_length=0.3, fill_opacity=1, fill_color=GREEN_E).move_to([-20, -11, 0])
        self.add(end)
        mirror = Prism(dimensions=[1, 0.5, 0.5])
        mirror = mirror.move_to([-20, -5, 0])
        mirror = mirror.set_color(WHITE)
        self.add(mirror)


#######################
#########################
#-----------------objectt!!
#object at [-17,-5,0]
        mirror = Prism(dimensions=[1, 0.5, 0.5])
        mirror = mirror.move_to([-17, -5, 0])
        mirror = mirror.set_color(WHITE)
        self.add(mirror)

######################
######################
#-----------------------------------ALL Optical Cables with Caps!

#Cable at [-2,0,0]
        end = Cube(side_length=0.3, fill_opacity=1, fill_color=GREEN_E).move_to([-2, -2.5, 0.1])
        self.add(end)
        for x in range(6):
          cable = Torus(major_radius=1, minor_radius=0.02, u_range=(0, 6.283185307179586), v_range=(0, 6.283185307179586), resolution=None).move_to([-2, -4, x/10])
          cable = cable.set_color(YELLOW_C)
          self.add(cable)
        cable = Line3D(start=np.array([-2, -2.4, 0]), end=np.array([-2,-3.3,0.5])).set_color(YELLOW_C)
        self.add(cable)
        cable = Line3D(start=np.array([-2.5, -3.5, 0.5]), end=np.array([-4.5,-3.5,0.5])).set_color(YELLOW_C)
        self.add(cable)
        end = Cube(side_length=0.3, fill_opacity=1, fill_color=GREEN_E).move_to([-4.5, -3.5, 0.5])
        self.add(end)

#Cable at [-2,0,0]
        end = Cube(side_length=0.3, fill_opacity=1, fill_color=GREEN_E).move_to([-5, -2.5, 0.1])
        self.add(end)
        cable = Line3D(start=np.array([-20, -11, 0]), end=np.array([-4.5, -3.5, 0.5])).set_color(YELLOW_C)
        self.add(cable)
        
#######################
#######################
#----------------------------------------All Mirrors

#Mirror at[-7,0,0]
        mirror = Prism(dimensions=[0.3, 1, 1]).rotate(PI / 4)
        mirror = mirror.move_to([-7, 0, 0])
        mirror = mirror.set_color(WHITE)
        self.add(mirror)
#mirror at [-7,4,0]
        mirror = Prism(dimensions=[0.3, 1, 1]).rotate(PI / 4)
        mirror = mirror.move_to([-7, 4, 0])
        mirror = mirror.set_color(WHITE)
        self.add(mirror)
#mirror at [-8,3,0]
        mirror = Prism(dimensions=[0.3, 1, 1]).rotate(-1*PI / 4)
        mirror = mirror.move_to([-8, 3, 0])
        mirror = mirror.set_color(WHITE)
        self.add(mirror)
#mirror at [-9,4,0]
        mirror = Prism(dimensions=[0.3, 1, 1])
        mirror = mirror.move_to([-9, 4, 0])
        mirror = mirror.set_color(WHITE)
        self.add(mirror)

#mirror at [-15,4,0]
        mirror = Prism(dimensions=[0.3, 1, 1])
        mirror = mirror.move_to([-15, 4, 0])
        mirror = mirror.set_color(WHITE)
        self.add(mirror)

#mirror at [-17,3,0]
        mirror = Prism(dimensions=[0.3, 1, 1])
        mirror = mirror.move_to([-17, 3, 0])
        mirror = mirror.set_color(WHITE)
        self.add(mirror)

#mirror at [-16,-8,0]
        mirror = Prism(dimensions=[0.3, 1, 1])
        mirror = mirror.move_to([-16,-8,0])
        mirror = mirror.set_color(WHITE)
        self.add(mirror)

#mirror at [-22,-8,0]
        mirror = Prism(dimensions=[0.3, 1, 1])
        mirror = mirror.move_to([-22,-8,0])
        mirror = mirror.set_color(WHITE)
        self.add(mirror)

#mirror at [-22,-8,0]
        mirror = Prism(dimensions=[0.3, 1, 1])
        mirror = mirror.move_to([-22,3,0])
        mirror = mirror.set_color(WHITE)
        self.add(mirror)
#######################
#######################



        self.add(cube1)


        #self.begin_3dillusion_camera_rotation(rate=1)
        #self.wait(PI)
       # self.stop_3dillusion_camera_rotation()

c1=d3()
