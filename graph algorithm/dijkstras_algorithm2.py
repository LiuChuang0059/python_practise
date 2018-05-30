# -*- coding: utf-8 -*-
"""
Created on Fri May 25 22:17:22 2018

@author: 刘闯

狄克斯特拉算法 


"""

# the graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# the costs table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# the parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None


procceded=[]    ### 标记过的节点



def find_lowest_cost_node(costs):  ###找到最近的节点
    lowest_cost=float("inf")  ##无穷  节点消耗
    lowest_cost_node=None   ###节点
    for n in costs:          
        cost=costs[n]
        if cost < lowest_cost and n not in procceded:
            lowest_cost=cost
            lowest_cost_node=n
    return lowest_cost_node


node=find_lowest_cost_node(costs)
while node is not None:  ###遍寻所有节点
    cost=costs[node]  ###节点消耗
    neighbors=graph[node]  ###节点邻居
    for n in neighbors.keys():  ###节点邻居消耗更新
        new_cost=cost+neighbors[n]   
        if new_cost < costs[n] :
            costs[n]=new_cost
            parents[n]=node    ###更新父节点
    procceded.append(node)  ### 去除节点
    node=find_lowest_cost_node(costs)
 
print(costs)
print(cost)
print(parents)








