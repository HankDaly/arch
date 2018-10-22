﻿"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "htwt"
__version__ = "2018.10.22"

import rhinoscriptsyntax as rs
from genicStructGh import child_main

def createHash(keys, values):
    mp = {}
    n = len(keys)
    for i in range(n):
        mp[keys[i]] = values[i]
    return mp
def getDicts():
    road_dict = createHash(road_node_key, road_bet_node)
    place_dict = createHash(place_index_key, place_pt)
    return road_dict, place_dict


def getPlacePtLst(place_lst, place_dict):
    return [place_dict[str(place[0]) + ',' + str(place[1])] for place in place_lst]
def getRoadCurve(trans_path, road_dict):
    # 根据路径结点序号得到一条路径线段
    curve_lst = []
    trans_path = ([9, 0, 70, 79, 91, 77, 8, 60, 56, 58, 47, 43, 29, 61, 50, 54, 78, 81, 80], 3660.0) 
    n = len(trans_path[0])
    for i in range(n-1):
        node, next = trans_path[0][i], trans_path[0][i+1]
        s1, s2 = str(node) + ',' + str(next), str(next) + ',' + str(node)
        cur = road_dict[s1] if s1 in road_dict else road_dict[s2]      # 0->9 or 9->0
        curve_lst.append(cur)
    join_curve = rs.JoinCurves(curve_lst)
    length = rs.CurveLength(join_curve)
    #print(length)
    #t = 0.5
    #pt = rs.CurveArcLengthPoint(join_curve, t*length)
    return join_curve

def main():
    dicts_lst = getDicts()
    road_dict, place_dict = dicts_lst[0], dicts_lst[1]
    
    child_main_lst = child_main()
    breakup = child_main_lst[0]
    seq_time = child_main_lst[1]
    trans_time = child_main_lst[2]
    place = child_main_lst[3]

    
    #print('breakup:')
    #print(breakup)
    #print('seq_time:')
    #print(seq_time)
    #print('trans_time:')
    #print(trans_time)
    print('place:')
    print(place)
    trans_path = ([9, 0, 70, 79, 91, 77, 8, 60, 56, 58, 47, 43, 29, 61, 50, 54, 78, 81, 80], 3660.0)
    
    # place_pt_lst: 该对象静态事件发生的点序列
    # road_curve:   该对象交通事件对应的路径线段
    place_pt_lst = getPlacePtLst(place, place_dict)
    road_curve = getRoadCurve(trans_path, road_dict)

    """
    # 设置帧数
    time_step = 0.1   # 0.1h/帧 = 6min/帧
    #time_step = 1     # 1h/帧
    #time_step = 1/60   # 1min/zhen
    tot_time = 24     # 记录一天的变化
    
    # 构造打点时间序列
    temp_sum = 0
    clock_time_range = []
    while temp_sum < tot_time:
        clock_time_range.append(temp_sum)
        temp_sum = temp_sum + time_step
    
    # child.isArrangeValid, child.breakup, child.time, child.trans_time, child.trans_speed, child.place, child.trans_path
    # 根据child.place得到区块点表(pace_pt_lst), 根据child.trans_path得到道路多段线(road_curve_lst)
    # evaluateCurveByLength() 组合line成polyline, 根据距离得到线上对应点
    # 获得确定起床点, 事件和交通情况下, 时间结点序列
    seqTime = [0, breakup]
    temp_sum = breakup
    for i in range(len(seq_time)-1):
        temp_sum = temp_sum + seq_time[i]
        seqTime.append(temp_sum)
        temp_sum = temp_sum + trans_time[i]
        seqTime.append(temp_sum)
    seqTime.append(temp_sum + seq_time[-1])
    # print(seqTime[-1]-breakup)   # right

    pt_lst = []       # 一个人的每一帧的点
    seq_p = 0         # 在序列上标记时间的指针
    for t in clock_time_range:
        while seqTime[seq_p+1] <= t:   # 用指针找到对应区间
            seq_p = seq_p + 1
        # seqTime[seq_p] <= t < seqTime[seq_p+1]
        if seq_p == 0:                 # 起床前睡觉地点(基因条未计算)
            pt = place_pt_lst[-1]
        else:                          # 一天的正常作息
            if seq_p % 2 == 1:  # 静事件
                pt = place_pt_lst[int((seq_p-1)/2)]
            else:               # 交通事件
                road_curve = road_curve_lst[int((seq_p-1)/2)]
                scale_t = (t-seqTime[seq_p]) / trans_time[int((seq_p-1)/2)]
                #domain = rs.CurveDomain(road_curve)
                #pt = rs.EvaluateCurve(road_curve, domain[1]*scale_t)
                length = trans_path[int((seq_p-1)/2)][1]*scale_t
                pt = rs.CurveArcLengthPoint(road_curve, length)
        pt_lst.append(pt)
    """
    return road_curve
    

a = main()
