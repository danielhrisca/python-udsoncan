from test.stub import StubbedConnection
from test.ThreadableTest import ThreadableTest
from udsoncan.client import Client

class ClientServerTest(ThreadableTest):
	def __init__(self, *args, **kwargs):
		ThreadableTest.__init__(self, *args, **kwargs)

	def setUp(self):
		self.conn = StubbedConnection()

	def clientSetUp(self):
		self.udsclient = Client(self.conn, request_timeout=0.5)
		self.udsclient.open()
		if hasattr(self, "postClientSetUp"):
			self.postClientSetUp()

	def clientTearDown(self):
		self.udsclient.close()