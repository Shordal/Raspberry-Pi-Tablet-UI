#Tablet UI
#2018 - 2018 Steven Payne, PyTabletUI

from tkinter import *
from picamera import *
from TabletCamera import cameraFunctions
from TabletLayouts import SelectImageEffects

global root, camera
root = Tk()
frame =Frame(root)


root.geometry('430x170+0+0')
#width, hight, x, y
root.overrideredirect(1)

frame.pack()
camera = PiCamera()
camera.resolution = (1280, 720)
camera.video_stabilization = "True"
camera.start_preview(fullscreen=False, window=(0,  50, 550, 550))
#location: X, location: Y, Width, Hight


class StartUpLayOut:
    
    def __init__(self, root): 
        
        goToImageEffects = Button(frame,  text = "Image Effects",  command = lambda: GoToImageEffects(camera, frame))
        goToImageEffects.grid(row = 0,  column = 0)
        
        takePictureButton = Button(frame,  text = "Take Picture!",  command = lambda: cameraFunctions.takePicture(camera))
        takePictureButton.grid(row = 0,  column = 1)
        
        exitButton = Button(frame,  text = 'Quit',  command = lambda: exitButton())
        exitButton.grid(row = 0, column = 2)
        
        def GoToImageEffects(camera, frame):
            
            goToImageEffects.destroy(),  takePictureButton.destroy()
            SelectImageEffects.imageEffectSelectionLayout(camera, frame)
            
        def exitButton():
            
            global root
            camera.stop_preview()
            root.destroy()
        
Start = StartUpLayOut(root)

root.mainloop()

