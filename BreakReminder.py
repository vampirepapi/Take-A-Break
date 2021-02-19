import time
from plyer import notification
if __name__ == '__main__':

	while True:

		notification.notify(
			title = "Take a break!",
			message = "Do some Exercise and Drink some Water. ",
			app_icon = r"C:\Users\vampirepapi\Desktop\Snippets\DesktopNotify\icon.ico",
			timeout=10

		)
		time.sleep(60*150)

