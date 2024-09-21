import serial
import time
import threading

def calculate_bps(bytes_transferred, duration):
    bits = bytes_transferred * 8
    bps = bits / duration if duration > 0 else 0
    return bps

def live_bps_tracking(port, baud_rate, data, check_interval=0.1, termination_char='\n'):
    try:
        ser = serial.Serial(port, baud_rate, timeout=2)
        time.sleep(2)

        total_bytes_sent = len(data.encode())
        start_time = time.time()
        
        print("Starting data transmission...")

        ser.write(data.encode())
        total_bytes_sent = len(data)

        send_duration = time.time() - start_time
        bps_send = calculate_bps(total_bytes_sent, send_duration)
        print(f"Total bytes sent: {total_bytes_sent}")
        print(f"Sending speed: {bps_send:.2f} bits/sec")

        total_bytes_received = 0
        start_time = time.time()

        received_data = ""
        prev_time = 0

        while True:
            if ser.inWaiting() > 0:
                response = ser.read(ser.inWaiting())
                total_bytes_received = len(response)
                current_time = time.time() - start_time
                transmission_time = current_time - prev_time
                prev_time = current_time

                bps_receive = calculate_bps(total_bytes_received, transmission_time)
                #print(f"Response:{response},bytes:{total_bytes_received},time:{transmission_time}")
                print(f"Live receiving speed: {bps_receive:.2f} bits/sec")
                received_data += response.decode()

                if termination_char in received_data:
                    print(f"Received: {received_data}")
                    print("Termination character received. Exiting...")
                    break

            time.sleep(check_interval)

    except serial.SerialException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    serial_port = 'COM4'
    baud_rate = 2400
    data_to_send = 'Finance Minister Arun Jaitley Tuesday hit out at former RBI governor Raghuram Rajan for predicting that the next banking crisis would be triggered by MSME lending, saying postmortem is easier than taking action when it was required. Rajan, who had as the chief economist at IMF warned of impending financial crisis of 2008, in a note to a parliamentary committee warned against ambitious credit targets and loan waivers, saying that they could be the sources of next banking crisis. Government should focus on sources of the next crisis, not just the last one. In particular, government should refrain from setting ambitious credit targets or waiving loans. Credit targets are sometimes achieved by abandoning appropriate due diligence, creating the environment for future NPAs," Rajan said in the note." Both MUDRA loans as well as the Kisan Credit Card, while popular, have to be examined more closely for potential credit risk. Rajan, who was RBI governor for three years till September 2016, is currently.\n'

    live_bps_tracking(serial_port, baud_rate, data_to_send, check_interval=0.01, termination_char='\n')