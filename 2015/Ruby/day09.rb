input = File.readlines("data/day09.txt", chomp: true)

def calculate_distance(route, routes)
    distance = 0
    for i in 0..route.length-2 do
        step = "#{route[i]} to #{route[i+1]}"
        distance += routes.fetch(step)
    end
    return distance
end

places = []
routes = {}

input.each do |i|
    route = i.split(" ")

    from = route[0]
    to = route[2]
    distance = route[4].to_i

    places.push(from)
    places.push(to)

    routes.store("#{from} to #{to}", distance)
    routes.store("#{to} to #{from}", distance)
end

places.uniq!

possible_routes = places.permutation.to_a

shortest = possible_routes.min_by { |x| calculate_distance(x, routes) }
longest = possible_routes.max_by { |x| calculate_distance(x, routes) }

print "#{shortest} = #{calculate_distance(shortest, routes)}\n"
print "#{longest} = #{calculate_distance(longest, routes)}\n"
