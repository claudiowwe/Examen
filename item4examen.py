from ncclient import manager
import xml.dom.minidom
m = manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )

print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    print(capability) 

print("-------------------------------------")
netconf_reply = m.get_config(source="running")


netconf_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>RiveraSanMartinMoyanoCodocedo</hostname>
  </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_hostname)

print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())