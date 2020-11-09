#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on November 09, 2020, at 12:43
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2020.2')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.5'
expName = 'FST_clear'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
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
    originPath='C:\\Users\\heard\\Documents\\GitHub\\FST_PsychoPy\\FST_v1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1024, 640], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
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

# Initialize components for Routine "welcome_screen"
welcome_screenClock = core.Clock()
text_welcome = visual.TextStim(win=win, name='text_welcome',
    text='Thank you for participating in our experiment!\n\nIn this experiment, you will listen to some sentences and will be asked a question about each sentence. \n\nPlease make sure you are wearing headphones. \n\n',
    font='Arial',
    pos=(0, .1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_welcome2 = visual.TextStim(win=win, name='text_welcome2',
    text='\n\n\n\n\n\n\n\nPress the space bar to listen to an example of a sentence.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_welcome = keyboard.Keyboard()

# Initialize components for Routine "tutorial_stim"
tutorial_stimClock = core.Clock()
tuto_sent = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='tuto_sent')
tuto_sent.setVolume(1)
text_inst1 = visual.TextStim(win=win, name='text_inst1',
    text='default text',
    font='Arial',
    pos=(0, .15), height=0.05, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_inst2 = visual.TextStim(win=win, name='text_inst2',
    text='default text',
    font='Arial',
    pos=(0, -.05), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_inst_cont1 = visual.TextStim(win=win, name='text_inst_cont1',
    text='Press the space bar to continue.',
    font='Arial',
    pos=(0, -.2), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_tuto = keyboard.Keyboard()

# Initialize components for Routine "tutorial_instr"
tutorial_instrClock = core.Clock()
text_inst3 = visual.TextStim(win=win, name='text_inst3',
    text='default text',
    font='Arial',
    pos=(0, .1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_inst_cont2 = visual.TextStim(win=win, name='text_inst_cont2',
    text='Press the space bar to continue.',
    font='Arial',
    pos=(0, -.15), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_inst = keyboard.Keyboard()

# Initialize components for Routine "practice_instr"
practice_instrClock = core.Clock()
text_prac1 = visual.TextStim(win=win, name='text_prac1',
    text="Let's practice. For the rest of the experiment, please stop adjusting the volume on your computer.\n\nPress the LEFT key if the gender of performing action is MALE.\nPress the RIGHT key if the gender of performing action is FEMALE.\n\nYou have 5 seconds to respond each trial.\nDuring the practice, you will be told if you were right or wrong.",
    font='Arial',
    pos=(0, .13), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_prac2 = visual.TextStim(win=win, name='text_prac2',
    text='Press the space bar to begin!',
    font='Arial',
    pos=(0, -.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_prac = keyboard.Keyboard()

# Initialize components for Routine "stim_resp"
stim_respClock = core.Clock()
msg='doh!'#if this comes up we forgot to update the msg!
trial_count=0
stim_present = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stim_present')
stim_present.setVolume(1)
text_qm = visual.TextStim(win=win, name='text_qm',
    text='MALE <',
    font='Arial',
    pos=(-.25, 0), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_qf = visual.TextStim(win=win, name='text_qf',
    text='> FEMALE',
    font='Arial',
    pos=(.29, 0), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',units='height', 
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "prac_feedback"
prac_feedbackClock = core.Clock()
text_feedback = visual.TextStim(win=win, name='text_feedback',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_exp_cont = visual.TextStim(win=win, name='text_exp_cont',
    text='Press the space bar to continue.',
    font='Arial',
    pos=(0, -.2), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_exp_cont = keyboard.Keyboard()

# Initialize components for Routine "main_instr"
main_instrClock = core.Clock()
text_main1 = visual.TextStim(win=win, name='text_main1',
    text="Now let's move onto the real experiment.\n\nPress the LEFT key if the gender of performing action is MALE.\nPress the RIGHT key if the gender of performing action is FEMALE.\n\nYou have 5 seconds to respond each trial.\nYou will not be told if you are right or wrong after each sentence.",
    font='Arial',
    pos=(0, .13), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_main2 = visual.TextStim(win=win, name='text_main2',
    text='Press the space bar to begin!',
    font='Arial',
    pos=(0, -.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_main = keyboard.Keyboard()

# Initialize components for Routine "stim_resp"
stim_respClock = core.Clock()
msg='doh!'#if this comes up we forgot to update the msg!
trial_count=0
stim_present = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stim_present')
stim_present.setVolume(1)
text_qm = visual.TextStim(win=win, name='text_qm',
    text='MALE <',
    font='Arial',
    pos=(-.25, 0), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_qf = visual.TextStim(win=win, name='text_qf',
    text='> FEMALE',
    font='Arial',
    pos=(.29, 0), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',units='height', 
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "main_feedback"
main_feedbackClock = core.Clock()
text_feedback_2 = visual.TextStim(win=win, name='text_feedback_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_exp_cont_2 = visual.TextStim(win=win, name='text_exp_cont_2',
    text='Press the space bar to continue.',
    font='Arial',
    pos=(0, -.2), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_exp_cont_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome_screen"-------
continueRoutine = True
# update component parameters for each repeat
key_welcome.keys = []
key_welcome.rt = []
_key_welcome_allKeys = []
# keep track of which components have finished
welcome_screenComponents = [text_welcome, text_welcome2, key_welcome]
for thisComponent in welcome_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcome_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome_screen"-------
while continueRoutine:
    # get current time
    t = welcome_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcome_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_welcome* updates
    if text_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_welcome.frameNStart = frameN  # exact frame index
        text_welcome.tStart = t  # local t and not account for scr refresh
        text_welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_welcome, 'tStartRefresh')  # time at next scr refresh
        text_welcome.setAutoDraw(True)
    
    # *text_welcome2* updates
    if text_welcome2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        text_welcome2.frameNStart = frameN  # exact frame index
        text_welcome2.tStart = t  # local t and not account for scr refresh
        text_welcome2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_welcome2, 'tStartRefresh')  # time at next scr refresh
        text_welcome2.setAutoDraw(True)
    
    # *key_welcome* updates
    waitOnFlip = False
    if key_welcome.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_welcome.frameNStart = frameN  # exact frame index
        key_welcome.tStart = t  # local t and not account for scr refresh
        key_welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_welcome, 'tStartRefresh')  # time at next scr refresh
        key_welcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_welcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_welcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_welcome.status == STARTED and not waitOnFlip:
        theseKeys = key_welcome.getKeys(keyList=['space'], waitRelease=False)
        _key_welcome_allKeys.extend(theseKeys)
        if len(_key_welcome_allKeys):
            key_welcome.keys = _key_welcome_allKeys[0].name  # just the first key pressed
            key_welcome.rt = _key_welcome_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_screen"-------
for thisComponent in welcome_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_welcome.keys in ['', [], None]:  # No response was made
    key_welcome.keys = None
thisExp.addData('key_welcome.keys',key_welcome.keys)
if key_welcome.keys != None:  # we had a response
    thisExp.addData('key_welcome.rt', key_welcome.rt)
thisExp.nextEntry()
# the Routine "welcome_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
tutorial_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Instruction.xlsx'),
    seed=None, name='tutorial_trials')
thisExp.addLoop(tutorial_trials)  # add the loop to the experiment
thisTutorial_trial = tutorial_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTutorial_trial.rgb)
if thisTutorial_trial != None:
    for paramName in thisTutorial_trial:
        exec('{} = thisTutorial_trial[paramName]'.format(paramName))

for thisTutorial_trial in tutorial_trials:
    currentLoop = tutorial_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTutorial_trial.rgb)
    if thisTutorial_trial != None:
        for paramName in thisTutorial_trial:
            exec('{} = thisTutorial_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "tutorial_stim"-------
    continueRoutine = True
    # update component parameters for each repeat
    tuto_sent.setSound(sent_stim, secs=2.5, hamming=True)
    tuto_sent.setVolume(1, log=False)
    text_inst1.setText(inst1)
    text_inst2.setText(inst2)
    key_tuto.keys = []
    key_tuto.rt = []
    _key_tuto_allKeys = []
    # keep track of which components have finished
    tutorial_stimComponents = [tuto_sent, text_inst1, text_inst2, text_inst_cont1, key_tuto]
    for thisComponent in tutorial_stimComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    tutorial_stimClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "tutorial_stim"-------
    while continueRoutine:
        # get current time
        t = tutorial_stimClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=tutorial_stimClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop tuto_sent
        if tuto_sent.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tuto_sent.frameNStart = frameN  # exact frame index
            tuto_sent.tStart = t  # local t and not account for scr refresh
            tuto_sent.tStartRefresh = tThisFlipGlobal  # on global time
            tuto_sent.play(when=win)  # sync with win flip
        if tuto_sent.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tuto_sent.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                tuto_sent.tStop = t  # not accounting for scr refresh
                tuto_sent.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tuto_sent, 'tStopRefresh')  # time at next scr refresh
                tuto_sent.stop()
        
        # *text_inst1* updates
        if text_inst1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_inst1.frameNStart = frameN  # exact frame index
            text_inst1.tStart = t  # local t and not account for scr refresh
            text_inst1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_inst1, 'tStartRefresh')  # time at next scr refresh
            text_inst1.setAutoDraw(True)
        
        # *text_inst2* updates
        if text_inst2.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            text_inst2.frameNStart = frameN  # exact frame index
            text_inst2.tStart = t  # local t and not account for scr refresh
            text_inst2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_inst2, 'tStartRefresh')  # time at next scr refresh
            text_inst2.setAutoDraw(True)
        
        # *text_inst_cont1* updates
        if text_inst_cont1.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            text_inst_cont1.frameNStart = frameN  # exact frame index
            text_inst_cont1.tStart = t  # local t and not account for scr refresh
            text_inst_cont1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_inst_cont1, 'tStartRefresh')  # time at next scr refresh
            text_inst_cont1.setAutoDraw(True)
        
        # *key_tuto* updates
        waitOnFlip = False
        if key_tuto.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            key_tuto.frameNStart = frameN  # exact frame index
            key_tuto.tStart = t  # local t and not account for scr refresh
            key_tuto.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_tuto, 'tStartRefresh')  # time at next scr refresh
            key_tuto.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_tuto.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_tuto.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_tuto.status == STARTED and not waitOnFlip:
            theseKeys = key_tuto.getKeys(keyList=['space'], waitRelease=False)
            _key_tuto_allKeys.extend(theseKeys)
            if len(_key_tuto_allKeys):
                key_tuto.keys = _key_tuto_allKeys[-1].name  # just the last key pressed
                key_tuto.rt = _key_tuto_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tutorial_stimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "tutorial_stim"-------
    for thisComponent in tutorial_stimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    tuto_sent.stop()  # ensure sound has stopped at end of routine
    # check responses
    if key_tuto.keys in ['', [], None]:  # No response was made
        key_tuto.keys = None
    tutorial_trials.addData('key_tuto.keys',key_tuto.keys)
    if key_tuto.keys != None:  # we had a response
        tutorial_trials.addData('key_tuto.rt', key_tuto.rt)
    # the Routine "tutorial_stim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "tutorial_instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_inst3.setText(inst3)
    key_inst.keys = []
    key_inst.rt = []
    _key_inst_allKeys = []
    # keep track of which components have finished
    tutorial_instrComponents = [text_inst3, text_inst_cont2, key_inst]
    for thisComponent in tutorial_instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    tutorial_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "tutorial_instr"-------
    while continueRoutine:
        # get current time
        t = tutorial_instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=tutorial_instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_inst3* updates
        if text_inst3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_inst3.frameNStart = frameN  # exact frame index
            text_inst3.tStart = t  # local t and not account for scr refresh
            text_inst3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_inst3, 'tStartRefresh')  # time at next scr refresh
            text_inst3.setAutoDraw(True)
        
        # *text_inst_cont2* updates
        if text_inst_cont2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            text_inst_cont2.frameNStart = frameN  # exact frame index
            text_inst_cont2.tStart = t  # local t and not account for scr refresh
            text_inst_cont2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_inst_cont2, 'tStartRefresh')  # time at next scr refresh
            text_inst_cont2.setAutoDraw(True)
        
        # *key_inst* updates
        waitOnFlip = False
        if key_inst.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            key_inst.frameNStart = frameN  # exact frame index
            key_inst.tStart = t  # local t and not account for scr refresh
            key_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_inst, 'tStartRefresh')  # time at next scr refresh
            key_inst.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_inst.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_inst.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_inst.status == STARTED and not waitOnFlip:
            theseKeys = key_inst.getKeys(keyList=['space'], waitRelease=False)
            _key_inst_allKeys.extend(theseKeys)
            if len(_key_inst_allKeys):
                key_inst.keys = _key_inst_allKeys[-1].name  # just the last key pressed
                key_inst.rt = _key_inst_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tutorial_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "tutorial_instr"-------
    for thisComponent in tutorial_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_inst.keys in ['', [], None]:  # No response was made
        key_inst.keys = None
    tutorial_trials.addData('key_inst.keys',key_inst.keys)
    if key_inst.keys != None:  # we had a response
        tutorial_trials.addData('key_inst.rt', key_inst.rt)
    # the Routine "tutorial_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'tutorial_trials'


# ------Prepare to start Routine "practice_instr"-------
continueRoutine = True
# update component parameters for each repeat
key_prac.keys = []
key_prac.rt = []
_key_prac_allKeys = []
# keep track of which components have finished
practice_instrComponents = [text_prac1, text_prac2, key_prac]
for thisComponent in practice_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_instr"-------
while continueRoutine:
    # get current time
    t = practice_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_prac1* updates
    if text_prac1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_prac1.frameNStart = frameN  # exact frame index
        text_prac1.tStart = t  # local t and not account for scr refresh
        text_prac1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_prac1, 'tStartRefresh')  # time at next scr refresh
        text_prac1.setAutoDraw(True)
    
    # *text_prac2* updates
    if text_prac2.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        text_prac2.frameNStart = frameN  # exact frame index
        text_prac2.tStart = t  # local t and not account for scr refresh
        text_prac2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_prac2, 'tStartRefresh')  # time at next scr refresh
        text_prac2.setAutoDraw(True)
    
    # *key_prac* updates
    waitOnFlip = False
    if key_prac.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        key_prac.frameNStart = frameN  # exact frame index
        key_prac.tStart = t  # local t and not account for scr refresh
        key_prac.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_prac, 'tStartRefresh')  # time at next scr refresh
        key_prac.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_prac.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_prac.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_prac.status == STARTED and not waitOnFlip:
        theseKeys = key_prac.getKeys(keyList=['space'], waitRelease=False)
        _key_prac_allKeys.extend(theseKeys)
        if len(_key_prac_allKeys):
            key_prac.keys = _key_prac_allKeys[-1].name  # just the last key pressed
            key_prac.rt = _key_prac_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_instr"-------
for thisComponent in practice_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_prac.keys in ['', [], None]:  # No response was made
    key_prac.keys = None
thisExp.addData('key_prac.keys',key_prac.keys)
if key_prac.keys != None:  # we had a response
    thisExp.addData('key_prac.rt', key_prac.rt)
thisExp.nextEntry()
# the Routine "practice_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice.xlsx'),
    seed=None, name='practice_trials')
thisExp.addLoop(practice_trials)  # add the loop to the experiment
thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
if thisPractice_trial != None:
    for paramName in thisPractice_trial:
        exec('{} = thisPractice_trial[paramName]'.format(paramName))

for thisPractice_trial in practice_trials:
    currentLoop = practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            exec('{} = thisPractice_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "stim_resp"-------
    continueRoutine = True
    routineTimer.add(8.000000)
    # update component parameters for each repeat
    stim_present.setSound(sent_stim, secs=2.5, hamming=True)
    stim_present.setVolume(1, log=False)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    stim_respComponents = [stim_present, text_qm, text_qf, fixation, key_resp]
    for thisComponent in stim_respComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stim_respClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stim_resp"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stim_respClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stim_respClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop stim_present
        if stim_present.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stim_present.frameNStart = frameN  # exact frame index
            stim_present.tStart = t  # local t and not account for scr refresh
            stim_present.tStartRefresh = tThisFlipGlobal  # on global time
            stim_present.play(when=win)  # sync with win flip
        if stim_present.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim_present.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                stim_present.tStop = t  # not accounting for scr refresh
                stim_present.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stim_present, 'tStopRefresh')  # time at next scr refresh
                stim_present.stop()
        
        # *text_qm* updates
        if text_qm.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            text_qm.frameNStart = frameN  # exact frame index
            text_qm.tStart = t  # local t and not account for scr refresh
            text_qm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_qm, 'tStartRefresh')  # time at next scr refresh
            text_qm.setAutoDraw(True)
        if text_qm.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_qm.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_qm.tStop = t  # not accounting for scr refresh
                text_qm.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_qm, 'tStopRefresh')  # time at next scr refresh
                text_qm.setAutoDraw(False)
        
        # *text_qf* updates
        if text_qf.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            text_qf.frameNStart = frameN  # exact frame index
            text_qf.tStart = t  # local t and not account for scr refresh
            text_qf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_qf, 'tStartRefresh')  # time at next scr refresh
            text_qf.setAutoDraw(True)
        if text_qf.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_qf.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_qf.tStop = t  # not accounting for scr refresh
                text_qf.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_qf, 'tStopRefresh')  # time at next scr refresh
                text_qf.setAutoDraw(False)
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
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
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 7.5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(target)) or (key_resp.keys == target):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim_respComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim_resp"-------
    for thisComponent in stim_respComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stim_present.stop()  # ensure sound has stopped at end of routine
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(target).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for practice_trials (TrialHandler)
    practice_trials.addData('key_resp.keys',key_resp.keys)
    practice_trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        practice_trials.addData('key_resp.rt', key_resp.rt)
    practice_trials.addData('key_resp.started', key_resp.tStartRefresh)
    practice_trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    if not key_resp.keys:
        msg="Failed to respond"
    elif key_resp.corr:#stored on last run routine
        msg="Correct!"
    else:
        msg="Oops! That was wrong"
    
    trial_count=trial_count+1
    msg_t = "[" + str(trial_count-16) + "/64]\nCompleted"
    
    # ------Prepare to start Routine "prac_feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_feedback.setText(msg)
    key_exp_cont.keys = []
    key_exp_cont.rt = []
    _key_exp_cont_allKeys = []
    # keep track of which components have finished
    prac_feedbackComponents = [text_feedback, text_exp_cont, key_exp_cont]
    for thisComponent in prac_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prac_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prac_feedback"-------
    while continueRoutine:
        # get current time
        t = prac_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prac_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_feedback* updates
        if text_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_feedback.frameNStart = frameN  # exact frame index
            text_feedback.tStart = t  # local t and not account for scr refresh
            text_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_feedback, 'tStartRefresh')  # time at next scr refresh
            text_feedback.setAutoDraw(True)
        
        # *text_exp_cont* updates
        if text_exp_cont.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text_exp_cont.frameNStart = frameN  # exact frame index
            text_exp_cont.tStart = t  # local t and not account for scr refresh
            text_exp_cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_exp_cont, 'tStartRefresh')  # time at next scr refresh
            text_exp_cont.setAutoDraw(True)
        
        # *key_exp_cont* updates
        waitOnFlip = False
        if key_exp_cont.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_exp_cont.frameNStart = frameN  # exact frame index
            key_exp_cont.tStart = t  # local t and not account for scr refresh
            key_exp_cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_exp_cont, 'tStartRefresh')  # time at next scr refresh
            key_exp_cont.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_exp_cont.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_exp_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_exp_cont.status == STARTED and not waitOnFlip:
            theseKeys = key_exp_cont.getKeys(keyList=['space'], waitRelease=False)
            _key_exp_cont_allKeys.extend(theseKeys)
            if len(_key_exp_cont_allKeys):
                key_exp_cont.keys = _key_exp_cont_allKeys[-1].name  # just the last key pressed
                key_exp_cont.rt = _key_exp_cont_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prac_feedback"-------
    for thisComponent in prac_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_exp_cont.keys in ['', [], None]:  # No response was made
        key_exp_cont.keys = None
    practice_trials.addData('key_exp_cont.keys',key_exp_cont.keys)
    if key_exp_cont.keys != None:  # we had a response
        practice_trials.addData('key_exp_cont.rt', key_exp_cont.rt)
    # the Routine "prac_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_trials'


