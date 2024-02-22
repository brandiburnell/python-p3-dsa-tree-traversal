class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    result = {}
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      if node['id'] == id:
        result.update(node)
      nodes_to_visit = nodes_to_visit + node['children']
    
    if len(result) == 0:
      return None
    return result
    
