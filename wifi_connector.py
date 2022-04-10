from subprocess import run
import sys




# command = nmcli dev wifi connect "mr.nobody" password "password"


try:
	ssid = sys.argv[1]

	password = sys.argv[2]


	connection = run(['nmcli', 'dev', 'wifi', 'connect', f'{ssid}', 'password', f'{password}'], capture_output=True).stdout


	print(f"[*] connected successfully to {ssid}")


except IndexError:
	print("usage: python3 wifi_connector.py <SSID> <PASSWORD>")