# ------Prepare to start Routine "main_instr"-------
continueRoutine = True
# update component parameters for each repeat
key_main.keys = []
key_main.rt = []
_key_main_allKeys = []
# keep track of which components have finished
main_instrComponents = [text_main1, text_main2, key_main]
for thisComponent in main_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
main_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "main_instr"-------
while continueRoutine:
    # get current time
    t = main_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=main_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_main1* updates
    if text_main1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_main1.frameNStart = frameN  # exact frame index
        text_main1.tStart = t  # local t and not account for scr refresh
        text_main1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_main1, 'tStartRefresh')  # time at next scr refresh
        text_main1.setAutoDraw(True)
    
    # *text_main2* updates
    if text_main2.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        text_main2.frameNStart = frameN  # exact frame index
        text_main2.tStart = t  # local t and not account for scr refresh
        text_main2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_main2, 'tStartRefresh')  # time at next scr refresh
        text_main2.setAutoDraw(True)
    
    # *key_main* updates
    waitOnFlip = False
    if key_main.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        key_main.frameNStart = frameN  # exact frame index
        key_main.tStart = t  # local t and not account for scr refresh
        key_main.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_main, 'tStartRefresh')  # time at next scr refresh
        key_main.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_main.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_main.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_main.status == STARTED and not waitOnFlip:
        theseKeys = key_main.getKeys(keyList=['space'], waitRelease=False)
        _key_main_allKeys.extend(theseKeys)
        if len(_key_main_allKeys):
            key_main.keys = _key_main_allKeys[-1].name  # just the last key pressed
            key_main.rt = _key_main_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in main_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "main_instr"-------
