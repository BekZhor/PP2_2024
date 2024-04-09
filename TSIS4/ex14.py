import json

with open("sample_data.json", "r") as f:
    data = json.loads(f)

    print("Interface Status")
    print("================================================================================")
    print("DN                                                 Description           Speed    MTU")  
    print("-------------------------------------------------- --------------------  ------  ------")


    for interface in data.get('imdata', []):
        l1phy = interface.get('l1PhysIf', {})
        att = l1phy.get('attributes', {})
    
        name = att.get('name', '-')
        description = att.get('description', '-')
        speed = att.get('speed', '-')
        mtu = att.get('mtu', '-')
    
        print(f'{name:<50} {description:<20} {speed:<8} {mtu:<6}')