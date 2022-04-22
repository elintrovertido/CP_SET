from collections import deque

def distance(nodes,source,tree):
    q = deque()
    dis = [0]*(nodes+1)
    q.append(source)
    
    while q:
        cur = q.popleft()
        for node in tree[cur]:
            q.append(node)
            dis[node] += dis[cur] +1
    return dis


if __name__ == "__main__":
    nodes = int(input())
    tree = dict()
    
    for i in range(1,nodes+1):
        tree[i] = []
    
    for i in range(nodes-1):
        a,b = tuple(map(int,input().split()))
        tree[a].append(b)
    # print(tree)

    print(distance(nodes,1,tree)) 
    