for thisComponent in main_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_main.keys in ['', [], None]:  # No response was made
    key_main.keys = None
thisExp.addData('key_main.keys',key_main.keys)
if key_main.keys != None:  # we had a response
    thisExp.addData('key_main.rt', key_main.rt)
thisExp.addData('key_main.started', key_main.tStartRefresh)
thisExp.addData('key_main.stopped', key_main.tStopRefresh)
thisExp.nextEntry()
# the Routine "main_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
main_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='main_trials')
thisExp.addLoop(main_trials)  # add the loop to the experiment
thisMain_trial = main_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMain_trial.rgb)
if thisMain_trial != None:
    for paramName in thisMain_trial:
        exec('{} = thisMain_trial[paramName]'.format(paramName))

for thisMain_trial in main_trials:
    currentLoop = main_trials
    # abbreviate parameter names if possible (e.g. rgb = thisMain_trial.rgb)
    if thisMain_trial != None:
        for paramName in thisMain_trial:
            exec('{} = thisMain_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "stim_resp"-------
    continueRoutine = True
    routineTimer.add(8.000000)
    # update component parameters for each repeat
    stim_present.setSound(sent_stim, secs=2.5, hamming=True)
    stim_present.setVolume(1, log=False)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    stim_respComponents = [stim_present, text_qm, text_qf, fixation, key_resp]
    for thisComponent in stim_respComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stim_respClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stim_resp"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stim_respClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stim_respClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop stim_present
        if stim_present.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stim_present.frameNStart = frameN  # exact frame index
            stim_present.tStart = t  # local t and not account for scr refresh
            stim_present.tStartRefresh = tThisFlipGlobal  # on global time
            stim_present.play(when=win)  # sync with win flip
        if stim_present.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim_present.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                stim_present.tStop = t  # not accounting for scr refresh
                stim_present.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stim_present, 'tStopRefresh')  # time at next scr refresh
                stim_present.stop()
        
        # *text_qm* updates
        if text_qm.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            text_qm.frameNStart = frameN  # exact frame index
            text_qm.tStart = t  # local t and not account for scr refresh
            text_qm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_qm, 'tStartRefresh')  # time at next scr refresh
            text_qm.setAutoDraw(True)
        if text_qm.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_qm.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_qm.tStop = t  # not accounting for scr refresh
                text_qm.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_qm, 'tStopRefresh')  # time at next scr refresh
                text_qm.setAutoDraw(False)
        
        # *text_qf* updates
        if text_qf.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            text_qf.frameNStart = frameN  # exact frame index
            text_qf.tStart = t  # local t and not account for scr refresh
            text_qf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_qf, 'tStartRefresh')  # time at next scr refresh
            text_qf.setAutoDraw(True)
        if text_qf.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_qf.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_qf.tStop = t  # not accounting for scr refresh
                text_qf.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_qf, 'tStopRefresh')  # time at next scr refresh
                text_qf.setAutoDraw(False)
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
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
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 7.5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(target)) or (key_resp.keys == target):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim_respComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim_resp"-------
    for thisComponent in stim_respComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stim_present.stop()  # ensure sound has stopped at end of routine
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(target).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for main_trials (TrialHandler)
    main_trials.addData('key_resp.keys',key_resp.keys)
    main_trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        main_trials.addData('key_resp.rt', key_resp.rt)
    main_trials.addData('key_resp.started', key_resp.tStartRefresh)
    main_trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    if not key_resp.keys:
        msg="Failed to respond"
    elif key_resp.corr:#stored on last run routine
        msg="Correct!"
    else:
        msg="Oops! That was wrong"
    
    trial_count=trial_count+1
    msg_t = "[" + str(trial_count-16) + "/64]\nCompleted"
    
    # ------Prepare to start Routine "main_feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_feedback_2.setText(msg_t)
    key_exp_cont_2.keys = []
    key_exp_cont_2.rt = []
    _key_exp_cont_2_allKeys = []
    # keep track of which components have finished
    main_feedbackComponents = [text_feedback_2, text_exp_cont_2, key_exp_cont_2]
    for thisComponent in main_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    main_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "main_feedback"-------
    while continueRoutine:
        # get current time
        t = main_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=main_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_feedback_2* updates
        if text_feedback_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_feedback_2.frameNStart = frameN  # exact frame index
            text_feedback_2.tStart = t  # local t and not account for scr refresh
            text_feedback_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_feedback_2, 'tStartRefresh')  # time at next scr refresh
            text_feedback_2.setAutoDraw(True)
        
        # *text_exp_cont_2* updates
        if text_exp_cont_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text_exp_cont_2.frameNStart = frameN  # exact frame index
            text_exp_cont_2.tStart = t  # local t and not account for scr refresh
            text_exp_cont_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_exp_cont_2, 'tStartRefresh')  # time at next scr refresh
            text_exp_cont_2.setAutoDraw(True)
        
        # *key_exp_cont_2* updates
        waitOnFlip = False
        if key_exp_cont_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_exp_cont_2.frameNStart = frameN  # exact frame index
            key_exp_cont_2.tStart = t  # local t and not account for scr refresh
            key_exp_cont_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_exp_cont_2, 'tStartRefresh')  # time at next scr refresh
            key_exp_cont_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_exp_cont_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_exp_cont_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_exp_cont_2.status == STARTED and not waitOnFlip:
            theseKeys = key_exp_cont_2.getKeys(keyList=['space'], waitRelease=False)
            _key_exp_cont_2_allKeys.extend(theseKeys)
            if len(_key_exp_cont_2_allKeys):
                key_exp_cont_2.keys = _key_exp_cont_2_allKeys[-1].name  # just the last key pressed
                key_exp_cont_2.rt = _key_exp_cont_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in main_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "main_feedback"-------
    for thisComponent in main_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_exp_cont_2.keys in ['', [], None]:  # No response was made
        key_exp_cont_2.keys = None
    main_trials.addData('key_exp_cont_2.keys',key_exp_cont_2.keys)
    if key_exp_cont_2.keys != None:  # we had a response
        main_trials.addData('key_exp_cont_2.rt', key_exp_cont_2.rt)
    # the Routine "main_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'main_trials'


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
