def go():
    ladders = {1: 38, 4: 14, 9: 32, 21: 42, 28: 84, 51: 67, 80: 99, 72: 91}

    level = {0:0}
    snakes = {17: 7, 62: 19, 87: 36, 54: 34, 64: 60, 95: 75, 93: 73, 98: 79}
    parent = {0:None}
    frontier = [0]
    f =1
    while frontier:
        next =[]
        for u in frontier:
            if u <100:
                for i in range(u ,u+7):
                    if i not in level:
                        if i in ladders or i in snakes:
                            if i in ladders:
                                level[i]= f
                                level[ladders[i]]=f
                                parent[ladders[i]]= u
                                next.append(ladders[i])
                            if i in snakes:
                                level[i]= f
                                if snakes[i] not in level:
                                    level[snakes[i]]= f
                                    parent[snakes[i]]= u
                                    next.append(snakes[i])
                        else:
                            level[i]=f
                            parent[i]=u
                            next.append(i)
        frontier = next
        f+=1
    print("the minimum throws to win :{} \nthe shortest path :".format(level[100]))
    shortest_path(parent ,0 , 100)


def shortest_path(parent, src, dest):
    if src == dest:
        return
    else:
        shortest_path(parent ,src , parent[dest])
        print(dest)

if __name__ == '__main__':
    go()
