#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Mon Jul 19 17:26:51 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')


from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
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
psychopyVersion = '2021.1.4'
expName = 'chat_task_B'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='/Users/kileyyeaman/Documents/chat_task_B.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "baseline1"
baseline1Clock = core.Clock()
key_resp = keyboard.Keyboard()

# Initialize components for Routine "panas1"
panas1Clock = core.Clock()
win.allowStencil = True
form = visual.Form(win=win, name='form',
    items='panas1.xlsx',
    textHeight=0.03,
    randomize=False,
    size=(1.5, 1),
    pos=(0, 0),
    style='light',
    itemPadding=0.05,)
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "welcomeScreen"
welcomeScreenClock = core.Clock()
welcomeTxt = visual.TextStim(win=win, name='welcomeTxt',
    text='WELCOME TO CHAT CHOOSE\n\nWe have matched you with other kids based on the choices you made and the choices the other kids made.\n\nYou will now play the game.\nThe first 3 rounds are with you and two other kids.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyResp = keyboard.Keyboard()

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
instr1txt = visual.TextStim(win=win, name='instr1txt',
    text='WELCOME TO CHAT CHOOSE\n\nFirst, each kid will take turns choosing which of the other two they would rather chat with about certain topics. ',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instr1Key = keyboard.Keyboard()

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
instr2txt = visual.TextStim(win=win, name='instr2txt',
    text='WELCOME TO CHAT CHOOSE\n\nIf it is your turn to choose, please use the left arrow key to choose the person on the left or use the right arrow key to choose the person on the right.\n\nPlease choose as quickly as possible — you have 3 seconds to make a response.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instr2Key = keyboard.Keyboard()

# Initialize components for Routine "instr3"
instr3Clock = core.Clock()
instr3txt = visual.TextStim(win=win, name='instr3txt',
    text='WELCOME TO CHAT CHOOSE\n\nIf it is NOT your turn to choose, please indicate whether the person on the left (press the left arrow key) or the person on the right (press the right arrow key) was chosen on each question. ',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instr3Key = keyboard.Keyboard()

# Initialize components for Routine "standby1"
standby1Clock = core.Clock()
standby1Txt = visual.TextStim(win=win, name='standby1Txt',
    text='STANDBY MODE\n\nYou can relax.\n\n(Press SPACEBAR to continue). ',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyStandby1 = keyboard.Keyboard()

# Initialize components for Routine "panas2"
panas2Clock = core.Clock()
win.allowStencil = True
form_2 = visual.Form(win=win, name='form_2',
    items='panas1.xlsx',
    textHeight=0.03,
    randomize=False,
    size=(1.5,1),
    pos=(0, 0),
    style='light',
    itemPadding=0.05,)
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "postChat1"
postChat1Clock = core.Clock()
win.allowStencil = True
form_3 = visual.Form(win=win, name='form_3',
    items='postChat1.xlsx',
    textHeight=0.03,
    randomize=False,
    size=(1.5,1),
    pos=(0, 0),
    style='light',
    itemPadding=0.05,)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "goodbye"
goodbyeClock = core.Clock()
goodbye1txt = visual.TextStim(win=win, name='goodbye1txt',
    text='Goodbye!',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "baseline1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
baseline1Components = [key_resp]
for thisComponent in baseline1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
baseline1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "baseline1"-------
while continueRoutine:
    # get current time
    t = baseline1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=baseline1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    for thisComponent in baseline1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "baseline1"-------
for thisComponent in baseline1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "baseline1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "panas1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
panas1Components = [form, key_resp_5]
for thisComponent in panas1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
panas1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "panas1"-------
while continueRoutine:
    # get current time
    t = panas1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=panas1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *form* updates
    if form.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        form.frameNStart = frameN  # exact frame index
        form.tStart = t  # local t and not account for scr refresh
        form.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form, 'tStartRefresh')  # time at next scr refresh
        form.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in panas1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "panas1"-------
for thisComponent in panas1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
form.addDataToExp(thisExp, 'columns')
form.autodraw = False
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "panas1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
keyResp.keys = []
keyResp.rt = []
_keyResp_allKeys = []
# keep track of which components have finished
welcomeScreenComponents = [welcomeTxt, keyResp]
for thisComponent in welcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcomeScreen"-------
while continueRoutine:
    # get current time
    t = welcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeTxt* updates
    if welcomeTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeTxt.frameNStart = frameN  # exact frame index
        welcomeTxt.tStart = t  # local t and not account for scr refresh
        welcomeTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeTxt, 'tStartRefresh')  # time at next scr refresh
        welcomeTxt.setAutoDraw(True)
    
    # *keyResp* updates
    if keyResp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyResp.frameNStart = frameN  # exact frame index
        keyResp.tStart = t  # local t and not account for scr refresh
        keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
        keyResp.status = STARTED
        # keyboard checking is just starting
        keyResp.clock.reset()  # now t=0
    if keyResp.status == STARTED:
        theseKeys = keyResp.getKeys(keyList=['space'], waitRelease=False)
        _keyResp_allKeys.extend(theseKeys)
        if len(_keyResp_allKeys):
            keyResp.keys = _keyResp_allKeys[-1].name  # just the last key pressed
            keyResp.rt = _keyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcomeScreen"-------
for thisComponent in welcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcomeTxt.started', welcomeTxt.tStartRefresh)
thisExp.addData('welcomeTxt.stopped', welcomeTxt.tStopRefresh)
# the Routine "welcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr1"-------
continueRoutine = True
# update component parameters for each repeat
instr1Key.keys = []
instr1Key.rt = []
_instr1Key_allKeys = []
# keep track of which components have finished
instr1Components = [instr1txt, instr1Key]
for thisComponent in instr1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr1"-------
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1txt* updates
    if instr1txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1txt.frameNStart = frameN  # exact frame index
        instr1txt.tStart = t  # local t and not account for scr refresh
        instr1txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1txt, 'tStartRefresh')  # time at next scr refresh
        instr1txt.setAutoDraw(True)
    
    # *instr1Key* updates
    if instr1Key.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1Key.frameNStart = frameN  # exact frame index
        instr1Key.tStart = t  # local t and not account for scr refresh
        instr1Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1Key, 'tStartRefresh')  # time at next scr refresh
        instr1Key.status = STARTED
        # keyboard checking is just starting
        instr1Key.clock.reset()  # now t=0
    if instr1Key.status == STARTED:
        theseKeys = instr1Key.getKeys(keyList=['space'], waitRelease=False)
        _instr1Key_allKeys.extend(theseKeys)
        if len(_instr1Key_allKeys):
            instr1Key.keys = _instr1Key_allKeys[-1].name  # just the last key pressed
            instr1Key.rt = _instr1Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr1txt.started', instr1txt.tStartRefresh)
thisExp.addData('instr1txt.stopped', instr1txt.tStopRefresh)
# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr2"-------
continueRoutine = True
# update component parameters for each repeat
instr2Key.keys = []
instr2Key.rt = []
_instr2Key_allKeys = []
# keep track of which components have finished
instr2Components = [instr2txt, instr2Key]
for thisComponent in instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr2"-------
while continueRoutine:
    # get current time
    t = instr2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr2txt* updates
    if instr2txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr2txt.frameNStart = frameN  # exact frame index
        instr2txt.tStart = t  # local t and not account for scr refresh
        instr2txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr2txt, 'tStartRefresh')  # time at next scr refresh
        instr2txt.setAutoDraw(True)
    
    # *instr2Key* updates
    waitOnFlip = False
    if instr2Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr2Key.frameNStart = frameN  # exact frame index
        instr2Key.tStart = t  # local t and not account for scr refresh
        instr2Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr2Key, 'tStartRefresh')  # time at next scr refresh
        instr2Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr2Key.clock.reset)  # t=0 on next screen flip
    if instr2Key.status == STARTED and not waitOnFlip:
        theseKeys = instr2Key.getKeys(keyList=['space'], waitRelease=False)
        _instr2Key_allKeys.extend(theseKeys)
        if len(_instr2Key_allKeys):
            instr2Key.keys = _instr2Key_allKeys[-1].name  # just the last key pressed
            instr2Key.rt = _instr2Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr2"-------
