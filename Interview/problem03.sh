if [ -z "$1" ]; then
    echo "Usage: $0 <filename.txt>"
    exit 1
fi

FILE="$1"

if [ ! -f "$FILE" ]; then
    echo "$FILE not found!"
    exit 1
fi

if [ $(wc -l < "$FILE") -lt 10 ]; then
    echo "$FILE has less than 10 lines."
    exit 1
fi

sed -n '10p' "$FILE"
