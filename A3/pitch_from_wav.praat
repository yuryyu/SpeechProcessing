form pitch_from_wav
	sentence filename C:\Users\yuzba\Documents\HIT\Speech\HandsOn3\Al_page_13_78.wav 
	real minpitch 	25
	real maxpitch 	900
	#real timestep	0.0
    boolean cache 1
    text moreArgs
endform
procedure getArg .name$ .varname$ .default
    '.varname$'=.default
    .argval=extractNumber(moreArgs$, .name$  + ":")
    if .argval<>undefined
    	'.varname$'=.argval
    endif
endproc
call getArg detection_for_DB.time_step time_step 0
call getArg detection_for_DB.max_num_candidates max_num_candidates 15
call getArg detection_for_DB.very_accurate very_accurate 0
call getArg detection_for_DB.silence_threshold silence_threshold 0.09
call getArg detection_for_DB.voicing_threshold voicing_threshold 0.40
call getArg detection_for_DB.octave_cost octave_cost 0.01
call getArg detection_for_DB.octave_jump_cost octave_jump_cost 0.35
call getArg detection_for_DB.voiced_unvoiced_cost voiced_unvoiced_cost 0.14

clearinfo
foundcache=0
if cache
    pitchfilename$=replace_regex$(filename$,"\.[^\.]+$","",1) + "[ac 'time_step' 'minpitch' 'max_num_candidates' 'very_accurate' 'silence_threshold' 'voicing_threshold' 'octave_cost' 'octave_jump_cost' 'voiced_unvoiced_cost' 'maxpitch'].Pitch"
    if fileReadable(pitchfilename$)
        Read from file... 'pitchfilename$'
        foundcache=1
    endif
endif
if foundcache==0
    Read from file... 'filename$'
To Pitch (ac)... 'time_step' 'minpitch' 'max_num_candidates' 'very_accurate' 'silence_threshold' 'voicing_threshold' 'octave_cost' 'octave_jump_cost' 'voiced_unvoiced_cost' 'maxpitch'
#To Pitch (ac)... 'timestep' 'minpitch' 15 off 0.03 0.50 0.01 0.35 0.14 'maxpitch'
#^ alissa 28.05.2012
#To Pitch (ac)... 'timestep' 'minpitch' 15 off 0.03 0.1 -0.01 0.75 0.75 'maxpitch'
#^ troy 28.05.2012
#To Pitch (ac)... 'timestep' 'minpitch' 15 off 0.03 0.4 0.01 0.35 0.4 'maxpitch'
    if cache
        Save as binary file... 'pitchfilename$'
    endif
endif
tstep=Get time step
printline 'tstep'
n=Get number of frames
printline 'n'
for i to n
	f0=Get value in frame... 'i' Hertz
	frame_t=Get time from frame number... 'i'
	if f0==undefined
		printline 'frame_t' NaN
	else
		printline 'frame_t' 'f0'
	endif
endfor