# pitch_textGrid_man.praat
# Cross-platform pitch extraction with TextGrid intervals
#
# Description:
#   Extracts mean pitch (F0) values for each interval in a TextGrid
#   Requires both Sound and TextGrid objects to be selected
#   Outputs tab-separated results: start_time, end_time, F0, label
#
# Usage:
#   1. Open audio file (Sound)
#   2. Create or open TextGrid for same audio
#   3. Select both Sound and TextGrid
#   4. Run this script: praat pitch_textGrid_man.praat --open --run
#
# Compatibility:
#   ✓ Windows
#   ✓ macOS (Intel and Apple Silicon)
#   ✓ Linux (Ubuntu, Debian, CentOS)
#
# Output:
#   Tab-separated values with columns:
#   - Start time (seconds)
#   - End time (seconds)
#   - Mean F0 (Hertz)
#   - Interval label

# Validate inputs
if numberOfSelected ("Sound") <> 1
    exitScript: "ERROR: Please select exactly one Sound object"
endif

if numberOfSelected ("TextGrid") <> 1
    exitScript: "ERROR: Please select exactly one TextGrid object"
endif

# Store references to selected objects
sound = selected ("Sound")
textgrid = selected ("TextGrid")

# Initialize output
writeInfoLine: "start_time", tab$, "end_time", tab$, "F0_Hz", tab$, "label"

# Extract pitch from sound
selectObject: sound
To Pitch: 0.0, 75, 600
pitch = selected ("Pitch")

# Get number of intervals in first tier
selectObject: textgrid
n = Get number of intervals: 1

# Process each interval
for i to n
    # Get interval info
    tekst$ = Get label of interval: 1, i
    
    # Only process non-empty intervals
    if tekst$ <> ""
        t1 = Get starting point: 1, i
        t2 = Get end point: 1, i
        
        # Get mean pitch for interval
        selectObject: pitch
        f0 = Get mean: t1, t2, "Hertz"
        
        # Format output
        if f0 = undefined
            f0_str$ = "NaN"
        else
            f0_str$ = fixed$ (round (f0), 0)
        endif
        
        # Write result
        f0_formatted$ = fixed$ (f0, 2)
        appendInfoLine: 
        ... fixed$ (t1, 3), tab$, fixed$ (t2, 3), tab$, f0_formatted$, tab$, tekst$
        
        # Return to TextGrid for next iteration
        selectObject: textgrid
    endif
endfor

# Cleanup
selectObject: sound, textgrid, pitch
appendInfoLine: ""
appendInfoLine: "Analysis complete for ", n, " intervals"

# Uncomment below to auto-save results to file
# output_file$ = replace_regex$ (selected$ ("Sound"), "\.[^\.]+$", "_pitch.txt", 1)
# Save as text file... 'output_file$'
# appendInfoLine: "Results saved to: ", output_file$
