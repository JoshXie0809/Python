from tool.Point import Point


def main():
    p1 = Point(0, 0)

    count = 0
    while count < 10:
        count += 1

        x = int(input("x : "))
        y = int(input("y : "))
        p2 = Point(x, y)
        print(p1.distanceCalc(p2))
        print(p2.now())


if __name__ == '__main__':
    main()
