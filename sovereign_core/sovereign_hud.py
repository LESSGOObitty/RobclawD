import os, sys, time, json

def draw_hud():
    while True:
        os.system('clear')
        print("\033[92m========================================================================\033[0m")
        print("\033[1m              ROBDOE.COM // SOVEREIGN TERMINAL NODE HUD                  \033[0m")
        print("\033[92m========================================================================\033[0m")
        try:
            with open(os.path.expanduser("~/robdoe_telemetry.json"), "r") as f:
                data = json.load(f)
                print(f" [AUTHORITY]         : \033[93m{data.get('domain_authority')}\033[0m")
                print(f" [ACTIVE INVARIANT]  : \033[96m{data.get('invariant')}\033[0m")
                print(f" [SHA256 DAG ROOT]   : \033[94m{data.get('sha256_root')[:36]}...\033[0m")
                print(f" [PROVMARK VAULT]    : {data.get('local_dag_depth')} Records Sealed")
                print("------------------------------------------------------------------------")
                print(f" [SERIAL PORT]       : {data['channels']['serial_esp32']}")
                print(f" [LAN MESH]          : {data['channels']['lan_udp_mesh']}")
                print(f" [RUNTIME ENGINE]    : {data['channels']['termux_arm64']}")
        except Exception as e:
            print(f" [STATUS]            : WAITING FOR MASTER LOOP ({e})")
        print("\033[92m========================================================================\033[0m")
        print(" Press [CTRL+C] to exit HUD.")
        time.sleep(2)

if __name__ == "__main__":
    try:
        draw_hud()
    except KeyboardInterrupt:
        sys.exit(0)
