require 'digest'

if ARGV[0] == nil
    puts("please provide key file")
    exit
end

key = File.open(ARGV[0]).read().gsub(/\r?\n?/,"")

n = 1
while true do
    if Digest::MD5.hexdigest(key + String(n))[0,5] == "00000"
        puts(n)
        break
    end
    n += 1
end

while true do
    if Digest::MD5.hexdigest(key + String(n))[0,6] == "000000"
        puts(n)
        break
    end
    n += 1
end
