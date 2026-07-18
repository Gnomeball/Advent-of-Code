class Reindeer

    attr_accessor :name
    attr_accessor :speed
    attr_accessor :move
    attr_accessor :sleep

    def initialize(name, speed, move, sleep)
        @name = name
        @speed = speed.to_i
        @move = move.to_i
        @sleep = sleep.to_i
    end

    def simulate(time)
        # initial = time
        distance = 0
        while time > 0 do
            if time < @move
                distance += speed
                time -= 1
                # print distance, " @ ", initial-time, ", "
            else
                distance += move * speed
                time -= (sleep + move)
                # print distance, " @ ", initial-time, ", "
            end
        end
        # print "\n"
        return distance
    end

end

input = File.readlines("data/day14.txt", chomp: true)

reindeers = []

input.each do |line|
    d = line.split(" ")
    reindeers.push(Reindeer.new(d[0], d[3], d[6], d[13]))
end

time = 2503
reindeers.each do |r|
    puts "After #{time} seconds, #{r.name} has traveled #{r.simulate(time)}"
end

# Part two was guessed (somehow correctly).
