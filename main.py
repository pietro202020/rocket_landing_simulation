import matplotlib.pyplot as plt


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def time_to_reach_distance_num(h, v, a):
    if v < 0:
        return -1

    time = -1
    timestamp = 0.2
    while h >= 0 and v >= 0:
        v += a * timestamp
        h -= v * timestamp

        time += timestamp
    return time


def time_to_reach_with_thrust(h, v):


    time_stamp = 0.2
    print("\tFsum:", Fsum)
    if v < 0:
        return 0
    time = -1
    while v > 0:
        v += Fsum * time_stamp
        h -= v * time_stamp
        if h <= 0:
            print("TOO LESS POWER TO STOP BEFORE CRUSH!!!")
            return -1


        time += time_stamp
    return time


def F(velocity, distance):
    # Required to be thrust to land safely
    if distance <= 0:
        return 0  # If distance is 0 or negative, no thrust is needed (already landed)
    else:
        required_thrust = Ms * (velocity ** 2) / (2 * distance)
        return required_thrust  # Limit thrust to maximum 1500 Newtons



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    G = 6.67 * pow(10, -11)  # stała grawitacyjna

    # timestamp = 5  # czas miedzy pomiarami
    tSimEnd = 300
    t_step = 1
    t = 0
    hStart = 4000  # wysokosc poczatkowa
    vStart = 10  # predkosc m/s poczatkowa, dodatnia gdy zbliza się

    Ms = 1000  # masa łazika
    Mp = 6.41 * pow(10, 23)  # masa planety
    Rp = 3389000  # km promien
    g = G * Mp / (Rp * Rp)  # grawitacja planety

    hCurr = hStart
    vCurr = vStart
    aCurr = g

    Fmax = 15000  # N maksymalna przepustnica
    Fcurr = 0  # obecna przepustnica

    Fsum =  -Fmax / Ms + g

    time_to_distance_num = time_to_reach_distance_num(hStart, vCurr, aCurr)
    thrust_time_to_distance_num = time_to_reach_with_thrust(hStart, vCurr)
    # time_to_distance_an = time_to_reach_distance_an(hStart, vCurr, aCurr)

    dt = []
    h = []
    v = []  # na plusie, gdy spada
    a = []
    f = []

    thrust_activated = False

    while (t < tSimEnd):
        print("\n", t, ":\tt num:", time_to_distance_num)
        print("\tthrust:", thrust_time_to_distance_num)
        # print(t, ":\tt an:", time_to_distance_an )
        print("\td:", hCurr)
        print("\tv:", vCurr)
        time_to_distance_num = time_to_reach_distance_num(hCurr, vCurr, aCurr)
        thrust_time_to_distance_num = time_to_reach_with_thrust(hCurr, vCurr)
        # time_to_distance_an = time_to_reach_distance_an(hCurr, vCurr, aCurr)
        dt.append(t)

        a.append(aCurr)
        v.append(vCurr)
        h.append(hCurr)
        f.append(F(vCurr, hCurr) / Ms)

        if time_to_distance_num <= thrust_time_to_distance_num and vCurr > 0 and hCurr > 0:
            aCurr = Fsum
        else:
            aCurr = g  # (F(vCurr, hCurr) / Ms)
        vCurr += aCurr * t_step
        hCurr -= vCurr * t_step

        t += t_step

        if hCurr <= 0 and vCurr > 10:
            print("crash")
            break
        else:
            if hCurr <= 0:
                print("Landed!")
                break

    plt.subplot(1, 4, 1)
    plt.plot(dt, h)
    plt.title("Wysokość")
    plt.xlabel("Czas [s]")
    plt.ylabel("Wysokość [m]")
    plt.grid(True)

    #
    plt.subplot(1, 4, 2)
    plt.plot(dt, v)
    plt.title("prędkość")
    plt.xlabel("Czas [s]")
    plt.ylabel("v")
    plt.grid(True)

    plt.subplot(1, 4, 3)
    plt.plot(dt, a)
    # plt.legend(["u_pi", "u"])
    plt.title("przyspieszenie")
    plt.xlabel("Czas [s]")
    plt.ylabel("a")
    plt.grid(True)


    plt.show()