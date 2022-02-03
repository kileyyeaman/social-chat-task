#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.2),
    on Tue Aug 10 11:56:46 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2021')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.2'
expName = 'chat_task_A'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'gender': ['Male', 'Female'], 'age': ['9-11', '12-14']}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/kileyyeaman/Documents/Chat Task/chat_task_A.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instrA"
instrAClock = core.Clock()
instAtxt = visual.TextStim(win=win, name='instAtxt',
    text='We will now show you the pictures and profiles of other participants in this study.\n\nPlease select 5 other kids you are INTERESTED in chatting with. To select, click the left button of your mouse.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instAkey = keyboard.Keyboard()

# Initialize components for Routine "selA"
selAClock = core.Clock()
rightBox = visual.Rect(
    win=win, name='rightBox',
    width=(1, 0.5)[0], height=(1, 0.5)[1],
    ori=0.0, pos=(.50, -.25),
    lineWidth=7.0,     colorSpace='rgb',  lineColor='blue', fillColor='white',
    opacity=0.0, depth=0.0, interpolate=True)
leftBox = visual.Rect(
    win=win, name='leftBox',
    width=(1, 0.5)[0], height=(1, 0.5)[1],
    ori=0.0, pos=(-.50, -.25),
    lineWidth=7.0,     colorSpace='rgb',  lineColor='blue', fillColor='white',
    opacity=0.0, depth=-1.0, interpolate=True)
F01 = visual.ImageStim(
    win=win,
    name='F01', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F01.bmp", mask=None,
    ori=0.0, pos=(-.72, .43), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
F02 = visual.ImageStim(
    win=win,
    name='F02', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F02.bmp", mask=None,
    ori=0.0, pos=(-.59, .43), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
F03 = visual.ImageStim(
    win=win,
    name='F03', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F03.bmp", mask=None,
    ori=0.0, pos=(-.46, .43), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
F04 = visual.ImageStim(
    win=win,
    name='F04', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F04.bmp", mask=None,
    ori=0.0, pos=(-.33, .43), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
F05 = visual.ImageStim(
    win=win,
    name='F05', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F05.bmp", mask=None,
    ori=0.0, pos=(-.20, .43), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
F06 = visual.ImageStim(
    win=win,
    name='F06', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F06.bmp", mask=None,
    ori=0.0, pos=(-.07, .43), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
F07 = visual.ImageStim(
    win=win,
    name='F07', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F07.bmp", mask=None,
    ori=0.0, pos=(.06, .43), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
F08 = visual.ImageStim(
    win=win,
    name='F08', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F08.bmp", mask=None,
    ori=0.0, pos=(.19, .43), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
F09 = visual.ImageStim(
    win=win,
    name='F09', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F09.bmp", mask=None,
    ori=0.0, pos=(.32, .43), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
F10 = visual.ImageStim(
    win=win,
    name='F10', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F10.bmp", mask=None,
    ori=0.0, pos=(.45, .43), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
F11 = visual.ImageStim(
    win=win,
    name='F11', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F11.bmp", mask=None,
    ori=0.0, pos=(.45, .43), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
F12 = visual.ImageStim(
    win=win,
    name='F12', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F12.bmp", mask=None,
    ori=0.0, pos=(.58, .43), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
F13 = visual.ImageStim(
    win=win,
    name='F13', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F13.bmp", mask=None,
    ori=0.0, pos=(.71, .43), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
F14 = visual.ImageStim(
    win=win,
    name='F14', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F14.bmp", mask=None,
    ori=0.0, pos=(-.72, .28), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
F15 = visual.ImageStim(
    win=win,
    name='F15', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F15.bmp", mask=None,
    ori=0.0, pos=(-.59, .28), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
F16 = visual.ImageStim(
    win=win,
    name='F16', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F16.bmp", mask=None,
    ori=0.0, pos=(-.46, .28), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
F17 = visual.ImageStim(
    win=win,
    name='F17', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F17.bmp", mask=None,
    ori=0.0, pos=(-.33, .28), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-19.0)
F18 = visual.ImageStim(
    win=win,
    name='F18', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F18.bmp", mask=None,
    ori=0.0, pos=(-.20, .28), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
F19 = visual.ImageStim(
    win=win,
    name='F19', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F19.bmp", mask=None,
    ori=0.0, pos=(-.07, .28), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-21.0)
F20 = visual.ImageStim(
    win=win,
    name='F20', 
    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_F20.bmp", mask=None,
    ori=0.0, pos=(.06, .28), size=(0.103125, 0.1375),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-22.0)
selAmouse = event.Mouse(win=win)
x, y = [None, None]
selAmouse.mouseClock = core.Clock()
femCount = visual.TextStim(win=win, name='femCount',
    text='',
    font='Open Sans',
    pos=(.71, -.47), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-24.0);
maleCount = visual.TextStim(win=win, name='maleCount',
    text='',
    font='Open Sans',
    pos=(-.73, -.47), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-25.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "instrB"
instrBClock = core.Clock()
instBtxt = visual.TextStim(win=win, name='instBtxt',
    text='We will now show you brief profiles of 5 kids who matched with you. Please rank the kids from 1 through 5, with 1 being the kid you MOST want to chat with. ',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instBkey = keyboard.Keyboard()

# Initialize components for Routine "selB"
selBClock = core.Clock()
selBtxt = visual.TextStim(win=win, name='selBtxt',
    text='Rank the other kids from 1 to 5, starting with the kid you MOST want to chat with:',
    font='Open Sans',
    pos=(0, .45), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
selBkey = keyboard.Keyboard()
selBmouse = event.Mouse(win=win)
x, y = [None, None]
selBmouse.mouseClock = core.Clock()
prof1 = visual.Rect(
    win=win, name='prof1',
    width=(0.4, 0.2)[0], height=(0.4, 0.2)[1],
    ori=0.0, pos=(-.45, .25),
    lineWidth=3.0,     colorSpace='rgb',  lineColor='black', fillColor='gray',
    opacity=None, depth=-5.0, interpolate=True)
prof1txt = visual.TextStim(win=win, name='prof1txt',
    text='',
    font='Open Sans',
    pos=(-.45, .25), height=0.0275, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
prof2 = visual.Rect(
    win=win, name='prof2',
    width=(0.4, 0.2)[0], height=(0.4, 0.2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=3.0,     colorSpace='rgb',  lineColor='black', fillColor='gray',
    opacity=None, depth=-7.0, interpolate=True)
prof2txt = visual.TextStim(win=win, name='prof2txt',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.0275, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
prof3 = visual.Rect(
    win=win, name='prof3',
    width=(0.4, 0.2)[0], height=(0.4, 0.2)[1],
    ori=0.0, pos=(-.45, -.25),
    lineWidth=3.0,     colorSpace='rgb',  lineColor='black', fillColor='gray',
    opacity=None, depth=-9.0, interpolate=True)
prof3txt = visual.TextStim(win=win, name='prof3txt',
    text='',
    font='Open Sans',
    pos=(-.45, -.25), height=0.0275, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
prof4 = visual.Rect(
    win=win, name='prof4',
    width=(0.4, 0.2)[0], height=(0.4, 0.2)[1],
    ori=0.0, pos=(.45, .25),
    lineWidth=3.0,     colorSpace='rgb',  lineColor='black', fillColor='gray',
    opacity=None, depth=-11.0, interpolate=True)
prof4txt = visual.TextStim(win=win, name='prof4txt',
    text='',
    font='Open Sans',
    pos=(.45, .25), height=0.0275, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
prof5 = visual.Rect(
    win=win, name='prof5',
    width=(0.4, 0.2)[0], height=(0.4, 0.2)[1],
    ori=0.0, pos=(.45, -.25),
    lineWidth=3.0,     colorSpace='rgb',  lineColor='black', fillColor='gray',
    opacity=None, depth=-13.0, interpolate=True)
prof5txt = visual.TextStim(win=win, name='prof5txt',
    text='',
    font='Open Sans',
    pos=(.45, -.25), height=0.0275, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);

# Initialize components for Routine "Goodbye"
GoodbyeClock = core.Clock()
byeTxt = visual.TextStim(win=win, name='byeTxt',
    text='Goodbye!',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
byeKey = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instrA"-------
continueRoutine = True
# update component parameters for each repeat
instAkey.keys = []
instAkey.rt = []
_instAkey_allKeys = []
# keep track of which components have finished
instrAComponents = [instAtxt, instAkey]
for thisComponent in instrAComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrAClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrA"-------
while continueRoutine:
    # get current time
    t = instrAClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrAClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instAtxt* updates
    if instAtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instAtxt.frameNStart = frameN  # exact frame index
        instAtxt.tStart = t  # local t and not account for scr refresh
        instAtxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instAtxt, 'tStartRefresh')  # time at next scr refresh
        instAtxt.setAutoDraw(True)
    
    # *instAkey* updates
    waitOnFlip = False
    if instAkey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instAkey.frameNStart = frameN  # exact frame index
        instAkey.tStart = t  # local t and not account for scr refresh
        instAkey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instAkey, 'tStartRefresh')  # time at next scr refresh
        instAkey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instAkey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instAkey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instAkey.status == STARTED and not waitOnFlip:
        theseKeys = instAkey.getKeys(keyList=['space'], waitRelease=False)
        _instAkey_allKeys.extend(theseKeys)
        if len(_instAkey_allKeys):
            instAkey.keys = _instAkey_allKeys[-1].name  # just the last key pressed
            instAkey.rt = _instAkey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrAComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrA"-------
for thisComponent in instrAComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instrA" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "selA"-------
continueRoutine = True
# update component parameters for each repeat
male_count = 'Males: 0'
female_count = 'Females: 0'

photos = [F01, F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20]
selectedPhotos = []
selectedPhotoNames = []
male_pos = [(-.72, -.10), (-.60, -.10), (-.48, -.10),(-.36, -.10),(-.24, -.10), (-2, -2)]
female_pos = [(.72, -.10), (.60, -.10), (.48, -.10),(.36, -.10),(.24, -.10),(-2, -2)]


# setup some python lists for storing info about the selAmouse
selAmouse.x = []
selAmouse.y = []
selAmouse.leftButton = []
selAmouse.midButton = []
selAmouse.rightButton = []
selAmouse.time = []
selAmouse.clicked_name = []
gotValidClick = False  # until a click is received
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
selAComponents = [rightBox, leftBox, F01, F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20, selAmouse, femCount, maleCount, key_resp]
for thisComponent in selAComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
selAClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "selA"-------
while continueRoutine:
    # get current time
    t = selAClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=selAClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rightBox* updates
    if rightBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rightBox.frameNStart = frameN  # exact frame index
        rightBox.tStart = t  # local t and not account for scr refresh
        rightBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rightBox, 'tStartRefresh')  # time at next scr refresh
        rightBox.setAutoDraw(True)
    
    # *leftBox* updates
    if leftBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        leftBox.frameNStart = frameN  # exact frame index
        leftBox.tStart = t  # local t and not account for scr refresh
        leftBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(leftBox, 'tStartRefresh')  # time at next scr refresh
        leftBox.setAutoDraw(True)
    for x in range(0,6):
        if len(selAmouse.clicked_name) == x  and expInfo['gender'] == 'Male':
            male_count = 'Males:' + str(x)
            female_count = 'Females: 0'
            for i in photos: 
                if selAmouse.isPressedIn(i):
                    pic1 = visual.ImageStim(win = win,
                    name = 'pic1',
                    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_"+str(i.name)+".bmp", mask=None,
                    ori=0.0, pos= male_pos[x], size=(0.103125, 0.1375),
                    color=[1,1,1], colorSpace='rgb', opacity=None,
                    flipHoriz=False, flipVert=False,
                    texRes=128.0, interpolate=True, depth=-1.0)
                    selectedPhotos.append(pic1)
                    photos.remove(i)
                    for selectedPic in selectedPhotos:
                        selectedPic.setAutoDraw(True)
        elif len(selAmouse.clicked_name) == x  and expInfo['gender'] == 'Female':
            male_count = 'Males: 0'
            female_count = 'Females:' + str(x)
            for i in photos: 
                if selAmouse.isPressedIn(i):
                    pic1 = visual.ImageStim(win = win,
                    name = 'pic1',
                    image="Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_"+str(i.name)+".bmp", mask=None,
                    ori=0.0, pos= female_pos[x], size=(0.103125, 0.1375),
                    color=[1,1,1], colorSpace='rgb', opacity=None,
                    flipHoriz=False, flipVert=False,
                    texRes=128.0, interpolate=True, depth=-1.0)
                    selectedPhotos.append(pic1)
                    photos.remove(i)
                    for selectedPic in selectedPhotos:
                        selectedPic.setAutoDraw(True)
    
    
    # *F01* updates
    if F01.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F01.frameNStart = frameN  # exact frame index
        F01.tStart = t  # local t and not account for scr refresh
        F01.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F01, 'tStartRefresh')  # time at next scr refresh
        F01.setAutoDraw(True)
    
    # *F02* updates
    if F02.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F02.frameNStart = frameN  # exact frame index
        F02.tStart = t  # local t and not account for scr refresh
        F02.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F02, 'tStartRefresh')  # time at next scr refresh
        F02.setAutoDraw(True)
    
    # *F03* updates
    if F03.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F03.frameNStart = frameN  # exact frame index
        F03.tStart = t  # local t and not account for scr refresh
        F03.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F03, 'tStartRefresh')  # time at next scr refresh
        F03.setAutoDraw(True)
    
    # *F04* updates
    if F04.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F04.frameNStart = frameN  # exact frame index
        F04.tStart = t  # local t and not account for scr refresh
        F04.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F04, 'tStartRefresh')  # time at next scr refresh
        F04.setAutoDraw(True)
    
    # *F05* updates
    if F05.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F05.frameNStart = frameN  # exact frame index
        F05.tStart = t  # local t and not account for scr refresh
        F05.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F05, 'tStartRefresh')  # time at next scr refresh
        F05.setAutoDraw(True)
    
    # *F06* updates
    if F06.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F06.frameNStart = frameN  # exact frame index
        F06.tStart = t  # local t and not account for scr refresh
        F06.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F06, 'tStartRefresh')  # time at next scr refresh
        F06.setAutoDraw(True)
    
    # *F07* updates
    if F07.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F07.frameNStart = frameN  # exact frame index
        F07.tStart = t  # local t and not account for scr refresh
        F07.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F07, 'tStartRefresh')  # time at next scr refresh
        F07.setAutoDraw(True)
    
    # *F08* updates
    if F08.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F08.frameNStart = frameN  # exact frame index
        F08.tStart = t  # local t and not account for scr refresh
        F08.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F08, 'tStartRefresh')  # time at next scr refresh
        F08.setAutoDraw(True)
    
    # *F09* updates
    if F09.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F09.frameNStart = frameN  # exact frame index
        F09.tStart = t  # local t and not account for scr refresh
        F09.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F09, 'tStartRefresh')  # time at next scr refresh
        F09.setAutoDraw(True)
    
    # *F10* updates
    if F10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F10.frameNStart = frameN  # exact frame index
        F10.tStart = t  # local t and not account for scr refresh
        F10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F10, 'tStartRefresh')  # time at next scr refresh
        F10.setAutoDraw(True)
    
    # *F11* updates
    if F11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F11.frameNStart = frameN  # exact frame index
        F11.tStart = t  # local t and not account for scr refresh
        F11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F11, 'tStartRefresh')  # time at next scr refresh
        F11.setAutoDraw(True)
    
    # *F12* updates
    if F12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F12.frameNStart = frameN  # exact frame index
        F12.tStart = t  # local t and not account for scr refresh
        F12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F12, 'tStartRefresh')  # time at next scr refresh
        F12.setAutoDraw(True)
    
    # *F13* updates
    if F13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F13.frameNStart = frameN  # exact frame index
        F13.tStart = t  # local t and not account for scr refresh
        F13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F13, 'tStartRefresh')  # time at next scr refresh
        F13.setAutoDraw(True)
    
    # *F14* updates
    if F14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F14.frameNStart = frameN  # exact frame index
        F14.tStart = t  # local t and not account for scr refresh
        F14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F14, 'tStartRefresh')  # time at next scr refresh
        F14.setAutoDraw(True)
    
    # *F15* updates
    if F15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F15.frameNStart = frameN  # exact frame index
        F15.tStart = t  # local t and not account for scr refresh
        F15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F15, 'tStartRefresh')  # time at next scr refresh
        F15.setAutoDraw(True)
    
    # *F16* updates
    if F16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F16.frameNStart = frameN  # exact frame index
        F16.tStart = t  # local t and not account for scr refresh
        F16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F16, 'tStartRefresh')  # time at next scr refresh
        F16.setAutoDraw(True)
    
    # *F17* updates
    if F17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F17.frameNStart = frameN  # exact frame index
        F17.tStart = t  # local t and not account for scr refresh
        F17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F17, 'tStartRefresh')  # time at next scr refresh
        F17.setAutoDraw(True)
    
    # *F18* updates
    if F18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F18.frameNStart = frameN  # exact frame index
        F18.tStart = t  # local t and not account for scr refresh
        F18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F18, 'tStartRefresh')  # time at next scr refresh
        F18.setAutoDraw(True)
    
    # *F19* updates
    if F19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F19.frameNStart = frameN  # exact frame index
        F19.tStart = t  # local t and not account for scr refresh
        F19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F19, 'tStartRefresh')  # time at next scr refresh
        F19.setAutoDraw(True)
    
    # *F20* updates
    if F20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        F20.frameNStart = frameN  # exact frame index
        F20.tStart = t  # local t and not account for scr refresh
        F20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(F20, 'tStartRefresh')  # time at next scr refresh
        F20.setAutoDraw(True)
    # *selAmouse* updates
    if selAmouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        selAmouse.frameNStart = frameN  # exact frame index
        selAmouse.tStart = t  # local t and not account for scr refresh
        selAmouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(selAmouse, 'tStartRefresh')  # time at next scr refresh
        selAmouse.status = STARTED
        prevButtonState = selAmouse.getPressed()  # if button is down already this ISN'T a new click
    if selAmouse.status == STARTED:
        if bool(len(selAmouse.clicked_name) == 5):
            # keep track of stop time/frame for later
            selAmouse.tStop = t  # not accounting for scr refresh
            selAmouse.frameNStop = frameN  # exact frame index
            win.timeOnFlip(selAmouse, 'tStopRefresh')  # time at next scr refresh
            selAmouse.status = FINISHED
    if selAmouse.status == STARTED:  # only update if started and not finished!
        buttons = selAmouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([F01, F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20])
                    clickableList = [F01, F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20]
                except:
                    clickableList = [[F01, F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20]]
                for obj in clickableList:
                    if obj.contains(selAmouse):
                        gotValidClick = True
                        selAmouse.clicked_name.append(obj.name)
                x, y = selAmouse.getPos()
                selAmouse.x.append(x)
                selAmouse.y.append(y)
                buttons = selAmouse.getPressed()
                selAmouse.leftButton.append(buttons[0])
                selAmouse.midButton.append(buttons[1])
                selAmouse.rightButton.append(buttons[2])
                selAmouse.time.append(globalClock.getTime())
    
    # *femCount* updates
    if femCount.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        femCount.frameNStart = frameN  # exact frame index
        femCount.tStart = t  # local t and not account for scr refresh
        femCount.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(femCount, 'tStartRefresh')  # time at next scr refresh
        femCount.setAutoDraw(True)
    if femCount.status == STARTED:  # only update if drawing
        femCount.setText(female_count, log=False)
    
    # *maleCount* updates
    if maleCount.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        maleCount.frameNStart = frameN  # exact frame index
        maleCount.tStart = t  # local t and not account for scr refresh
        maleCount.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(maleCount, 'tStartRefresh')  # time at next scr refresh
        maleCount.setAutoDraw(True)
    if maleCount.status == STARTED:  # only update if drawing
        maleCount.setText(male_count, log=False)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and len(selAmouse.clicked_name) == 5:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in selAComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "selA"-------
for thisComponent in selAComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
for selectedPic in selectedPhotos:
    selectedPic.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('selAmouse.x', selAmouse.x)
thisExp.addData('selAmouse.y', selAmouse.y)
thisExp.addData('selAmouse.leftButton', selAmouse.leftButton)
thisExp.addData('selAmouse.midButton', selAmouse.midButton)
thisExp.addData('selAmouse.rightButton', selAmouse.rightButton)
thisExp.addData('selAmouse.time', selAmouse.time)
thisExp.addData('selAmouse.clicked_name', selAmouse.clicked_name)
thisExp.nextEntry()
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "selA" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instrB"-------
continueRoutine = True
# update component parameters for each repeat
instBkey.keys = []
instBkey.rt = []
_instBkey_allKeys = []
# keep track of which components have finished
instrBComponents = [instBtxt, instBkey]
for thisComponent in instrBComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrBClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrB"-------
while continueRoutine:
    # get current time
    t = instrBClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrBClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instBtxt* updates
    if instBtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instBtxt.frameNStart = frameN  # exact frame index
        instBtxt.tStart = t  # local t and not account for scr refresh
        instBtxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instBtxt, 'tStartRefresh')  # time at next scr refresh
        instBtxt.setAutoDraw(True)
    
    # *instBkey* updates
    waitOnFlip = False
    if instBkey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instBkey.frameNStart = frameN  # exact frame index
        instBkey.tStart = t  # local t and not account for scr refresh
        instBkey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instBkey, 'tStartRefresh')  # time at next scr refresh
        instBkey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instBkey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instBkey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instBkey.status == STARTED and not waitOnFlip:
        theseKeys = instBkey.getKeys(keyList=['space'], waitRelease=False)
        _instBkey_allKeys.extend(theseKeys)
        if len(_instBkey_allKeys):
            instBkey.keys = _instBkey_allKeys[-1].name  # just the last key pressed
            instBkey.rt = _instBkey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrBComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrB"-------
for thisComponent in instrBComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instBtxt.started', instBtxt.tStartRefresh)
thisExp.addData('instBtxt.stopped', instBtxt.tStopRefresh)
# the Routine "instrB" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "selB"-------
continueRoutine = True
# update component parameters for each repeat
selBkey.keys = []
selBkey.rt = []
_selBkey_allKeys = []
# setup some python lists for storing info about the selBmouse
selBmouse.x = []
selBmouse.y = []
selBmouse.leftButton = []
selBmouse.midButton = []
selBmouse.rightButton = []
selBmouse.time = []
selBmouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
selBComponents = [selBtxt, selBkey, selBmouse, prof1, prof1txt, prof2, prof2txt, prof3, prof3txt, prof4, prof4txt, prof5, prof5txt]
for thisComponent in selBComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
selBClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "selB"-------
while continueRoutine:
    # get current time
    t = selBClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=selBClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    for stimulus in [prof1, prof2, prof3, prof4, prof5]:
        if selBmouse.isPressedIn(stimulus):
            stimulus.fillColor ='black'
    
    if expInfo['gender']=='Male' and expInfo['age'] == '9-11':
        prof1_txt = 'Michael \nPlays soccer \nLikes playing Wii bowling \nWants to be a policeman'
    elif expInfo['gender']=='Male' and expInfo['age'] == '12-14':
        prof1_txt = 'Jake \nGood at skateboarding and dirtbikes \nLikes hanging out with friends \nWants to be a competitive skateboarder'
    elif expInfo['gender']=='Female' and expInfo['age'] == '9-11':
        prof1_txt = 'Cara \nBelongs to the art club \nLikes making jewelry \nWants to be a teacher'
    elif expInfo['gender']=='Female' and expInfo['age'] == '12-14':
        prof1_txt = 'Erin \nCompetes in Jazz competitions \nLikes talking on the phone  \nWants to be a dancer'
    
    if expInfo['gender']=='Male' and expInfo['age'] == '9-11':
        prof2_txt = 'Brandon\nParticipates in the math team\nLikes karate\nWants to be a doctor'
    elif expInfo['gender']=='Male' and expInfo['age'] == '12-14':
        prof2_txt = 'Jesse\nWon first place at school art show\nLikes to play video games\nWants to be a photographer'
    elif expInfo['gender']=='Female' and expInfo['age'] == '9-11':
        prof2_txt = 'Tiffany\nPlays the clarinet\nLikes playing with her two dogs\nWants to be a travel agent'
    elif expInfo['gender']=='Female' and expInfo['age'] == '12-14':
        prof2_txt = 'Megan\nSings in the choir\nLikes babysitting\nWants to be a doctor' 
    
    if expInfo['gender']=='Male' and expInfo['age'] == '9-11':
        prof3_txt = 'Luke\nPlays football\nLikes building model airplanes\nWants to be a pilot'
    elif expInfo['gender']=='Male' and expInfo['age'] == '12-14':
        prof3_txt = 'Greg\nPlays football and baseball\nLikes playing sports with friends\nWants to be a professional football player'
    elif expInfo['gender']=='Female' and expInfo['age'] == '9-11':
        prof3_txt = 'Julie\nPlays soccer\nLikes dancing\nWants to be an actress'
    elif expInfo['gender']=='Female' and expInfo['age'] == '12-14':
        prof3_txt = 'Serena\nPlays flute in school band\nLoves animals\nWants to be a scientist'
    
    if expInfo['gender']=='Male' and expInfo['age'] == '9-11':
        prof4_txt = 'Erik\nBelongs to environmental club\nLikes drawing\nWants to be a scientist'
    elif expInfo['gender']=='Male' and expInfo['age'] == '12-14':
        prof4_txt = 'Dan\nWon first place at science fair\nLikes biking and hiking\nWants to be a park ranger' 
    elif expInfo['gender']=='Female' and expInfo['age'] == '9-11':
        prof4_txt = 'Stephanie\nParticipates in cheerleading\nLikes baking cookies\nWants to be a skater'
    elif expInfo['gender']=='Female' and expInfo['age'] == '12-14':
        prof4_txt = 'Molly\nActs in community plays\nLikes shopping in the mall with friends\nWants to work with computers'
    
    if expInfo['gender']=='Male' and expInfo['age'] == '9-11':
        prof5_txt = 'Joey\nPlays on an ice hockey team\nLikes reading comic books\nWants to be a hockey player'
    elif expInfo['gender']=='Male' and expInfo['age'] == '12-14':
        prof5_txt = 'Josh\nPresident of student council\nLikes to hang out with friends\nWants to be a lawyer'
    elif expInfo['gender']=='Female' and expInfo['age'] == '9-11':
        prof5_txt = 'Shawna\nParticipates in girl scouts\nLikes acting and singing\nWants to be a doctor'
    elif expInfo['gender']=='Female' and expInfo['age'] == '12-14':
        prof5_txt = 'Kathy\nWon poetry writing contest\nLikes reading\nWants to be a writer'
    
    # *selBtxt* updates
    if selBtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        selBtxt.frameNStart = frameN  # exact frame index
        selBtxt.tStart = t  # local t and not account for scr refresh
        selBtxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(selBtxt, 'tStartRefresh')  # time at next scr refresh
        selBtxt.setAutoDraw(True)
    
    # *selBkey* updates
    waitOnFlip = False
    if selBkey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        selBkey.frameNStart = frameN  # exact frame index
        selBkey.tStart = t  # local t and not account for scr refresh
        selBkey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(selBkey, 'tStartRefresh')  # time at next scr refresh
        selBkey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(selBkey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(selBkey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if selBkey.status == STARTED and not waitOnFlip:
        theseKeys = selBkey.getKeys(keyList=['space'], waitRelease=False)
        _selBkey_allKeys.extend(theseKeys)
        if len(_selBkey_allKeys):
            selBkey.keys = _selBkey_allKeys[-1].name  # just the last key pressed
            selBkey.rt = _selBkey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *selBmouse* updates
    if selBmouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        selBmouse.frameNStart = frameN  # exact frame index
        selBmouse.tStart = t  # local t and not account for scr refresh
        selBmouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(selBmouse, 'tStartRefresh')  # time at next scr refresh
        selBmouse.status = STARTED
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if selBmouse.status == STARTED:  # only update if started and not finished!
        buttons = selBmouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([prof1, prof2, prof3, prof4, prof5])
                    clickableList = [prof1, prof2, prof3, prof4, prof5]
                except:
                    clickableList = [[prof1, prof2, prof3, prof4, prof5]]
                for obj in clickableList:
                    if obj.contains(selBmouse):
                        gotValidClick = True
                        selBmouse.clicked_name.append(obj.name)
                x, y = selBmouse.getPos()
                selBmouse.x.append(x)
                selBmouse.y.append(y)
                buttons = selBmouse.getPressed()
                selBmouse.leftButton.append(buttons[0])
                selBmouse.midButton.append(buttons[1])
                selBmouse.rightButton.append(buttons[2])
                selBmouse.time.append(globalClock.getTime())
    
    # *prof1* updates
    if prof1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prof1.frameNStart = frameN  # exact frame index
        prof1.tStart = t  # local t and not account for scr refresh
        prof1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prof1, 'tStartRefresh')  # time at next scr refresh
        prof1.setAutoDraw(True)
    
    # *prof1txt* updates
    if prof1txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prof1txt.frameNStart = frameN  # exact frame index
        prof1txt.tStart = t  # local t and not account for scr refresh
        prof1txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prof1txt, 'tStartRefresh')  # time at next scr refresh
        prof1txt.setAutoDraw(True)
    if prof1txt.status == STARTED:  # only update if drawing
        prof1txt.setText(prof1_txt, log=False)
    
    # *prof2* updates
    if prof2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prof2.frameNStart = frameN  # exact frame index
        prof2.tStart = t  # local t and not account for scr refresh
        prof2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prof2, 'tStartRefresh')  # time at next scr refresh
        prof2.setAutoDraw(True)
    
    # *prof2txt* updates
    if prof2txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prof2txt.frameNStart = frameN  # exact frame index
        prof2txt.tStart = t  # local t and not account for scr refresh
        prof2txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prof2txt, 'tStartRefresh')  # time at next scr refresh
        prof2txt.setAutoDraw(True)
    if prof2txt.status == STARTED:  # only update if drawing
        prof2txt.setText(prof2_txt, log=False)
    
    # *prof3* updates
    if prof3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prof3.frameNStart = frameN  # exact frame index
        prof3.tStart = t  # local t and not account for scr refresh
        prof3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prof3, 'tStartRefresh')  # time at next scr refresh
        prof3.setAutoDraw(True)
    
    # *prof3txt* updates
    if prof3txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prof3txt.frameNStart = frameN  # exact frame index
        prof3txt.tStart = t  # local t and not account for scr refresh
        prof3txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prof3txt, 'tStartRefresh')  # time at next scr refresh
        prof3txt.setAutoDraw(True)
    if prof3txt.status == STARTED:  # only update if drawing
        prof3txt.setText(prof3_txt, log=False)
    
    # *prof4* updates
    if prof4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prof4.frameNStart = frameN  # exact frame index
        prof4.tStart = t  # local t and not account for scr refresh
        prof4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prof4, 'tStartRefresh')  # time at next scr refresh
        prof4.setAutoDraw(True)
    
    # *prof4txt* updates
    if prof4txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prof4txt.frameNStart = frameN  # exact frame index
        prof4txt.tStart = t  # local t and not account for scr refresh
        prof4txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prof4txt, 'tStartRefresh')  # time at next scr refresh
        prof4txt.setAutoDraw(True)
    if prof4txt.status == STARTED:  # only update if drawing
        prof4txt.setText(prof4_txt, log=False)
    
    # *prof5* updates
    if prof5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prof5.frameNStart = frameN  # exact frame index
        prof5.tStart = t  # local t and not account for scr refresh
        prof5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prof5, 'tStartRefresh')  # time at next scr refresh
        prof5.setAutoDraw(True)
    
    # *prof5txt* updates
    if prof5txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prof5txt.frameNStart = frameN  # exact frame index
        prof5txt.tStart = t  # local t and not account for scr refresh
        prof5txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prof5txt, 'tStartRefresh')  # time at next scr refresh
        prof5txt.setAutoDraw(True)
    if prof5txt.status == STARTED:  # only update if drawing
        prof5txt.setText(prof5_txt, log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in selBComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "selB"-------
for thisComponent in selBComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('selBtxt.started', selBtxt.tStartRefresh)
thisExp.addData('selBtxt.stopped', selBtxt.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('selBmouse.x', selBmouse.x)
thisExp.addData('selBmouse.y', selBmouse.y)
thisExp.addData('selBmouse.leftButton', selBmouse.leftButton)
thisExp.addData('selBmouse.midButton', selBmouse.midButton)
thisExp.addData('selBmouse.rightButton', selBmouse.rightButton)
thisExp.addData('selBmouse.time', selBmouse.time)
thisExp.addData('selBmouse.clicked_name', selBmouse.clicked_name)
thisExp.nextEntry()
# the Routine "selB" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Goodbye"-------
continueRoutine = True
# update component parameters for each repeat
byeKey.keys = []
byeKey.rt = []
_byeKey_allKeys = []
# keep track of which components have finished
GoodbyeComponents = [byeTxt, byeKey]
for thisComponent in GoodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Goodbye"-------
while continueRoutine:
    # get current time
    t = GoodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *byeTxt* updates
    if byeTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        byeTxt.frameNStart = frameN  # exact frame index
        byeTxt.tStart = t  # local t and not account for scr refresh
        byeTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(byeTxt, 'tStartRefresh')  # time at next scr refresh
        byeTxt.setAutoDraw(True)
    
    # *byeKey* updates
    waitOnFlip = False
    if byeKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        byeKey.frameNStart = frameN  # exact frame index
        byeKey.tStart = t  # local t and not account for scr refresh
        byeKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(byeKey, 'tStartRefresh')  # time at next scr refresh
        byeKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(byeKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(byeKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if byeKey.status == STARTED and not waitOnFlip:
        theseKeys = byeKey.getKeys(keyList=['space'], waitRelease=False)
        _byeKey_allKeys.extend(theseKeys)
        if len(_byeKey_allKeys):
            byeKey.keys = _byeKey_allKeys[-1].name  # just the last key pressed
            byeKey.rt = _byeKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Goodbye"-------
for thisComponent in GoodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
list1 = selAmouse.clicked_name[0:2]
list2 = selBmouse.clicked_name[0:2]

file=open("Chat Task/"+str(expInfo['participant'])+"/"+str(expInfo['participant'])+"_photos.txt", "w")
for items in list1:
    file.writelines("Experiment Files/Photos/"+expInfo['gender']+"_"+expInfo['age']+"_"+items+".bmp"+'\n')
file.close()

file=open(str(expInfo['participant'])+"_profile1.txt", "w")
if list2[0] == 'prof1':
    file.writelines(prof1_txt)
elif list2[0] == 'prof2':
    file.writelines(prof2_txt)
elif list2[0] == 'prof3':
    file.writelines(prof3_txt)
elif list2[0] == 'prof4':
    file.writelines(prof4_txt)
elif list2[0] == 'prof5':
    file.writelines(prof4_txt)
file.close()

file=open(str(expInfo['participant'])+"_profile2.txt", "w")
if list2[1] == 'prof1':
    file.writelines(prof1_txt)
elif list2[1] == 'prof2':
    file.writelines(prof2_txt)
elif list2[1] == 'prof3':
    file.writelines(prof3_txt)
elif list2[1] == 'prof4':
    file.writelines(prof4_txt)
elif list2[1] == 'prof5':
    file.writelines(prof4_txt)
file.close()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
