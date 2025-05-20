import jieba

def func():
    n = int(input())
    line_stations = []
    station_to_lines = {}
    for i in range(n):
        stations = input().split()
        line_stations.append(stations)
        for station in stations:
            if station not in station_to_lines:
                station_to_lines[station] = []
            station_to_lines[station].append(i)

    s, t = input().split()

    visited = {}
    heap = []
    for line in station_to_lines.get(s, []):
        cost = 2
        path = [(s, line)]
        heapq.heappush(heap, (cost, path, s, line))
        visited[(s, line)] = cost

    min_cost = None
    best_path = None

    while heap:
        cost, path, cur_station, cur_line = heapq.heappop(heap)
        if cur_station == t:
            if min_cost is None or cost < min_cost:
                min_cost = cost
                best_path = path
            continue

        stations = line_stations[cur_line]
        idx = stations.index(cur_station)
        if idx > 0:
            next_station = stations[idx -1]
            new_cost = cost
            new_path = path+[(next_station, cur_line)]
            key = (next_station, cur_line)
            if key not in visited or new_cost < visited[key]:
                visited[key] = new_cost
                heapq.heappush(heap, (new_cost, new_path, next_station, cur_line))

        if idx < len(stations) -1:
            next_station = stations[idx+1]
            new_cost = cost
            new_path = path+[(next_station, cur_line)]
            key = (next_station, cur_line)
            if key not in visited or new_cost < visited[key]:
                visited[key] = new_cost
                heapq.heappush(heap, (new_cost, new_path, next_station, cur_line))

        for other_line in station_to_lines[cur_station]:
            if other_line != cur_line:
                new_cost = cost+1
                new_path = path+[(cur_station, other_line)]
                key = (cur_station,other_line)
                if key not in visited or new_cost < visited[key]:
                    visited[key] = new_cost
                    heapq.heappush(heap, (new_cost, new_path, cur_station, other_line))

    if best_path is None:
        print("NA")
    else:
        output = [best_path[0][0]]
        for i in range(1, len(best_path)):
            prev_station, prev_line = best_path[i-1]
            cur_station, cur_line = best_path[i]
            if cur_line != prev_line:
                output.append(prev_station)
            output.append(cur_station)

        final_output = [output[0]]
        for s in output[1:]:
            if s != final_output[-1]:
                final_output.append(s)

        print('-'.join(final_output))
        print(min_cost)

if __name__ == '__main__':
    func()