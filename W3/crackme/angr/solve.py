#!/usr/bin/python


import angr


proj = angr.Project('ProtectionSystem.II.exe')
print(proj.arch)
print(hex(proj.entry))
print(proj.loader)

state = proj.factory.blank_state(addr=0x4010A3)
v_login = state.se.BVS("login", 9*8)
v_pass = state.se.BVS("pass", 9*8)
print(state.se)

print(state)
path_group = proj.factory.path_group(state)
path_group.explore(find=0x401160, avoid=[0x401189, 0x4011B2])

print(path_group)
print(path_group.found)
