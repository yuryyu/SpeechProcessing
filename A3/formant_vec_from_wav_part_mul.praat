form formant_vec_from_wav_part 
	sentence filename C:\Users\yuzba\Documents\HIT\Speech\HandsOn3\Al_page_13_78.wav
   	sentence samp_starts 0
	sentence samp_ends 0
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
call getArg formant_detection_for_DB.time_step time_step 0
call getArg formant_detection_for_DB.max_freq max_freq 5000
call getArg formant_detection_for_DB.num_formants num_formants 7
call getArg formant_detection_for_DB.window_length window_length 0.025
call getArg formant_detection_for_DB.pre_emphasis pre_emphasis 50

clearinfo

snd=Open long sound file... 'filename$'



foundcache=0
if cache
    formantfilename$=replace_regex$(filename$,"\.[^\.]+$","",1) + "[burg 'time_step' 'max_freq' 'num_formants' 'window_length' 'pre_emphasis'].Formant"
    if fileReadable(formantfilename$)
        frm=do ("Read from file...", formantfilename$)
        foundcache=1
    endif
endif
if foundcache==0
    do ("Read from file...", filename$)

    frm=do ("To Formant (burg)...", time_step, num_formants, max_freq, window_length, pre_emphasis)
    if cache
        do("Save as text file...", formantfilename$)
    endif
endif

if not endsWith(samp_starts$," ")
	samp_starts$ = samp_starts$ + " "
endif
if not endsWith(samp_ends$," ")
	samp_ends$ = samp_ends$ + " "
endif

samp_start = number(samp_starts$)
samp_end = number(samp_ends$)
while not ((samp_start==undefined) or (samp_end==undefined))
    select snd
	tstart=do ("Get time from sample number...", samp_start)
	tend=do ("Get time from sample number...", samp_end)
    select frm
	for i from 1 to num_formants
		if samp_start==samp_end
			formant_val=do ("Get value at time...", i, tstart, "Hertz", "Linear")
		else
			formant_val=do ("Get mean...", i, tstart, tend, "Hertz")
		endif
		if formant_val==undefined
			writeInfo("NaN ")
		else
			writeInfo(formant_val, " ")
		endif
	endfor
	writeInfoLine()
	samp_starts$=right$(samp_starts$,length(samp_starts$)-index(samp_starts$," "))
	samp_ends$=right$(samp_ends$,length(samp_ends$)-index(samp_ends$," "))

	samp_start = number(samp_starts$)
	samp_end = number(samp_ends$)
endwhile