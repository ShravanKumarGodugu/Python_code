import nuke

read_nodes = nuke.allNodes('Read')
print '\n Read Node paths are'
for i in read_nodes:
  read_node_path = i['file'].value()
  print read_node_path

deep_nodes = nuke.allNodes('DeepRead')
print '\n Deep_Read Node paths are'
for i in deep_nodes:
  deepread_node_path = i['file'].value()
  print deepread_node_pathread_node_path
  
