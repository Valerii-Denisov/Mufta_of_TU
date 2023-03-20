def math_resist(r_normative, m, k, k_n):
    print((r_normative * m) / (k * k_n))
    return (r_normative * m) / (k * k_n)

def math_thickness(r_normative, m, k, k_n, diam, n, p):
    return (n * p * diam) / (2 * (math_resist(r_normative, m, k, k_n) + n * p))


print(math_thickness(590, 0.825, 1.4, 1.1, 530, 1.1, 7.5))