if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

    print [[m, q, p] for m in range(x + 1) for q in range(y + 1) for p in range(z + 1) if ((m + q + p) != n )]
