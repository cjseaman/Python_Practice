# Merge sort implementation in python by Collin Seaman


def msort(unsorted):
    if len(unsorted) > 1:
        mid = len(unsorted) // 2
        lower = unsorted[:mid]
        upper = unsorted[mid:]
        msort(lower)
        msort(upper)
        i = j = k = 0
        while i < len(lower) and j < len(upper):

            if lower[i] < upper[j]:
                unsorted[k] = lower[i]
                k = k + 1
                i = i + 1
            elif lower[i] > upper[j]:
                unsorted[k] = lower[i]
                k = k + 1
                j = j + 1

        while i < len(lower):
            unsorted[k] = lower[i]
            k = k + 1
            i = i + 1
        while j < len(upper):
            unsorted[k] = upper[j]
            k = k + 1
            j = j + 1