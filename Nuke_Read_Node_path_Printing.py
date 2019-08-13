import nuke
A = nuke.allNodes("Read")
for i in A:
  path = i['file'].value()
  print path
