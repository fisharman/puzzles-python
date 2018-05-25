def moveTowers(disks, start, end, spare):
    if disks == 1:
        print("{} to {}".format(start, end))
        return

    moveTowers(disks-1, start, spare, end)
    print("{} -> {}".format(start, end))
    moveTowers(disks-1, spare, end, start)

if __name__ == "__main__":
    moveTowers(3, "A", "B", "C")