for thisComponent in instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr3"-------
continueRoutine = True
# update component parameters for each repeat
instr3Key.keys = []
instr3Key.rt = []
_instr3Key_allKeys = []
# keep track of which components have finished
instr3Components = [instr3txt, instr3Key]
for thisComponent in instr3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr3"-------
while continueRoutine:
    # get current time
    t = instr3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr3txt* updates
    if instr3txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr3txt.frameNStart = frameN  # exact frame index
        instr3txt.tStart = t  # local t and not account for scr refresh
        instr3txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr3txt, 'tStartRefresh')  # time at next scr refresh
        instr3txt.setAutoDraw(True)
    
    # *instr3Key* updates
    waitOnFlip = False
    if instr3Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr3Key.frameNStart = frameN  # exact frame index
        instr3Key.tStart = t  # local t and not account for scr refresh
        instr3Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr3Key, 'tStartRefresh')  # time at next scr refresh
        instr3Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr3Key.clock.reset)  # t=0 on next screen flip
    if instr3Key.status == STARTED and not waitOnFlip:
        theseKeys = instr3Key.getKeys(keyList=['space'], waitRelease=False)
        _instr3Key_allKeys.extend(theseKeys)
        if len(_instr3Key_allKeys):
            instr3Key.keys = _instr3Key_allKeys[-1].name  # just the last key pressed
            instr3Key.rt = _instr3Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr3"-------
