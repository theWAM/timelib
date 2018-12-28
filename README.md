# timelibWAM

timelibWAM is an open source package meant to alert the user about the 
completion of a program. This can work best with larger
projects in which may take longer periods of time to 
finish running. The package can also alert the user
about errors that occur.
  
## Installation
Copy into terminal/command prompt:

    pip install timelibWAM

## Use 

### 1. Run: 

    from timelibWAM import * 

**IMPORTANT:**
  When utilizing the library, run the import statement by itself. After 
  completing the entry, run the rest of your code. You will incur errors otherwise!
  
### 2. Run tl.start() and save its return value in a variable

    from timelibWAM import * 
    
    s = tl.start()

### 3. Enter your code!

    from timelibWAM import * 
    
    s = tl.start()
    
    #Your code here
    
### 4. Run one of our ending functions (print_end(), frame_end(), send_end(), or send_frame_end()) after your code
    
    from timelibWAM import * 
    
    s = tl.start()
    
    #Your code here
    
    tl.send_frame_end(s)
    
**IMPORTANT:**
  If you'd like to be alerted in the case of error, steps 2-4 should be within a try statement
  followed by an except statement that runs one of our error functions (frame_alert() or error_alert())

**Best Setup:**
Copy and paste this bad boy for text and frame alerts:

    from timelibWAM import *

      try:
        s = tl.start() 

        *your code*
          
        tl.send_frame_end(s)
      
      except Exception as e:
        
        tl.error_alert()
