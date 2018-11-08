#!/usr/bin/env python
#-*- coding: utf-8 -*-
from geometry import Point2D, PointVec, Vector, VectorTwoPts, RectangleCornerPoint, RectangleEdgePoint, Phrase, Polyline, Rectangle, RectangleRelation, ReverseVector
from rectangleShortestPath import findShortestPath

def constructNormalRec(start_pt_lst, length, width):
    start_pt = Point2D(start_pt_lst)
    vec_lst = []
    length_vec = Vector(length, 0.0)
    width_vec = Vector(0.0, width)
    vec_lst = [length_vec, width_vec, ReverseVector(length_vec), ReverseVector(width_vec)]
    rec = Rectangle(vec_lst, start_pt)
    #print("print(rec.vec_lst): ")
    #for vec in rec.vec_lst:
    #    print(vec)
    return rec

def constructNotNormalRecsSample1():
    start_pt1, start_pt2 = Point2D([-2.989484, 2.030411]), Point2D([-0.040854, -9.81334])
    vec_lst1 = [ Vector(4.523321,-1.382918), Vector(3.008505,9.840376), Vector(-4.523321,1.382918), Vector(-3.008505,-9.840376) ]
    vec_lst2 = [Vector(8.19364, 4.667886), Vector(-2.098816, 3.684097), Vector(-8.19364, -4.667886), Vector(2.098816, -3.684097)]
    rec1 = Rectangle(vec_lst1, start_pt1)
    rec2 = Rectangle(vec_lst2, start_pt2)
    return rec1, rec2

def constructRelation(rec1, rec2):
    relation = RectangleRelation(rec1, rec2)

    """
    print('rec1, rec2:')
    print(relation.rec1, relation.rec2)
    print('relation.cornerVisiable_dict: ')
    print(relation.cornerVisiable_dict)
    print('relation.cornerShortestPath_dict: ')
    print(relation.cornerShortestPath_dict)
    print('relation.corner_vec_dict: ')
    print(relation.corner_vec_dict)

    print('')
    print('relation.isParallel: ')
    print(relation.isParallel)
    print('relation.gapClass: ')
    print(relation.gapClass)
    print('relation.gapDistance: ')
    print(relation.gapDistance)
    """

    """
    print('print(relation.cornerVisiable_dict): ')
    print(relation.cornerVisiable_dict)
    print('print(relation.cornerShortestPath_dict): ')
    for corner1 in relation.cornerVisiable_dict:
        for corner2_i in range(len(relation.cornerVisiable_dict[corner1])):
            corner2 = relation.cornerVisiable_dict[corner1][corner2_i]
            print(corner1, corner2)
            path = relation.cornerShortestPath_dict[corner1][corner2_i]
            print(path.vec_lst[0])
            print(path.vec_lst[1])
    """

    return relation

def testFindShortestPath(relation):
    edge_index1 = 0; length1 = 3.5
    edge_index2 = 1; length2 = 2.2
    path = findShortestPath(relation, edge_index1, length1, edge_index2, length2)
    #print('path: ')
    #print(path)
    print('path.keys: ')
    print(path.__dict__.keys())
    print('path.start_pt.x,y:')
    print(path.start_pt.x, path.start_pt.y)
    print('path.vec_lst: ')
    for vec in path.vec_lst:
        print(vec)

    print('len = ' + str(path.length))
    return path



def main():
    # ZeroDivisionError: float division by zero
    rec1 = constructNormalRec([0.0, 4.0], 4.0, 3.0)
    rec2 = constructNormalRec([10.0, 0.0], 3.0, 5.0)

    #rec1, rec2 = constructNotNormalRecsSample1()
    relation = constructRelation(rec1, rec2)
    testFindShortestPath(relation)
    return
if __name__ == '__main__':
    main()
    
