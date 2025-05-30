with open('D:\\programming\\filespy\\data_prog_contest_problem_1.txt', 'r') as file:
    linends0 = str(file.read()).split()
linends = []

for i in linends0:
    linends.append(int(i))
    
lineamnt = linends.pop(0)
linends = [linends[i:i+2] for i in range(0, len(linends), 2)]


def min_cover_points(segments):
    segments.sort(key=lambda seg: seg[1])

    points = []
    for L, R in segments:
        if not points or points[-1] < L:
            points.append(R)
    return points

print(min_cover_points)
print (len(min_cover_points(linends)))