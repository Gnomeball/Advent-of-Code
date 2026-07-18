# input = File.readlines("data/day12.txt", chomp: true).map { |l| l.split("-") }

# print input, "\n"

# nodes = input.flatten.uniq

# print nodes, "\n"

# routes = {}

# for node in nodes
#     links = []
#     # if routes.key?(node) then
#     #     links = routes.fetch(node)
#     # end
#     for i in input
#         if i[0] == node then
#             links.push(i[1])
#         elsif i[1] == node then
#             links.push(i[0])
#         end
#     end
#     routes.store(node, links)
# end

# print routes, "\n"

# # def find_path(nodes, routes)

# # end

# def find_paths(nodes, routes)

#     paths = []

#     start = routes.fetch("start")
#     stop = routes.fetch("end")

#     possible_nodes = start.dup
#     while !possible_nodes.empty?
#         node = possible_nodes.shift
#         path = [start, node]
#         if node == stop then
#             path.push(stop)
#             paths.push(path)
#             next
#         end
#         # [start, A]

#     end

#     return paths

# end

# print find_paths(nodes, routes), "\n"
