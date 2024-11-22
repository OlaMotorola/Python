import unittest


class Poly:
    """Klasa reprezentująca wielomiany."""

    def __init__(self, c=0, n=0):
        if n < 0:
            raise ValueError("Stopień wielomianu musi być nieujemny.")
        self.size = n + 1
        self.a = [0] * self.size
        self.a[n] = c

    def __str__(self):
        """Zwraca wielomian w postaci czytelnej."""
        terms = []
        for i, coeff in enumerate(self.a):
            if coeff == 0:
                continue
            if i == 0:
                terms.append(f"{coeff}")
            elif i == 1:
                terms.append(f"{coeff if coeff != 1 else ''}x")
            else:
                terms.append(f"{coeff if coeff != 1 else ''}x^{i}")
        return " + ".join(terms) or "0"

    def __add__(self, other):
        """Dodawanie wielomianu z innym wielomianem lub liczbą."""
        if isinstance(other, Poly):
            max_size = max(len(self), len(other))
            result = Poly()
            result.a = [0] * max_size
            for i in range(max_size):
                coeff1 = self.a[i] if i < len(self) else 0
                coeff2 = other.a[i] if i < len(other) else 0
                result.a[i] = coeff1 + coeff2
            return result
        elif isinstance(other, (int, float)):
            result = Poly()
            result.a = self.a[:]
            result.a[0] += other
            return result
        else:
            raise ValueError("Dodawanie obsługuje tylko wielomiany i liczby.")

    __radd__ = __add__

    def __sub__(self, other):
        """Odejmowanie wielomianów lub liczby."""
        if isinstance(other, Poly):
            return self + (-other)
        elif isinstance(other, (int, float)):
            return self + (-other)
        else:
            raise ValueError("Odejmowanie obsługuje tylko wielomiany i liczby.")

    def __rsub__(self, other):
        """Odejmowanie liczby od wielomianu."""
        return (-self) + other

    def __mul__(self, other):
        """Mnożenie wielomianów lub liczby."""
        if isinstance(other, Poly):
            result_size = len(self) + len(other) - 1
            result = Poly()
            result.a = [0] * result_size
            for i, coeff1 in enumerate(self.a):
                for j, coeff2 in enumerate(other.a):
                    result.a[i + j] += coeff1 * coeff2
            return result
        elif isinstance(other, (int, float)):
            result = Poly()
            result.a = [coeff * other for coeff in self.a]
            return result
        else:
            raise ValueError("Mnożenie obsługuje tylko wielomiany i liczby.")

    __rmul__ = __mul__

    def __pos__(self):
        """Zwraca wielomian jako dodatni."""
        return self

    def __neg__(self):
        """Neguje wielomian."""
        result = Poly()
        result.a = [-coeff for coeff in self.a]
        return result

    def is_zero(self):
        """Sprawdza, czy wielomian jest zerowy."""
        return all(coeff == 0 for coeff in self.a)

    def __eq__(self, other):
        """Sprawdza równość wielomianów."""
        if not isinstance(other, Poly):
            return False
        return self.a == other.a

    def eval(self, x):
        """Oblicza wartość wielomianu dla x (schemat Hornera)."""
        result = 0
        for coeff in reversed(self.a):
            result = result * x + coeff
        return result

    def combine(self, other):
        """Łączy dwa wielomiany."""
        if not isinstance(other, Poly):
            raise ValueError("Argument musi być instancją Poly.")
        result = Poly()
        for i, coeff in enumerate(self.a):
            if coeff != 0:
                result += Poly(coeff) * (other ** i)
        return result

    def __pow__(self, n):
        """Podnoszenie wielomianu do potęgi."""
        if not isinstance(n, int) or n < 0:
            raise ValueError("Wykładnik musi być liczbą całkowitą nieujemną.")
        result = Poly(1, 0)  # Jedynka wielomianowa
        base = self
        while n > 0:
            if n % 2 == 1:
                result *= base
            base *= base
            n //= 2
        return result

    def diff(self):
        """Różniczkowanie wielomianu."""
        if len(self) <= 1:
            return Poly(0, 0)
        result = Poly()
        result.a = [i * coeff for i, coeff in enumerate(self.a)][1:]
        return result

    def integrate(self):
        """Całkowanie wielomianu."""
        result = Poly()
        result.a = [0] * (len(self) + 1)  # Tworzymy tablicę o jeden dłuższą
        for i, coeff in enumerate(self.a):
            result.a[i + 1] = int(coeff / (i + 1))  # Operacja dzielenia zwraca float
        return result

    def __len__(self):
        """Rozmiar wielomianu."""
        return len(self.a)

    def __getitem__(self, i):
        """Zwraca współczynnik przy x^i."""
        return self.a[i] if 0 <= i < len(self) else 0

    def __setitem__(self, i, value):
        """Ustawia współczynnik przy x^i."""
        if i < 0:
            raise IndexError("Indeks musi być nieujemny.")
        if i >= len(self):
            self.a.extend([0] * (i + 1 - len(self)))
        self.a[i] = value

    def __call__(self, x):
        """Oblicza wartość wielomianu (eval) lub składa wielomiany (combine)."""
        if isinstance(x, (int, float)):
            return self.eval(x)
        elif isinstance(x, Poly):
            return self.combine(x)
        else:
            raise ValueError("Argument musi być liczbą lub wielomianem.")

    def __iter__(self):
        """Umożliwia iterację po współczynnikach wielomianu."""
        return iter(self.a)


class TestPoly(unittest.TestCase):
    def test_init(self):
        p = Poly(3, 2)  # 3x^2
        self.assertEqual(p.a, [0, 0, 3])

    def test_str(self):
        p = Poly(3, 2) + Poly(2, 1) + Poly(1, 0)  # 3x^2 + 2x + 1
        self.assertEqual(str(p), "1 + 2x + 3x^2")

    def test_add(self):
        p1 = Poly(2, 1)  # 2x
        p2 = Poly(3, 0)  # 3
        self.assertEqual((p1 + p2).__str__(), "3 + 2x")

    def test_sub(self):
        p1 = Poly(3, 1)  # 3x
        p2 = Poly(2, 0)  # 2
        self.assertEqual((p1 - p2).__str__(), "-2 + 3x")

    def test_mul(self):
        p1 = Poly(1, 1)  # x
        p2 = Poly(2, 0)  # 2
        self.assertEqual((p1 * p2).__str__(), "2x")

    def test_pos_neg(self):
        p = Poly(3, 1)  # 3x
        self.assertEqual((+p).__str__(), "3x")
        self.assertEqual((-p).__str__(), "-3x")

    def test_is_zero(self):
        p1 = Poly(0, 0)  # 0
        p2 = Poly(1, 1)  # x
        self.assertTrue(p1.is_zero())
        self.assertFalse(p2.is_zero())

    def test_eq_ne(self):
        p1 = Poly(2, 1)  # 2x
        p2 = Poly(2, 1)  # 2x
        p3 = Poly(3, 1)  # 3x
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)
        self.assertTrue(p1 != p3)

    def test_eval(self):
        p = Poly(3, 2) + Poly(2, 1) + Poly(1, 0)  # 3x^2 + 2x + 1
        self.assertEqual(p.eval(2), 17)

    def test_iter(self):
        p = Poly(3, 2) + Poly(2, 1) + Poly(1, 0)  # 3x^2 + 2x + 1
        coeffs = [coeff for coeff in p]
        self.assertEqual(coeffs, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
