#Tablet UI
#2018 - 2018 Steven Payne, PyTablUI

from tkinter import *
from picamera import *
from TabletCamera import cameraFunctions
from TabletLayouts import SelectImageEffects

global root, camera
root = Tk()
frame =Frame(root)
frame.pack()
camera = PiCamera()

camera.start_preview(fullscreen=False, window=(100, 200, 600, 800))

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

