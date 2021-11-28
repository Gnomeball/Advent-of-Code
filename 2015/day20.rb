TARGET = 34000000

# === part 1 ===

def factors(n)
    return [*1..n/2+1].delete_if { |e| n % e != 0 }.push(n)
end

def factor_sum(n)
    return factors(n).sum * 10 # (because puzzle)
end

# Number derived from target / [1..10].sum then round up a lot
# to a factor of 560 (560 divides evenly by all of [1..10])
# In particular 1400 * 560
start = 784000

while true
    sum = factor_sum(start)
    if sum > TARGET
        print("Part 1 : House #{start} gets #{sum} presents\n")
        break
    end
    # We then only need to check values that divide by 560
    start += 560
end

# Yes this is slow, but is faster than the below approach with the asumptions

# === part 2 ===

houses = Array.new(1000000) { |v| 0 }

for h in 1..1000000 do
    for i in 1..50 do
        if i*h < 1000000
            houses[h*i] += 11 * h
        end
    end
end

the_house = houses.find_index { |v| v > TARGET }
print("Part 2 : House #{the_house} gets #{houses[the_house]} presents\n")

