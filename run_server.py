from skycrane.skycrane import SkyCrane
from time import sleep


failures = 0
while failures < 5:
	try:
		crane = SkyCrane()
		while True:
			crane.run()
			sleep(1)
	except Exception as e:
		failures += 1
		print("System crashed!")
		print(e)
		print("Attempting restart #", failures)
