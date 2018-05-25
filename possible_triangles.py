def possible_triangles(sides):
    answer = 0

    # adds up the smaller sides
    sides.sort()

    for side1 in range(len(sides)):
        for side2 in range(side1 + 1, len(sides)):
            for side3 in range(side2 + 1, len(sides)):
                if sides[side1] + sides[side2] > sides[side3]:
                    print(sides[side1],end= " ")
                    print(sides[side2],end= " ")
                    print(sides[side3])
                    answer += 1

    return answer

if __name__ == "__main__":
    print(possible_triangles([4,6,3,7]))
    print(possible_triangles([4,7,3,6]))