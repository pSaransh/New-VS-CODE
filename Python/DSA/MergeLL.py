from typing import Optional
from Node import Node
def mergeList(ll1:Node,ll2:Node)->Optional[Node]:
    ll3 = Node()
    while ll1.next is None and ll2 is not None:
        ll5 = ll3.next
        if(ll1.data<ll2.data):
            ll4 = Node(ll1.data)
            ll5 = ll4
        else:
            ll4 = Node(ll2.data)
            ll5 = ll4
        ll3.next = ll5
    return ll3