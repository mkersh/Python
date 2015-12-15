from java import awt
#from javax.swing import JFrame, JButton, JOptionPane
from javax.swing import JOptionPane
import sys
import pdb

class SpamListener(awt.event.ActionListener):
    def actionPerformed(self,event):
        if event.getActionCommand() == "Spam":
	    print 'Spam and eggs!'

class ExitBtnListener(awt.event.ActionListener):
    def actionPerformed(self,event):
        if event.getActionCommand() == "Exit":
	    print 'About to Exit!'
	    sys.exit(0)

class DebugBtnListener(awt.event.ActionListener):
    def actionPerformed(self,event):
    	# setting debug here works and you can then have a persistent debugging session stopping in multiple listeners
        pdb.set_trace()

# Need to setup something like the below for the window to close
class Adapter(awt.event.WindowAdapter):
    def windowClosing(self, event):
    	# Can just close without asking
    	#sys.exit(0)
        if JOptionPane.showConfirmDialog(None, "Wanna exit?","Jython Test", JOptionPane.OK_CANCEL_OPTION) == JOptionPane.OK_OPTION:
            sys.exit(0)

def main():
	# enable the below to debug this test
	f = awt.Frame("Subclassing Example")
	b = awt.Button("Spam")
	b.addActionListener(SpamListener())
	b2 = awt.Button("Exit")
	b2.addActionListener(ExitBtnListener())
	b3 = awt.Button("Debug")
	b3.addActionListener(DebugBtnListener())
	f.add(b, "North")
	f.add(b2, "South")
	f.add(b3, "West")
	# either set the size explicitly or do a pack to minimise the space used
	#f.setSize(500,500)
	f.pack()
	f.setVisible(1)
	# if you want to debug a Swing app you have to call set_trace() in the Java thread
	# if you call it in main it will not work. It will stop in main but not allow you to
	# set breaks on any of your listeners
	f.addWindowListener(Adapter())

if __name__ == '__main__':
	main()