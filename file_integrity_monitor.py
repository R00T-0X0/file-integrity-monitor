
import hashlib
import time
import os


def calculate_file_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()


def create_baseline(file_path):
    baseline_hash = calculate_file_hash(file_path)

    print(f"[+] Baseline Hash: {baseline_hash}")

    return baseline_hash


def compare_hashes(baseline_hash, current_hash):
    return baseline_hash == current_hash


def display_alert():
    print("\n" + "!" * 55)
    print("[CRITICAL ALERT] File modification detected!")
    print("[!] The file integrity has been compromised.")
    print("!" * 55 + "\n")


def monitor_file(file_path, baseline_hash):
    print("\n[*] File monitoring started...")
    print("[*] Checking every 3 seconds.")
    print("[*] Press CTRL+C to stop.\n")

    while True:
        try:
            current_hash = calculate_file_hash(file_path)

            if compare_hashes(baseline_hash, current_hash):
                print("[+] No changes detected.")
            else:
                display_alert()

        except FileNotFoundError:
            print("[CRITICAL ALERT] The monitored file was not found!")

        except PermissionError:
            print("[ERROR] Permission denied.")

        except OSError as error:
            print(f"[ERROR] {error}")

        time.sleep(3)


def Start_file_monitor():
    file_path = input("Enter file path: ").strip()

    if not os.path.isfile(file_path):
        print("[ERROR] File does not exist.")
        return

    baseline_hash = create_baseline(file_path)

    try:
        monitor_file(file_path, baseline_hash)

    except KeyboardInterrupt:
        print("\n[*] Monitoring stopped.")


if __name__ == "__main__":
    Start_file_monitor()
