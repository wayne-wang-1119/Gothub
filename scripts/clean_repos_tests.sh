# Remove every directory in repos

dir="./repos/tests"

for d in $dir/*; do
    if [ -d "$d" ]; then
        rm -rf "$d"
    fi
done
