# timelibWAM

timelibWAM is a library meant to alert the user about the 
completion of a program. This can work best with larger
projects in which may take longer periods of time to 
finish running. The package can also alert the user
about errors that occur.

**IMPORTANT:**
  When utilizing the library, run the import statement by itself. After 
  completing the entry, run the rest of your code. You will incur errors otherwise!

**Best Setup:**
Copy and paste this bad boy:

===================================

from timelibWAM import *

      try:
          s = tl.start() 

          *your code*
          
          tl.send_frame_end(s)
      
      except Exception as e:
          tl.error_alert()

===================================
