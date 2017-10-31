'''

SMS API
Author: Salil Kapur

'''

import gtk
import pygtk
import urllib2


class gui:
	
	def __init__(self):
		
		self.win=gtk.Window()
		self.win.set_title("SMS API")
		self.win.set_size_request(500,300)
		self.win.show()
		
		'''Creating a box inside the window'''
		self.winbox=gtk.VBox(False,2)  
		self.win.add(self.winbox)
		self.winbox.show()
		
		'''Box used for Heading'''
		self.info=gtk.VBox(False,2)
		self.winbox.add(self.info)
		self.info.show()
		
		self.head=gtk.Label("LOGIN")
		self.info.add(self.head)
		self.head.show()
		
		'''Box to input Username and Password from user'''
		self.user=gtk.VBox(False,2)
		self.winbox.add(self.user)
		self.user.show()
		
		self.unamebox=gtk.HBox()
		self.user.add(self.unamebox)
		self.unamebox.show()
		
		self.uname=gtk.Label("Username:")
		self.unamebox.add(self.uname)
		self.uname.show()
		
		self.username=gtk.Entry()
		self.unamebox.add(self.username)
		self.username.show()
	
		
		self.pwd=gtk.HBox()
		self.user.add(self.pwd)
		self.pwd.show()
		
		self.passwd=gtk.Label("Password:")
		self.pwd.add(self.passwd)
		self.passwd.show()
		
		self.password=gtk.Entry()
		self.pwd.add(self.password)
		self.password.show()

		'''Box used to send message'''
		self.msg_info=gtk.VBox(False,2)
		self.winbox.add(self.msg_info)
		self.msg_info.show()		
		
		self.to_info=gtk.HBox()
		self.msg_info.add(self.to_info)
		self.to_info.show()
		
		self.to_label=gtk.Label("To:")
		self.to_info.add(self.to_label)
		self.to_label.show()
		
		self.to=gtk.Entry()
		self.to_info.add(self.to)
		self.to.show()

		self.msgbox=gtk.HBox()
		self.msg_info.add(self.msgbox)
		self.msgbox.show()
		
		self.msg_label=gtk.Label("Message")
		self.msgbox.add(self.msg_label)
		self.msg_label.show()
				
		self.msg=gtk.Entry()
		self.msgbox.add(self.msg)
		self.msg.show()
		
		'''Button to send message'''
		self.sendbox=gtk.HBox()
		self.winbox.add(self.sendbox)
		self.sendbox.show()
		
		self.send=gtk.Button("SEND")
		self.sendbox.add(self.send)
		self.send.show()
		self.send.connect("clicked",self.get_numbers)
	
	'''Function to get numbers'''
	def get_numbers(self,Widget=None,Data=None):
		self.numbers=(self.to.get_text()).split(',')
		print self.numbers
		self.send_msg()
		
	'''Function to send message'''
	def send_msg(self,Widget=None,Data=None):
		base_url='http://ubaid.tk/sms/sms.aspx?'
		
		for i in self.numbers:
			print i
			details='uid='+str(self.username.get_text())+'&pwd='+str(self.password.get_text())+'&phone='+str(i)+'&msg='+str(self.msg.get_text())+'&codes=1'+'&provider=way2sms'
		
				
			data=urllib2.urlopen(base_url+details)
			print data.read()
	

gui()
gtk.main()
