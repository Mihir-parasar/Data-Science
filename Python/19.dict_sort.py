d = {'apple': 15, 'banana': 10, 'cherry': 20}
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))


print(f"original dictionary:{d}")
print(f"sorted dictionary: {sorted_d}")