for thisComponent in instr3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "standby1"-------
continueRoutine = True
# update component parameters for each repeat
keyStandby1.keys = []
keyStandby1.rt = []
_keyStandby1_allKeys = []
# keep track of which components have finished
standby1Components = [standby1Txt, keyStandby1]
for thisComponent in standby1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
standby1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "standby1"-------
while continueRoutine:
    # get current time
    t = standby1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=standby1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *standby1Txt* updates
    if standby1Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        standby1Txt.frameNStart = frameN  # exact frame index
        standby1Txt.tStart = t  # local t and not account for scr refresh
        standby1Txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(standby1Txt, 'tStartRefresh')  # time at next scr refresh
        standby1Txt.setAutoDraw(True)
    
    # *keyStandby1* updates
    waitOnFlip = False
    if keyStandby1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyStandby1.frameNStart = frameN  # exact frame index
        keyStandby1.tStart = t  # local t and not account for scr refresh
        keyStandby1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyStandby1, 'tStartRefresh')  # time at next scr refresh
        keyStandby1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyStandby1.clock.reset)  # t=0 on next screen flip
    if keyStandby1.status == STARTED and not waitOnFlip:
        theseKeys = keyStandby1.getKeys(keyList=['space'], waitRelease=False)
        _keyStandby1_allKeys.extend(theseKeys)
        if len(_keyStandby1_allKeys):
            keyStandby1.keys = _keyStandby1_allKeys[-1].name  # just the last key pressed
            keyStandby1.rt = _keyStandby1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in standby1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "standby1"-------
for thisComponent in standby1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "standby1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "panas2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
panas2Components = [form_2, key_resp_3]
for thisComponent in panas2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
panas2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "panas2"-------
while continueRoutine:
    # get current time
    t = panas2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=panas2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *form_2* updates
    if form_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        form_2.frameNStart = frameN  # exact frame index
        form_2.tStart = t  # local t and not account for scr refresh
        form_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form_2, 'tStartRefresh')  # time at next scr refresh
        form_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in panas2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "panas2"-------
for thisComponent in panas2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
form_2.addDataToExp(thisExp, 'rows')
form_2.autodraw = False
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "panas2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "postChat1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
postChat1Components = [form_3, key_resp_2]
for thisComponent in postChat1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
postChat1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "postChat1"-------
while continueRoutine:
    # get current time
    t = postChat1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=postChat1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *form_3* updates
    if form_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        form_3.frameNStart = frameN  # exact frame index
        form_3.tStart = t  # local t and not account for scr refresh
        form_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form_3, 'tStartRefresh')  # time at next scr refresh
        form_3.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postChat1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "postChat1"-------
for thisComponent in postChat1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
form_3.addDataToExp(thisExp, 'rows')
form_3.autodraw = False
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "postChat1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "goodbye"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
goodbyeComponents = [goodbye1txt, key_resp_4]
for thisComponent in goodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
goodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "goodbye"-------
while continueRoutine:
    # get current time
    t = goodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=goodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *goodbye1txt* updates
    if goodbye1txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goodbye1txt.frameNStart = frameN  # exact frame index
        goodbye1txt.tStart = t  # local t and not account for scr refresh
        goodbye1txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goodbye1txt, 'tStartRefresh')  # time at next scr refresh
        goodbye1txt.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "goodbye"-------
for thisComponent in goodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('goodbye1txt.started', goodbye1txt.tStartRefresh)
thisExp.addData('goodbye1txt.stopped', goodbye1txt.tStopRefresh)
# the Routine "goodbye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
