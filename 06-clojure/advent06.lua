width = 999
part = 'B'
lightshow = {}
for row = 0, width do
    lightshow[row] = {}
    for col = 0, width do
        lightshow[row][col] = 0
    end
end

function turn_off(row, col)
    if part == 'A' then
        lightshow[row][col] = 0
    else
        lightshow[row][col] = lightshow[row][col] - 1
        if lightshow[row][col] < 0 then lightshow[row][col] = 0 end
    end
end

function turn_on(row, col)
    if part == 'A' then
        lightshow[row][col] = 1
    else
        lightshow[row][col] = lightshow[row][col] + 1
    end
end

function toggle(row, col)
    if part == 'A' then
        if lightshow[row][col] == 1 then
            lightshow[row][col] = 0
        else
            lightshow[row][col] = 1
        end
    else
        lightshow[row][col] = lightshow[row][col] + 2
    end
end

fn = nil
for line in io.lines('input') do
    instr, origx, origy, destx, desty = string.match(line, "(.*) (%d+),(%d+) through (%d+),(%d+)")

    if instr == "turn off" then fn = turn_off
    elseif instr == "turn on" then fn = turn_on
    else fn = toggle end

    for y = origy, desty do
        for x = origx, destx do
            fn(y, x)
        end
    end
end

cnt = 0
for i, row in pairs(lightshow) do
    for j, val in pairs(row) do
        cnt = cnt + val
    end
end

print(cnt)


