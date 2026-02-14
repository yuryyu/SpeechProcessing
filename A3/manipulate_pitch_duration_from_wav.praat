form vivotext_sampler_runpsola
	sentence concatenatedFile C:\Users\MOTIZ~1\AppData\Local\Temp\Vivotext\5ec7-8d05-17d3-910f.in.wav
	sentence pitchFile C:\Users\MOTIZ~1\AppData\Local\Temp\Vivotext\5ec7-8d05-17d3-910f.PitchTier
	sentence durationFile C:\Users\MOTIZ~1\AppData\Local\Temp\Vivotext\5ec7-8d05-17d3-910f.DurationTier
	sentence outFile C:\Users\MOTIZ~1\AppData\Local\Temp\Vivotext\5ec7-8d05-17d3-910f.out.wav
	positive minpitch 40
	positive maxpitch 450
    text moreArgs
endform

procedure getArg .name$ .varname$ .default
    '.varname$'=.default
    .argval=extractNumber(moreArgs$, .name$  + ":")

    if .argval<>undefined
    	'.varname$'=.argval
    endif
endproc

call getArg detection_for_PSOLA.time_step time_step 0
call getArg detection_for_PSOLA.max_num_candidates max_num_candidates 15
call getArg detection_for_PSOLA.very_accurate very_accurate 0
call getArg detection_for_PSOLA.silence_threshold silence_threshold 0.03
call getArg detection_for_PSOLA.voicing_threshold voicing_threshold 0.40
call getArg detection_for_PSOLA.octave_cost octave_cost 0.01
call getArg detection_for_PSOLA.octave_jump_cost octave_jump_cost 0.35
call getArg detection_for_PSOLA.voiced_unvoiced_cost voiced_unvoiced_cost 0.14
call getArg furby_effect.uncorrectedShiftCents uncorrectedShiftCents 0
call getArg furby_effect.formantShiftCents formantShiftCents 0


sound_inner=Read from file... 'concatenatedFile$'
#Write to WAV file... 'outFile$'.nodsp.wav
origSampleRate = Get sampling frequency
if (uncorrectedShiftCents<>0)
	uncorrectedShiftRatio = 2^(uncorrectedShiftCents/1200)
	invUncorrectedShiftRatio = 1 / uncorrectedShiftRatio
	Scale times by... 'invUncorrectedShiftRatio'
	minpitch = minpitch * uncorrectedShiftRatio
	maxpitch = maxpitch * uncorrectedShiftRatio
endif

if (formantShiftCents<>0)
	formantShiftRatio = 2^(formantShiftCents/1200)
	invFormantShiftRatio = 1 / formantShiftRatio
	Scale times by... 'invFormantShiftRatio'
	minpitch = minpitch * formantShiftRatio
	maxpitch = maxpitch * formantShiftRatio
endif


sampleRate = Get sampling frequency

maxperiod=1/minpitch


dur_inner=Get total duration

silence1=Create Sound from formula... silence1 1 0 1 'sampleRate' 0
Override sampling frequency... 'sampleRate'

select sound_inner
sound_inner2=Copy...
select sound_inner
Remove
sound_inner = sound_inner2
select sound_inner
Override sampling frequency... 'sampleRate'

pitchT=Read from file... 'pitchFile$'

if (uncorrectedShiftCents<>0)
	Multiply frequencies... 0 'dur_inner' 'uncorrectedShiftRatio'
	Scale times by... 'invUncorrectedShiftRatio'
endif
if (formantShiftCents<>0)	
	Scale times by... 'invFormantShiftRatio'
endif

duration=Read from file... 'durationFile$'
if (uncorrectedShiftCents<>0)
	Scale times by... 'invUncorrectedShiftRatio'
endif
if (formantShiftCents<>0)
	Scale times by... 'invFormantShiftRatio'
	Formula... self * 'formantShiftRatio'
endif

dur_inner_target=Get target duration... 0 'dur_inner'
dur_left_silence_target=Get target duration... -1 0
tmp=dur_inner+1
dur_right_silence_target=Get target duration... 'dur_inner' 'tmp'
select silence1
silence2=Copy... silence2

select silence1
plus sound_inner
plus silence2
sound=Concatenate

select sound
Shift times by... -1


origpitch=To Pitch (ac)... 'time_step' 'minpitch' 'max_num_candidates' 'very_accurate' 'silence_threshold' 'voicing_threshold' 'octave_cost' 'octave_jump_cost' 'voiced_unvoiced_cost' 'maxpitch'
#origpitch=To Pitch (ac)... 0 'minpitch' 15 off 0.03 0.40 0.01 0.35 0.14 'maxpitch'
#^ alissa 28.05.2012
#origpitch=To Pitch (ac)... 0 'minpitch' 15 off 0.03 0.2 -0.01 0.75 0.75 'maxpitch'
#^ troy 28.05.2012
select sound
plus origpitch
pulses=To PointProcess (cc)

select sound
plus pitchT
plus duration
plus pulses
To Sound... 'maxperiod'
dur_left_silence_target=dur_left_silence_target-1
tmp=(dur_left_silence_target+dur_inner_target)
sound_target=Extract part... 'dur_left_silence_target' 'tmp' rectangular 1 no

if origSampleRate<>sampleRate
	resampleAccuracy = (50/44100) * origSampleRate
	Resample... 'origSampleRate' 'resampleAccuracy'
endif
out=Write to WAV file... 'outFile$'
select sound_target
plus silence1
plus silence2
plus sound
plus sound_inner
plus pitchT
plus duration
plus pulses
plus out
#Remove
