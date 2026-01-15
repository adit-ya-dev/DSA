"Find the customer with maximum total wealth."

def maximum_wealth(accounts):
    max_wealth = 0
    for customer in accounts:
        total_wealth = sum(customer)
        if total_wealth > max_wealth:
            max_wealth = total_wealth
    return max_wealth