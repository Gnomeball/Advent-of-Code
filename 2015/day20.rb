TARGET = 34000000

def factors(n)
    return [*1..n].delete_if { |e| n % e != 0 }
end

def factor_sum(n)
    return factors(n).sum * 10 # (because puzzle)
end

# Number derived from target / [1..10].sum
# Then round up a lot to a factor of 560
# (560 divides evenly by all of [1..10])
# In particular 1400 * 560
start = 784000

while true
    sum = factor_sum(start)
    if sum > TARGET
        print("House #{start} gets #{sum} presents\n")
        break
    end
    if start % 1000 == 0
        print("--- #{start} ---\n")
    end
    # We then only need to check values that divide by 560
    start += 560
end

# House 786240 gets 34137600 presents
