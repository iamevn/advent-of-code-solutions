function addCoord(t, c)
    if t[c.y] == nil then
        t[c.y] = {}
    end
    t[c.y][c.x] = true
end

santaCoord = {x = 0, y = 0}
roboCoord = {x = 0, y = 0}
santaTurn = true
delivered = {}
count = 1
addCoord(delivered, santaCoord)
for line in io.lines("input") do
    for dir in line:gmatch(".") do
        dx, dy = 0, 0
        if dir == '<' then
            dx = -1
        elseif dir == '>' then
            dx = 1
        elseif dir == '^' then
            dy = -1
        elseif dir == 'v' then
            dy = 1
        end
        if santaTurn then
            santaCoord.x = santaCoord.x + dx
            santaCoord.y = santaCoord.y + dy

            if delivered[santaCoord.y] == nil or delivered[santaCoord.y][santaCoord.x] == nil then
                count = count + 1
            end
            addCoord(delivered, santaCoord)

            santaTurn = false
        else
            roboCoord.x = roboCoord.x + dx
            roboCoord.y = roboCoord.y + dy

            if delivered[roboCoord.y] == nil or delivered[roboCoord.y][roboCoord.x] == nil then
                count = count + 1
            end
            addCoord(delivered, roboCoord)

            santaTurn = true
        end
    end
end

-- dc = 0
-- for i,v in pairs(delivered) do
--     dc = dc + #v
-- end
-- print(#delivered)
-- print(dc)
print(count)
