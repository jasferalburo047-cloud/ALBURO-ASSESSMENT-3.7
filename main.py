def prepare_name_array(full_name):
    unsorted_arr = []

    allowed_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in full_name.upper():
        if char in allowed_letters and char not in unsorted_arr:
            unsorted_arr.append(char)

    return unsorted_arr


def selection_sort(arr):

    sorted_arr = arr.copy()
    n = len(sorted_arr)

    print("--- Selection Sort Process ---")
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j

        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
        print(f"Pass {i + 1}: {sorted_arr}")

    return sorted_arr


def main():
    full_name = "JASFER ALBURO"


    unsorted_array = prepare_name_array(full_name)
    sorted_array = selection_sort(unsorted_array)

    print("\n--- Final Result ---")
    print(f"Full Name:      {full_name}")
    print(f"Unsorted Array: {unsorted_array}")
    print(f"Sorted Array:   {sorted_array}")


if __name__ == "__main__":
    main()