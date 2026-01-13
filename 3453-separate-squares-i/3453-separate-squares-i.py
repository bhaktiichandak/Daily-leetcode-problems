class Solution:
    def separateSquares(self, squares):
        def area_diff(h):
            below = 0
            total = 0
            for _, y, l in squares:
                total += l * l
                if h > y:
                    below += min(h - y, l) * l
            return below - (total - below)

        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        for _ in range(60):  # enough for 1e-5 precision
            mid = (low + high) / 2
            if area_diff(mid) >= 0:
                high = mid
            else:
                low = mid

        return low
