import Algorithms.Sort as Sort
import data
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
matplotlib.use("TkAgg")

if __name__ == "__main__":
    msg = "Select sorting method number:\n1. Bubble\t2. Merge\t3. Heap\n4. Quick\t5. Insertion\t6. Cocktail Sort\n"
    selection = input(msg)
    arr = data.get_data()

    if selection == '1':
        title = "Bubble Sort"
        sort_type = Sort.Bubble_Sort.sort(arr)
    elif selection == '2':
        title = "Merge Sort"
        sort_type = Sort.Merge_Sort.sort(arr)
    elif selection == '3':
        title = "Heap Sort"
        sort_type = Sort.Heap_Sort.sort(arr)
    elif selection == '4':
        title = "Quick Sort"
        sort_type = Sort.Quick_Sort.sort(arr)
    elif selection == '5':
        title = "Insertion Sort"
        sort_type = Sort.Insertion_Sort.sort(arr)
    elif selection == '6':
        title = "Cocktail Shaker Sort"
        sort_type = Sort.Cocktail_Sort.sort(arr)
    else:
        title = ""
        sort_type = None

    figure, ax = plt.subplots()
    rec = ax.bar(range(len(arr)), arr, align="edge")
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    ax.set_title(title)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 110)

    def update_figure(arr, rec, iteration):
        for rec, val, in zip(rec, arr):
            rec.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")


    anim = animation.FuncAnimation(figure, func=update_figure,
                                   fargs=(rec, iteration), frames=sort_type, interval=1,
                                   repeat=False)
    plt.show()
