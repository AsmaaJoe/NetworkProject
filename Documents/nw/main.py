from PyQt4 import QtGui, QtCore # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication

import project # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer
from scapy.all import *

class ExampleApp(QtGui.QMainWindow, project.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        ##pkts=sniff(count=3,prn=self.textEdit.setText(lambda x: x.custom_action()))
        #packet= sniff(count=3)
        
        # for i in range (5):
        #     packet= sniff(count=1)
        #     self.textEdit.append('Packet : {} ==> {}'.format( packet[0][1].src, packet[0][1].dst)   )
        ##self.textEdit.setText(str(pkts[0]))
        ##Qstring y = pkts[0]
        self.pushButton.clicked.connect(self.b1_clicked)
        self.pushButton_2.clicked.connect(self.b2_clicked)
      ##  self.textEdit.setText(str(pkts[0]))
                            # It sets up layout and widgets that are defined
  
    def b1_clicked(self):
         for i in range (5):
            packet= sniff(count=1)
            self.textEdit.append('Packet : {} ==> {}'.format( packet[0][1].src, packet[0][1].dst)   )
    def b2_clicked(self):
        self.textEdit.setText('')

     # for i in range(10):
     #    print i
     #    if self.pushButton:
     #        break
     #    time.sleep(0.5)    

		
		
def custom_action(packet):
    global counter
    counter += 1
    return   'Packet #{}: {} ==> {}'.format(counter, packet[0][1].src, packet[0][1].dst)   
def main():
	
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication

    form = ExampleApp()                 # We set the form to be our ExampleApp (design) 
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
