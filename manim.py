from manim import *
import math
from gateq.matrix.views import inputs

# class FirstManim(Scene):
#     def construct(self,x1=0.8):
#         green_square=Square(2,color=GREEN_A)
#         green_square.set_fill(color=YELLOW,opacity=x1)
#         ax=Axes(x_range=(-10,10),y_range=(-5,5))
#         wave =ax.plot(lambda x: math.sin(x),color=RED)
#         area= ax.get_area(wave,x_range=(-10,10))
#         self.add(ax)
#         self.play(Create(wave),run_time=3)
#         self.play(FadeIn(area),color=RED,opacity=0.8)


#inputs=['11', '12', '13', '21', '22', '23', '31', '32', '33', '41', '42', '43', '51', '52', '53', '61', '62', '63']

      # Note the difference from the manual!!!
class d3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        global inputs
        circle=Circle(radius=5.0, color=WHITE, fill_opacity = 1)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES, gamma=None,zoom=0.5, focal_distance=None, )
#############################
#location of static objects
        print("Coordinates of Objects in [X,Y,Z] format are-")
        locations = """Source = [9,0,0].Beam Splitter = [7,0,0].Polariser = [5,0,0].Crystal Beam Splitter = [0,0,0].Mirror[-3,0,0].Mirror[-3,0,0].Mirror[-3,0,0].Mirror[-3,0,0].Mirror[-3,0,0].Mirror[-3,0,0].Mirror[-3,1,0].Mirror[--1,0,0].Mirror[-13,0,0].Mirror[-15,0,0].Mirror[-15,0,0].Mirror[-3,0,0]"""
        coordinates = locations.split(".")
        for x in coordinates:
          print(" "+x)
        print("Path of the light as straight lines between the objects-")
        locations = """Source = [9,0,0].[7,0,0].[5,0,0].[0,0,0].[-3,0,0].[-3,2,0] [-3,3,0] [-3,5,0] [-3,6,0]--Sink.[-3,7,0].[-3,1,0].[--1,0,0].[-13,0,0].[-15,0,0] [-15,2,0]--sink.[-22,0,0]--sink"""
        coordinates = locations.split(".")
        for x in coordinates:
          print(" "+x)
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


        #cylinder1 = Cylinder(radius=0.5, height=0.1, direction=[1., 0., 0.]).move_to([1,0,0])
        #self.add(cylinder1)

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
        ###################
        if slm2_x[2] != -1:

           cube2 = Cube(side_length=1, fill_opacity=0.7, fill_color=PINK).move_to([-17, -3, 0])
           self.add(cube2)
###############################
        if lc_x[2] != -1:
            cube2 = Cube(side_length=1, fill_opacity=0.7, fill_color=PINK).move_to([-20, -8, 0])
            self.add(cube2)
###############################
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





# #######################################################################################
# ###ANIMATION PART#
# ############################################################################################
#         #laser
#         #
#         laser1 = Cylinder(radius=0.2, height=1, direction=[1., 0., 0.]).move_to([8,0,0])
#         laser1 = laser1.set_color(RED)

#         laser2 = Cylinder(radius=0.2, height=1, direction=[1., 0., 0.]).move_to([-2,0,0])
#         laser2 = laser2.set_color(PINK)

#         laser3 = Cylinder(radius=0.2, height=1, direction=[0., 1., 0.]).move_to([-7,0,0])
#         laser3 = laser3.set_color(PINK)
#         #self.add(cylinder4)
#         self.play(
#             laser1.animate.move_to([-2,0,0]), run_time=2
            
#         )
#         self.play(FadeOut(laser1))
#         self.play(
#             laser2.animate.move_to([-7,0,0]), run_time=2
            
#         )
#         self.play(FadeOut(laser2))
#         self.play(
#             laser3.animate.move_to([-7,3,0]), run_time=2
            
#         )
#         self.play(FadeOut(laser3))
        
#         ########
#         #laser = Cylinder(radius=0.2, height=1, direction=[0., 1., 0.]).move_to([-7,3,0])
#        # laser = laser.set_color(PINK)
#         #self.play(
#             #laser.animate.move_to([-7,5,0]), run_time=2
            
#         #)
#         #self.play(FadeOut(laser))
# #
#         #laser = Cylinder(radius=0.2, height=1, direction=[0., 1., 0.]).move_to([-7,3,0])
#         #laser = laser.set_color(PINK)
#         #self.play(
#             #laser.animate.move_to([-7,5,0]), run_time=2
            
#         #)
#         #self.play(FadeOut(laser))
#         #
        
#         laser = Cylinder(radius=0.2, height=1, direction=[1., 0., 0.]).move_to([-7,3,0])
#         laser = laser.set_color(PINK)
#         self.play(
#             laser.animate.move_to([-16,3,0]), run_time=2
            
#         )
#         self.play(FadeOut(laser))
#         #
#         laser = Cylinder(radius=0.2, height=1, direction=[0., 1., 0.]).move_to([-20,3,0])
#         laser = laser.set_color(PINK)
#         self.play(
#             laser.animate.move_to([-20,-11,0]), run_time=2
            
#         )
#         self.play(FadeOut(laser))
     ######################################   
        #l2 = ThreeDVMobject()
        
        #l2.add_updater(lambda x: x.become(Line3D(LEFT, d1.get_center()).set_color(RED)))
        #self.play(MoveAlongPath(d1, path), rate_func=linear)


        self.begin_3dillusion_camera_rotation(rate=1)
        self.wait(PI)
        self.stop_3dillusion_camera_rotation()
        #self.begin_3dillusion_camera_rotation(rate=1)
        #self.wait(PI)
       # self.stop_3dillusion_camera_rotation()
c1=d3()
