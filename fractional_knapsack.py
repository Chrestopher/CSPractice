"""
The fractional knapsack problem involves finding the highest value you can put inside a bag with max capacity. This is a greedy algorithm
problem that requires sorting the best value to weight ratio and filling the bag with the best item until it can't fit anymore then moving
onto the next item.
"""


def fractional_knapsack(capacity, items):
    """
    Finds the selection of items that would fit in the knapsack capacity and have the most value.
    n refers to the number of items in the final bag
    Time complexity: O(nlogn)   The list of items is sorted by non-increasing value per weight O(nlogn), then each item is placed
    into the knapsack until it cant fit and moves onto the next item O(n)
    Space complexity: O(n) - the size of the final knapsack
    :param capacity: the weight of the knapsack
    :param items: the list of items that can be in the knapsack
    :return:
    """
    items = sorted(items, key=lambda i: i["ratio"], reverse=True)

    knapsack = {}
    max_value = 0

    for item in items:
        while item["weight"] <= capacity:
            max_value += item["value"]
            capacity -= item["weight"]
            if item["name"] in knapsack:
                knapsack[item["name"]] += 1
            else:
                knapsack[item["name"]] = 1

    print("Items in backpack")
    for k, v in knapsack.items():
        print(k + ": " + str(v))

    print()
    print("Max value: " + str(max_value))


if __name__ == '__main__':
    print("Testing with rock, paper, and scissors. Max value should be 2130")
    print()
    rock = {"name": "Rock", "weight": 50, "value": 100, "ratio": 2}
    paper = {"name": "Paper", "weight": 5, "value": 15, "ratio": 3}
    scissors = {"name": "Scissors", "weight": 30, "value": 150, "ratio": 5}
    bag = [scissors, paper, rock]
    max_weight = 430
    fractional_knapsack(max_weight, bag)
    print()

    print("Testing with bananas, apples, and strawberries. Max value should be 2417")
    print()
    bananas = {"name": "Bananas", "weight": 1, "value": 1, "ratio": 1}
    apples = {"name": "Apples", "weight": 7, "value": 15, "ratio": 2.14}
    strawberries = {"name": "Strawberries", "weight": 31, "value": 150, "ratio": 4.84}
    bag = [bananas, apples, strawberries]
    max_weight = 505
    fractional_knapsack(max_weight, bag)
