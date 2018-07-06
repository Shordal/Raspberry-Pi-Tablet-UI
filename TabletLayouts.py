#Tablet UI
#2018 - 2018 Steven payne, PyTablUI

from tkinter import *
from picamera import *
from TabletCamera import *
from imageEffects import *
import TabletUi

class SelectImageEffects(object):
        
    def imageEffectSelectionLayout(camera,  frame):
        
        
        takePictureButton = Button(frame,  text = "Take Picture!", activebackground = 'blue', activeforeground = 'red', bg = 'red', fg ='black', command = lambda: cameraFunctions.takePicture(camera))
        takePictureButton.grid(row = 0,  column = 0,  sticky = 'nwew')
        
        cameraNegativeButton = Button(frame,  text = "Negative", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraNegative(camera))
        cameraNegativeButton.grid(row = 0,  column = 1,  sticky = 'nwew')
        
        EffectsLabel = Label(frame,  text = "Select an Effect!", bg = 'purple',  fg = 'white',  font = "Helvetica, 16")
        EffectsLabel.grid(row =0,  column= 2,  columnspan = 2,  sticky = 'nwew' )
        
        cameraSolarizeButton = Button(frame,  text = "Solarize", activebackground = 'blue', activeforeground = 'red',   command = lambda: cameraImageEffects.cameraSolarize(camera))
        cameraSolarizeButton.grid(row = 5,  column = 1,  sticky = 'nwew')
        
        cameraSketchButton = Button(frame,  text = "Sketch", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraSketch(camera))
        cameraSketchButton.grid(row = 5,  column = 2,  sticky = 'nwew')
        
        cameraDenoiseButton = Button(frame,  text = "Denoise", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraDenoise(camera))
        cameraDenoiseButton.grid(row = 1,  column = 0,  sticky = 'nwew')
        
        cameraEmbossButton = Button(frame,  text = "Emboss", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraEmboss(camera))
        cameraEmbossButton.grid(row = 1,  column = 1,  sticky = 'nwew')
        
        cameraOilpaintButton = Button(frame,  text = "Oil Paint", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraOilpaint(camera))
        cameraOilpaintButton.grid(row = 1,  column = 2,  sticky = 'nwew')
        
        cameraHatchButton = Button(frame,  text = "Hatch", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraHatch(camera))
        cameraHatchButton.grid(row = 1,  column = 3,  sticky = 'nwew')
        
        cameraGpenButton = Button(frame,  text = "Gpen", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraGpen(camera))
        cameraGpenButton.grid(row = 2,  column = 0,  sticky = 'nwew')
        
        cameraPastelButton = Button(frame,  text = "Pastel", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraPastel(camera))
        cameraPastelButton.grid(row = 2,  column = 1,  sticky = 'nwew')
        
        cameraWatercolorButton = Button(frame,  text = "Water Colors", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraWatercolor(camera))
        cameraWatercolorButton.grid(row = 2,  column = 2,  sticky = 'nwew')
        
        cameraFilmButton = Button(frame,  text = "Film", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraFilm(camera))
        cameraFilmButton.grid(row = 2,  column = 3,  sticky = 'nwew')
        
        cameraBlurButton = Button(frame,  text = "Blur", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraBlur(camera))
        cameraBlurButton.grid(row = 3,  column = 0,  sticky = 'nwew')
        
        cameraSaturationButton = Button(frame,  text = "Saturation", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraSaturation(camera))
        cameraSaturationButton.grid(row = 3,  column = 1,  sticky = 'nwew')
        
        cameraColorswapButton = Button(frame,  text = "Swap Colors", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraColorswap(camera))
        cameraColorswapButton.grid(row = 3,  column = 2,  sticky = 'nwew')
        
        cameraWashedoutButton = Button(frame,  text = "Washed Out", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraWashedout(camera))
        cameraWashedoutButton.grid(row = 3,  column = 3,  sticky = 'nwew')
        
        cameraPosteriseButton = Button(frame,  text = "Posterise", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraPosterise(camera))
        cameraPosteriseButton.grid(row = 4,  column = 0,  sticky = 'nwew')
        
        cameraColorpointButton = Button(frame,  text = "Color Point", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraColorpoint(camera))
        cameraColorpointButton.grid(row = 4,  column = 1,  sticky = 'nwew')
        
        cameraColorbalanceButton = Button(frame,  text = "Color Balance", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraColorbalance(camera))
        cameraColorbalanceButton.grid(row = 4,  column = 2,  sticky = 'nwew')
        
        cameraCartoonButton = Button(frame,  text = "Cartoon", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraCartoon(camera))
        cameraCartoonButton.grid(row = 4,  column = 3,  sticky = 'nwew')
        
        cameraNoneButton = Button(frame,  text = "None!", activebackground = 'blue', activeforeground = 'red', command = lambda: cameraImageEffects.cameraNone(camera))
        cameraNoneButton.grid(row = 5,  column = 3,  sticky = 'nwew')
        
        BackTomainButton = Button(frame,  text ="Main Menu",  activebackground = 'black', activeforeground = 'white',  fg = 'black',  bg = 'white', command = lambda: backToMainCleanUp(camera))
        BackTomainButton.grid(row = 5,  column = 0,  sticky = 'nsew')
    
        def backToMainCleanUp(camera):
            
            takePictureButton.destroy(), cameraNegativeButton.destroy(), EffectsLabel.destroy(), cameraSolarizeButton.destroy(), cameraSketchButton.destroy(), cameraDenoiseButton.destroy()
            cameraEmbossButton.destroy(), cameraOilpaintButton.destroy(), cameraHatchButton.destroy(), cameraGpenButton.destroy(), cameraPastelButton.destroy(), cameraWatercolorButton.destroy()
            cameraFilmButton.destroy(), cameraBlurButton.destroy(), cameraSaturationButton.destroy(), cameraColorswapButton.destroy(), cameraWashedoutButton.destroy(), cameraPosteriseButton.destroy()
            cameraColorpointButton.destroy(), cameraColorbalanceButton.destroy(), cameraCartoonButton.destroy(), cameraNoneButton.destroy(), BackTomainButton.destroy()
            
            TabletUi.StartUpLayOut(camera)
            

    
    
#class CreatorInformaiton:
    
    
