# this is the file that will be run by Mimir
import math

#Calculate the cost between two cities and return the list of options we can take.
def costCalculater(cityList, distanceConst,elevationConst):

    #calculating the cost between two cities
    def cost(startCity, endCity, distanceConst, elevationConst):
        start, x1, y1, z1 = startCity
        x1, y1, z1 = int(x1), int(y1), int(z1)
        end, x2, y2, z2 = endCity
        x2, y2, z2 = int(x2), int(y2), int(z2)
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        costCount = round(distanceConst * distance + elevationConst * ((z2 - z1) ** 2))
        option = [start, end, costCount]
        return option

    #making a list of options
    optionList=[]
    for item in cityList:
        start = cityList.index(item) + 1
        end = len(cityList)
        startCity = item
        for i in range(start, end):
            endCity = cityList[i]
            result = cost(startCity, endCity, distanceConst, elevationConst)
            optionList.append(result)

    return optionList

#converting option list to a adjacency matrix
def adjacencyMatrix(options):
    graph = [
        [0] * 5,
        [0] * 5,
        [0] * 5,
        [0] * 5,
        [0] * 5,
    ]
    cities = ['Davis', 'Sacramento', 'LA', 'Tahoe', 'San Francisco']
    for item in options:
        x_axis = cities.index(item[0])
        y_axis = cities.index(item[1])
        graph[y_axis][x_axis] = item[2]
        graph[x_axis][y_axis] = item[2]
    return graph

#finding the minimum expamsion tree using prims algorithem
def minnode(n, key_val, mst_set):
    minmum = 100000000000000000
    minmum_index = None

    for i in range(n):
        if (mst_set[i] == False and key_val[i] < minmum):
            minmum = key_val[i]
            minmum_index = i
    return minmum_index


def findPath(count, city):
    parent = [None] * count

    key_val = [100000000000000000] * count

    mst_set = [False] * count

    parent[0] = -1
    key_val[0] = 0

    for i in range(count - 1):

        u = minnode(count, key_val, mst_set)

        mst_set[u] = True

        for v in range(count):
            if (city[u][v] and mst_set[v] == False and city[u][v] < key_val[v]):
                key_val[v] = city[u][v]
                parent[v] = u

    cordinates=[]
    for i in range(1, count):
        cordinates.append([parent[i],i])

    return cordinates

#drawing the map between cities usuing the out put of minimum expnsion tree
def mappingPath(codinates,cityList):
    city=['Davis', 'Sacramento', 'LA', 'Tahoe', 'San Francisco']
    total_Cost=0
    mapDic={}
    for item in codinates:
        x_cordinate=item[0]
        y_cordinate=item[1]

        mapDic[cityList[x_cordinate][y_cordinate]]=f"{city[x_cordinate]} -> {city[y_cordinate]}"
        total_Cost+=cityList[x_cordinate][y_cordinate]

    print("We should build the following roads:")
    for road in sorted(mapDic):
        print(mapDic[road],end=" =")
        print(f"${road}")
    print(f"For a total cost of ${total_Cost}")

def main():
    # seting city numbers to 5
    count = 5

    cityList = []

    # talking inputs from the txt file
    f = open('test_countries/California.txt', 'r')
    details = []
    for line in f:
        cityDetails = line.strip()
        details.append(cityDetails)
    distanceConst = int(details[0])
    elevationConst = int(details[1])

    # spliting the input and enter the cordinates of cities to city list under appropriate citys
    for item in details[2:]:
        sc = item.split(',')
        cityList.append(sc)

    # getting the option list with costClaculater function
    options = costCalculater(cityList, distanceConst, elevationConst)

    # converting options list to a adjacency matrix
    city = adjacencyMatrix(options)

    # find the ccordinates for cheepest path using findPath function
    cordinates = findPath(count, city)

    # printing the map and costs using map function
    mappingPath(cordinates, city)

if __name__=='__main__':
    main()
