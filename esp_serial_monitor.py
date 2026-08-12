import serial
import sys
import time

PORT = sys.argv[1] if len(sys.argv) > 1 else "/dev/tty.usbserial"
BAUD_RATE = 115200


def monitor_esp(port, baud_rate):
    try:
        esp = serial.Serial(port, baud_rate, timeout=1)
        time.sleep(2)

        print(f"Connected to ESP device on {port}")
        print(f"Baud rate: {baud_rate}")
        print("Listening for serial data...\n")

        while True:
            if esp.in_waiting:
                data = esp.readline().decode("utf-8", errors="replace").strip()

                if data:
                    print(f"[ESP] {data}")

    except serial.SerialException as error:
        print(f"Could not connect to ESP device: {error}")

    except KeyboardInterrupt:
        print("\nSerial monitor stopped.")

    finally:
        if "esp" in locals() and esp.is_open:
            esp.close()


if __name__ == "__main__":
    monitor_esp(PORT, BAUD_RATE)