function addCoord(t, c)
    if t[c.y] == nil then
        t[c.y] = {}
    end
    t[c.y][c.x] = true
end

currentCoord = {x = 0, y = 0}
delivered = {}
count = 1
addCoord(delivered, currentCoord)
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
        currentCoord.x = currentCoord.x + dx
        currentCoord.y = currentCoord.y + dy

        if delivered[currentCoord.y] == nil or delivered[currentCoord.y][currentCoord.x] == nil then
            count = count + 1
        end
        addCoord(delivered, currentCoord)
    end
end

dc = 0
for i,v in pairs(delivered) do
    dc = dc + #v
end
print(#delivered)
print(dc)
print(count)
