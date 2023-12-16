from wifi import WifiConnector
import secrets

wifi = WifiConnector(secrets.SSID, secrets.PASSWORD)

wifi.connect()
