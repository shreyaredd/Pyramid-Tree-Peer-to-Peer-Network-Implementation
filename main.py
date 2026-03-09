class Node: 
    def __init__(self, logical_address, ip_address, resource_type, connections=None): 
        self.logical_address = logical_address 
        self.ip_address = ip_address 
        self.resource_type = resource_type 
        self.connections = connections if connections else [] 

class GlobalResourceTable: 
    def __init__(self): 
        self.table = {} 

    def add_entry(self, logical_address, ip_address, resource_type, connections): 
        self.table[logical_address] = { 
            'Logical Address': logical_address, 
            'IP Address': ip_address, 
            'Resource Type': resource_type, 
            'Connections': connections 
        } 

    def print_table(self): 
        print("--- Global Resource Table (Network Topology) ---") 
        for addr, entry in self.table.items(): 
            print(f"Node {addr}: IP={entry['IP Address']}, Resource={entry['Resource Type']}, Neighbors={entry['Connections']}") 
        print("-" * 50) 

    def dfs_search(self, current_addr, target_resource, visited=None):
        if visited is None:
            visited = set()
        
    
        visited.add(current_addr)
        node_data = self.table[current_addr]

        print(f"Checking Node {current_addr}...")

        
        if node_data['Resource Type'] == target_resource:
            return node_data

        
        for neighbor in node_data['Connections']:
            if neighbor not in visited:
                result = self.dfs_search(neighbor, target_resource, visited)
                if result:
                    return result
        
        return None

def create_network(): 
   
    nodes = {}
    for i in range(15):
        nodes[i] = Node(logical_address=i, ip_address=f"192.168.0.{i+1}", resource_type=str(i))

    
    for i in range(15):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < 15:
            nodes[i].connections.append(nodes[left])
            nodes[left].connections.append(nodes[i]) # Backlink
        if right < 15:
            nodes[i].connections.append(nodes[right])
            nodes[right].connections.append(nodes[i]) # Backlink

    global_table = GlobalResourceTable() 
    for node in nodes.values(): 
        global_table.add_entry( 
            node.logical_address, node.ip_address, node.resource_type, 
            [conn.logical_address for conn in node.connections] 
        ) 
    return global_table 

if __name__ == "__main__": 
    network = create_network() 
    network.print_table() 

    try:
        start_node = int(input("Enter the logical address to start search from (0-14): "))
        target_res = input("Enter the resource type to find (0-14): ")
        
        print(f"\nStarting DFS Search from Node {start_node}...")
        
        found_node = network.dfs_search(start_node, target_res)

        if found_node:
            print(f"\nSUCCESS: Resource '{target_res}' found at Node {found_node['Logical Address']} (IP: {found_node['IP Address']})")
        else:
            print("\nFAILURE: Resource not found in the network.")
            
    except (ValueError, KeyError):
        print("Invalid input. Please use numeric addresses between 0 and 14.")
