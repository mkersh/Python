class Myerr1(Exception):
	def __init__(self, str):
		super().__init__(str)

def main():
	try:
		print("1")
		raise Exception("Throw an error")
		#raise Myerr1("Throw an error")
		print("Should not get here")
	except Myerr1 as er:
		print("More specific Exception was:", repr(er))
	except Exception as er:
		print("Exception was:", repr(er))
	


if __name__ == '__main__':
	main()