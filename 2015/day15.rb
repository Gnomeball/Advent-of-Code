class Ingredient

    attr_accessor :name
    attr_accessor :capacity
    attr_accessor :durability
    attr_accessor :flavour
    attr_accessor :texture
    attr_accessor :calories

    def initialize(input)
        details = input.split(" ")
        @name = details[0].delete! ":"
        @capacity = details[2].to_i
        @durability = details[4].to_i
        @flavour = details[6].to_i
        @texture = details[8].to_i
        @calories = details[10].to_i
    end

end

def score(ingredients, selection)

    score = 0

    capacity = 0
    durability = 0
    flavour = 0
    texture = 0
    calories = 0

    for i in 0...ingredients.length do
        capacity += ingredients[i].capacity * selection[i]
        durability += ingredients[i].durability * selection[i]
        flavour += ingredients[i].flavour * selection[i]
        texture += ingredients[i].texture * selection[i]
        calories += ingredients[i].calories * selection[i]
    end

    if capacity < 1 then capacity = 0 end
    if flavour < 1 then flavour = 0 end
    if texture < 1 then texture = 0 end
    if durability < 1 then durability = 0 end

    # Toggle this for part 1
    # return capacity * durability * flavour * texture

    if calories == 500
        return capacity * durability * flavour * texture
    else
        return 0
    end

end

input = File.readlines("day15.txt", chomp: true)

ingredients = []
input.each { |i| ingredients.push(Ingredient.new(i)) }

selections = []

for i in 0..100 do
    for j in 0..100-i do
        for k in 0..100-i-j do
            selections.push([i, j, k, 100-i-j-k])
        end
    end
end

maximum = selections.max_by { |s| score(ingredients, s) }
puts "Maximum : #{score(ingredients, maximum)} from #{maximum}"
